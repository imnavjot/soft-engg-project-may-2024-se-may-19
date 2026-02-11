# app.py
from flask import Flask, request, jsonify, redirect, url_for, session
from docx import Document
import re
from flask_cors import CORS
import logging
from io import BytesIO
from PyPDF2 import PdfReader
import traceback
import requests
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import User, db, Question, Week, Course, Option, Lecture
from __init__ import create_app, bcrypt
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = create_app()

# Enable CORS
CORS(app)

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

GROQ_API_KEY = "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"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def query(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        course_list = []
        for course in courses:
            first_lecture = None
            if course.weeks and course.weeks[0].lectures:
                first_lecture = course.weeks[0].lectures[0]
            course_list.append({
                "id": course.id,
                "title": course.title,
                "description": course.description,
                "first_lecture_id": first_lecture.id if first_lecture else None
            })
        return jsonify(course_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/course/<int:course_id>', methods=['GET'])
def get_course(course_id):
    try:
        app.logger.info(f"Fetching course with ID: {course_id}")
        course = Course.query.get(course_id)
        if not course:
            app.logger.warning(f"Course with ID {course_id} not found")
            return jsonify({"error": "Course not found"}), 404

        course_data = {
            "id": course.id,
            "title": course.title,
            "description": course.description,
            "weeks": []
        }

        for week in course.weeks:
            lectures_data = [{"id": lecture.id, "title": lecture.title, "description": lecture.description, "video_url": lecture.video_url} for lecture in week.lectures]

            questions_data = []
            for question in week.questions:
                options_data = [{"id": option.id, "text": option.text, "label": option.label} for option in question.options]
                questions_data.append({
                    "id": question.id,
                    "text": question.text,
                    "correct_answer": question.correct_answer,
                    "options": options_data,
                    "code": question.code,
                    "test_cases": question.test_cases,
                    "type": question.type
                })

            course_data["weeks"].append({
                "id": week.id,
                "title": week.title,
                "lectures": lectures_data,
                "questions": questions_data
            })

        return jsonify(course_data)
    except SQLAlchemyError as e:
        app.logger.error(f"SQLAlchemy error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
    except Exception as e:
        app.logger.error(f"Error fetching course data: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Bad Request, missing email or password'}), 400

    email = data['email']
    password = data['password']

    try:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(email=email, password=hashed_password, name=email.split('@')[0])
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()


        # Check for missing email or password
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Missing email or password'}), 400

        email = data['email']
        password = data['password']

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401

    return jsonify({'message': 'Login page'})

@app.route('/signout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

# Helper function to extract text from DOCX file
def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Helper function to get partial summary based on end time
def get_partial_summary(text, end_time):
    time_pattern = re.compile(r'\(Refer Slide Time: (\d+):(\d+)\)')
    lines = text.split('\n')
    partial_text = ""
    for line in lines:
        match = time_pattern.search(line)
        if match:
            minutes, seconds = map(int, match.groups())
            slide_time_seconds = minutes * 60 + seconds
            if slide_time_seconds > end_time:
                break
        partial_text += line + "\n"
    return partial_text.strip()

# Route for content summary endpoint
@app.route('/content_summary', methods=['POST'])
def summarize():
    data = request.get_json()
    video_id = data.get('videoId')
    summary_type = data.get('type')
    end_time = data.get('endTime')

    # Define the path to the DOCX file (adjust path as per your setup)
    file_path = f'src/assets/{video_id}.docx'

    try:
        # Extract text from the DOCX file
        text = extract_text_from_docx(file_path)
    except Exception as e:
        logger.error(f'Error extracting text from DOCX: {str(e)}')
        return jsonify({'error': str(e)}), 500

    if summary_type == 'complete':
        logger.info('Performing complete summary...')
        # Invoke Hugging Face API
        prompt = (
            "Please summarize the following lecture. The summary should be presented in a clear, structured manner with bullet points. "
            "Each point should highlight a key concept or idea from the lecture:\n\n"
            f"{text}"
        )
        response = query(prompt)

        # extract the generated text
        summary = response['choices'][0]['message']['content'].replace(prompt, "").strip()
    elif summary_type == 'partial':
        if end_time is not None:
            logger.info(f'Performing partial summary up to endTime: {end_time}...')
            partial_text = get_partial_summary(text, end_time)
            prompt = (
                "Please summarize the following lecture. The summary should be presented in a clear, structured manner with bullet points. "
                "Each point should highlight a key concept or idea from the lecture:\n\n"
                f"{partial_text}"
            )
            # Invoke Hugging Face API
            # Invoke Hugging Face API
            response = query(prompt)

            # extract the generated text
            summary = response['choices'][0]['message']['content'].replace(prompt, "").strip()
        else:
            logger.error('endTime is required for partial summary')
            return jsonify({'error': 'endTime is required for partial summary'}), 400
    else:
        logger.error('Invalid summary type')
        return jsonify({'error': 'Invalid summary type'}), 400

    logger.info(f'Summary generated: {summary}')

    return jsonify({'summary': summary})

@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    data = request.get_json()
    video_id = data.get('videoId')
    end_time = data.get('endTime')


    if not video_id or not end_time:
        return jsonify({'error': 'Missing videoId or endTime'}), 400

    # Load document and extract text
    file_path = f'src/assets/{video_id}.docx'
    text = extract_text_from_docx(file_path)
    partial_text = get_partial_summary(text, end_time)
    prompt = (
        f"Create 5 multiple choice questions from the text provided:\n{partial_text}\n"
        f"The output format should be:\n"
        f"1: question, 4 choices, correct answer\n"
        f"2: question, 4 choices, correct answer\n"
        f"3: question, 4 choices, correct answer\n"
        f"4: question, 4 choices, correct answer\n"
        f"5: question, 4 choices, correct answer\n\n"
        f"Format each question as follows:\n"
        f"Question: <question_text>\n"
        f"A) <option1>\n"
        f"B) <option2>\n"
        f"C) <option3>\n"
        f"D) <option4>\n"
        f"Correct answer: <correct_option>"
    )

    try:
        # Invoke Groq API
        response = query(prompt)
        # extract the generated text
        questions_text = response['choices'][0]['message']['content'].replace(partial_text, "").strip()

        # Parse the questions into a structured format (you may need to adjust this based on the response format)
        questions = parse_questions(questions_text)

        return jsonify({'questions': questions}), 200

    except Exception as e:
        logger.error(f'Error generating questions: {str(e)}')
        return jsonify({'error': str(e)}), 500

def parse_questions(questions_text):
    questions = []
    lines = questions_text.split('\n')
    current_question = None
    current_options = []

    for line in lines:
        if line.startswith("Question:"):
            if current_question:
                questions.append({
                    "question": current_question,
                    "options": current_options,
                    "correct": current_correct
                })
            current_question = line.replace("Question: ", "").strip()
            current_options = []
            current_correct = None
        elif line.startswith(("A)", "B)", "C)", "D)")):
            current_options.append(line.strip())
        elif line.startswith("Correct answer:"):
            current_correct = line.replace("Correct answer: ", "").strip()

    if current_question:
        questions.append({
            "question": current_question,
            "options": current_options,
            "correct": current_correct
        })

    return questions

@app.route('/evaluate_answers', methods=['POST'])
def evaluate_answers():
    data = request.get_json()
    questions = data.get('questions', [])
    answers = data.get('answers', [])

    # Check if questions or answers are empty
    if not questions or not answers:
        return jsonify({'error': 'Questions or answers cannot be empty'}), 400

    correct_count = 0
    for question, answer in zip(questions, answers):
        if question['correct'] == answer:
            correct_count += 1

    return jsonify({'correct_count': correct_count}), 200

# Helper function to extract text from PDF file
def extract_text_from_pdf(file_path1):
    with open(file_path1, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

# Route for PDF summary endpoint
@app.route('/pdf_summary', methods=['POST'])
def summarize_pdf():
    data = request.get_json()

    if not data or 'pdfUrl' not in data:
        return jsonify({'error': 'Bad Request, missing pdfUrl'}), 400

    pdf_url = data.get('pdfUrl')

    # Define the path to the PDF file (adjust path as per your setup)
    file_path1 = f'public{pdf_url}'

    try:
        # Extract text from the PDF file
        text = extract_text_from_pdf(file_path1)
    except Exception as e:
        logger.error(f'Error extracting text from PDF: {str(e)}')
        return jsonify({'error': str(e)}), 500

    logger.info('Performing complete summary...')
        # Invoke Hugging Face API
        # Invoke Hugging Face API
    prompt = (
        "Please summarize the following lecture. The summary should be presented in a clear, structured manner with bullet points. "
        "Also provide with clickable external Links(websites and reaserch articles must be related to computer science fields) related to the content of the course  which can be helpful for the learner."
        "Each point should highlight a key concept or idea from the lecture:\n\n"
        f"{text}\n\n"
    )
    response = query(prompt)

        # extract the generated text
    summary = response['choices'][0]['message']['content'].replace(prompt, "").strip()
    logger.info(f'Summary generated: {summary}')

    return jsonify({'summary': summary}), 200

@app.route('/ppa_test_run', methods=['POST'])
def test_run():
    data = request.json
    if not data or 'code' not in data or 'testCases' not in data or 'functionName' not in data:
        return jsonify({'error': 'Bad Request, missing data'}), 400
    code = data.get('code')
    test_cases = data.get('testCases')
    function_name = data.get('functionName')

    try:
        results = run_tests(code, test_cases, function_name, public_only=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({"results": results})

@app.route('/ppa_submit', methods=['POST'])
def submit():
    data = request.json

    if not data or 'code' not in data or 'testCases' not in data or 'functionName' not in data:
        return jsonify({'error': 'Bad Request, missing data'}), 400

    code = data.get('code')
    test_cases = data.get('testCases')
    function_name = data.get('functionName')
    try:
        results = run_tests(code, test_cases, function_name, public_only=False)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    # Save submission details to the database if needed
    return jsonify({"results": results})

def run_tests(code, test_cases, function_name, public_only=True):
    results = {
        "public": [],
        "private": []
    }

    public_cases = test_cases[:2]
    private_cases = test_cases[2:]

    # Define a safe namespace to exec the code
    safe_namespace = {}

    try:
        exec(code, {}, safe_namespace)
    except Exception as e:
        # If there's an error in the provided code, all tests will fail
        error_message = f"Error in code: {str(e)}"
        results['public'] = [{"input": test['input'], "expected": test['expected'], "output": None, "result": error_message} for test in public_cases]
        results['private'] = [{"result": error_message} for test in private_cases]
        return results

    def test_case(test):
        try:
            # Ensure that the function is callable
            func = safe_namespace.get(function_name)
            if func and callable(func):
                output = func(*test['input'])
                result = "Passed" if output == test['expected'] else "Failed"
            else:
                output = None
                result = "Error: Function not callable or not found"
        except Exception as e:
            output = None
            result = f"Error: {str(e)}"
        return {
            "input": test['input'],
            "expected": test['expected'],
            "output": output,
            "result": result
        }

    for test in public_cases:
        results['public'].append(test_case(test))

    if not public_only:
        for test in private_cases:
            results['private'].append(test_case(test))

    return results


@app.route('/pseudocode', methods=['POST'])
def get_pseudocode():
    data = request.get_json()
    question = data.get('question')

    if not question:
        logger.error('No question provided')
        return jsonify({'error': 'No question provided'}), 400

    try:
        prompt = (
            "Generate pseudocode for the following problem statement:\n\n"
            f"{question}\n\n"
            "Your pseudocode should outline the key steps required to solve the problem in a high-level and conceptual manner. "
            "Focus on describing the logic and flow of the solution rather than providing exact code. Include key elements such as loops, conditionals, and function calls, but avoid specific syntax or detailed implementation. "
            "Ensure the pseudocode is structured, clear, and easy to follow, serving as a guide for writing the actual code. "
            "Do not provide complete or runnable code; aim to present a high-level plan to assist in coding the solution."
        )

        # Invoke Hugging Face API
        response = query(prompt)

        # extract the generated text
        pseudocode = response['choices'][0]['message']['content'].replace(prompt, "").strip()
        logger.info(f'Code analysis generated: {pseudocode}')
        return jsonify({'pseudocode': pseudocode})

    except Exception as e:
        logger.error(f'Error fetching analysis: {str(e)}')
        return jsonify({'error': str(e)}), 500

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    code = data.get('code')

    if not code:
        logger.error('No code provided')
        return jsonify({'error': 'No code provided'}), 400

    try:
        prompt = (
            "Analyze the following code(Python) for quality issues including code smells, technical debt, blocker bugs, and vulnerabilities:\n\n"
            f"{code}\n\n"
            "Provide the issues in a structured format as follows:\n"
            "1. **Issue:** [Short Description of the Issue]\n\n"
            "   **Location:** [Line Number or Section]\n\n"
            "   **Suggestion:** [Concise Recommendation for Improvement]\n\n"
            "2. **Issue:** [Short Description of the Issue]\n\n"
            "   **Location:** [Line Number or Section]\n\n"
            "   **Suggestion:** [Concise Recommendation for Improvement]\n\n"
            "Ensure the output is clear and structured, listing each issue with a brief description, its location in the code, and a concise suggestion for improvement. Format it in a way that is easy to read and actionable, similar to what you would find in an IDE or code review tool."
            "Do not provide complete solution or code; focus on guiding the user to find and fix the errors themselves."
            "Ensure there is Numbering and a horizontal line between each issue to maintain clarity and readability."
        )
        # Invoke LLM API
        response = query(prompt)

        # extract the generated text
        issues = response['choices'][0]['message']['content'].replace(prompt, "").strip()
        logger.info(f'Code analysis generated: {issues}')
        return jsonify({'issues': issues})

    except Exception as e:
        logger.error(f'Error fetching analysis: {str(e)}')
        return jsonify({'error': str(e)}), 500


@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    code = data.get('code')
    results = data.get('results')
    if not code:
        logger.error('No code provided')
        return jsonify({'error': 'No code provided'}), 400

    try:
        prompt = (
            "Analyze the following code for errors and provide feedback or hints to correct these errors. Below is the code provided by the user:\n\n"
            f"{code}\n\n"
            "Results of the test cases performed:\n\n"
            f"{results}\n\n"
            "Please provide feedback in the following structured format:\n\n"
            "1. **Issue:** [Brief Description of the Error]\n\n"
            "   **Location:** [Line Number or Code Section]\n\n"
            "   **Feedback:** [Brief Explanation of the Problem]\n\n"
            "   **Hint:** [Guidance or Hint to Correct the Error]\n\n"
            "2. **Issue:** [Brief Description of the Error]\n\n"
            "   **Location:** [Line Number or Code Section]\n\n"
            "   **Feedback:** [Brief Explanation of the Problem]\n\n"
            "   **Hint:** [Guidance or Hint to Correct the Error]\n\n"
            "Ensure that each issue is described clearly with actionable feedback and hints."
            "Do not provide complete solutions or code; focus on guiding the user to find and fix the errors themselves."
        )
        response = query(prompt)

        # extract the generated text
        feedback = response['choices'][0]['message']['content'].replace(prompt, "").strip()

        logger.info(f'Code analysis generated: {feedback}')
        return jsonify({'feedback': feedback})

    except Exception as e:
        logger.error(f'Error fetching analysis: {str(e)}')
        return jsonify({'error': str(e)}), 500

@app.route('/improvement', methods=['POST'])
def improvement():
    data = request.get_json()
    code = data.get('code')

    if not code:
        logger.error('No code provided')
        return jsonify({'error': 'No code provided'}), 400

    try:
        prompt = (
            "Analyze the following code. It is currently passing all test cases, but please suggest any potential improvements or optimizations that can be made. "
            "Below is the code provided by the user:\n\n"
            f"{code}\n\n"
            "Please provide your suggestions in the following format:\n\n"
            "1. **Improvement Area:** [Brief Description of the Improvement]\n\n"
            "   **Reason:** [Why this improvement is beneficial]\n\n"
            "   **Suggestion:** [Specific advice or example code for implementing the improvement]\n\n"
            "2. **Improvement Area:** [Brief Description of the Improvement]\n\n"
            "   **Reason:** [Why this improvement is beneficial]\n\n"
            "   **Suggestion:** [Specific advice or example code for implementing the improvement]\n\n"
            "Focus on providing actionable feedback that can enhance code quality, readability, maintainability, or performance. Avoid discussing the correctness of the code since it is already passing all tests."
        )
        response = query(prompt)

        # extract the generated text
        improvements = response['choices'][0]['message']['content'].replace(prompt, "").strip()

        logger.info(f'Code analysis generated: {improvements}')
        return jsonify({'improvements': improvements})

    except Exception as e:
        logger.error(f'Error fetching analysis: {str(e)}')
        return jsonify({'error': str(e)}), 500

@app.route('/gaanswers', methods=['POST'])
def gaanswers():
    data = request.get_json()

        # Check if the 'answers' key is missing
    if 'answers' not in data:
        return jsonify({'error': 'Missing answers'}), 400

    answers = data.get('answers', [])

    correct_count = 0
    feedback = []
    for answer in answers:
        question = Question.query.get(answer['question_id'])
        # Check if question exists
        if not question:
            return jsonify({'error': f'Question with id {question_id} not found'}), 404

        if question.correct_answer == answer['selected']:
            correct_count += 1
        else:
            feedback.append({
                'question': question.text,
                'correct_answer': question.correct_answer,
                'selected_answer': answer['selected']
            })

    return jsonify({'correct_count': correct_count, 'feedback': feedback}), 200

@app.route('/gaimprovement', methods=['POST'])
def gaimprovement():
    data = request.get_json()
    feedback = data.get('feedback', [])

    if not feedback:
        return jsonify({'error': 'No feedback provided'}), 400

    try:
        prompt = "Here is some feedback on the following questions:\n"
        for item in feedback:
            prompt += f"Question: {item['question']}\n"
            prompt += f"Correct answer: {item['correct_answer']}\n"
            prompt += f"Selected answer: {item['selected_answer']}\n"

        prompt += "Please provide detailed explanations and suggestions for improvement."

        response = query(prompt)
        improvements = response['choices'][0]['message']['content'].strip()

        return jsonify({'improvements': improvements})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/paanswers', methods=['POST'])
def paanswers():
    data = request.get_json()

    if not data or 'answers' not in data:
        return jsonify({'error': 'Bad Request, missing or incorrect data'}), 400

    answers = data.get('answers', [])

    correct_count = 0
    feedback = []
    for answer in answers:
        question = Question.query.get(answer['question_id'])
        if question.correct_answer == answer['selected']:
            correct_count += 1
        else:
            feedback.append({
                'question': question.text,
                'correct_answer': question.correct_answer,
                'selected_answer': answer['selected']
            })

    return jsonify({'correct_count': correct_count, 'feedback': feedback})

@app.route('/pahint', methods=['POST'])
def pahint():
    data = request.get_json()
    question_id = data.get('question_id')

    if not question_id:
        return jsonify({'error': 'Question ID is required'}), 400

    try:
        question = Question.query.get(question_id)
        if not question:
            return jsonify({'error': 'Question not found'}), 404

        prompt = f"Question: {question.text}\n"
        for option in question.options:
            prompt += f"{option.label}. {option.text}\n"
        prompt += "Please provide a hint for the correct answer without revealing the solution."

        response = query(prompt)
        hint = response['choices'][0]['message']['content'].strip()

        return jsonify({'hint': hint})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/paimprovement', methods=['POST'])
def paimprovement():
    data = request.get_json()
    feedback = data.get('feedback', [])

    if not feedback:
        return jsonify({'error': 'No feedback provided'}), 400

    try:
        prompt = "Here is some feedback on the following questions:\n"
        for item in feedback:
            prompt += f"Question: {item['question']}\n"
            prompt += f"Correct answer: {item['correct_answer']}\n"
            prompt += f"Selected answer: {item['selected_answer']}\n"

        prompt += "Please provide detailed explanations and suggestions for improvement."
        prompt += "Also provide with clickable external Links(websites and reaserch articles must be related to computer science fields) related to the questions improving their knowledge  which can be helpful for the learner."

        response = query(prompt)
        improvements = response['choices'][0]['message']['content'].strip()

        return jsonify({'improvements': improvements})

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        # Replace with actual Groq API call
        prompt = f"AI response to: {prompt}"
        response = query(prompt)
        chat = response['choices'][0]['message']['content'].replace(prompt, "").strip()
        return jsonify({'chat': chat})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask application

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
