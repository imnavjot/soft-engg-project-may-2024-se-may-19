import unittest
import requests
import uuid

BASE_URL = "http://localhost:5000"

class APITestCases(unittest.TestCase):

    def test_signup_success(self):
        unique_email = f"test_{uuid.uuid4()}@example.com"
        payload = {
            "email": unique_email,
            "password": "password123"
        }
        response = requests.post(f"{BASE_URL}/signup", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    def test_signup_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/signup", json=payload)
        self.assertEqual(response.status_code, 400)

    def test_login_success(self):
        payload = {
            "email": "test@example.com",
            "password": "password123"
        }
        response = requests.post(f"{BASE_URL}/login", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_login_bad_request(self):
        payload = {
            "email": "test@example.com"
        }
        response = requests.post(f"{BASE_URL}/login", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Missing email or password'})

    def test_logout_success(self):
        # First, log in the user
        login_payload = {
            "email": "test@example.com",
            "password": "password123"
        }
        login_response = requests.post(f"{BASE_URL}/login", json=login_payload)
        self.assertEqual(login_response.status_code, 200)

        # Now, attempt to log out
        response = requests.post(f"{BASE_URL}/signout")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())


    def test_fetch_courses_success(self):
        response = requests.get(f"{BASE_URL}/courses")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        # Example structure check
        if response.json():
            course = response.json()[0]
            self.assertIn("id", course)
            self.assertIn("title", course)
            self.assertIn("description", course)
            self.assertIn("first_lecture_id", course)

    def test_fetch_course_by_id_success(self):
        course_id = 1
        response = requests.get(f"{BASE_URL}/course/{course_id}")
        self.assertEqual(response.status_code, 200)
        course = response.json()
        self.assertIn("id", course)
        self.assertIn("title", course)
        self.assertIn("description", course)
        self.assertIn("weeks", course)
        self.assertIsInstance(course["weeks"], list)

    def test_fetch_course_by_id_not_found(self):
        course_id = 999
        response = requests.get(f"{BASE_URL}/course/{course_id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "Course not found"})

    def test_content_summary_complete_success(self):
        payload = {
            "videoId": 1,
            "type": "complete",
        }
        response = requests.post(f"{BASE_URL}/content_summary", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("summary", response.json())

    def test_content_summary_missing_summary_type(self):
        payload = {
            "videoId": 1
        }
        response = requests.post(f"{BASE_URL}/content_summary", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Invalid summary type"})

    def test_generate_questions_success(self):
        payload = {
            "videoId": 1,
            "endTime": 600
        }
        response = requests.post(f"{BASE_URL}/generate_questions", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("questions", response.json())

    def test_generate_questions_bad_request(self):
        payload = {
            "endTime": 600
        }  # Missing 'videoId' and 'endTime'
        response = requests.post(f"{BASE_URL}/generate_questions", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Missing videoId or endTime'})

    def test_evaluate_answers_success(self):
        payload = {
            "questions": [{"id": 1, "correct": "A"}],
            "answers": ["A"]
        }
        response = requests.post(f"{BASE_URL}/evaluate_answers", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("correct_count", response.json())

    def test_evaluate_answers_bad_request(self):
        payload = {
            "questions": [{"id": 1, "correct": "A"}]
        }
        response = requests.post(f"{BASE_URL}/evaluate_answers", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Questions or answers cannot be empty'})


    def test_summarize_pdf_success(self):
        payload = {"pdfUrl": "/lecture_1.pdf"}
        response = requests.post(f"{BASE_URL}/pdf_summary", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("summary", response.json())

    def test_summarize_pdf_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/pdf_summary", json=payload)
        self.assertEqual(response.status_code, 400)

    def test_ppa_test_run_success(self):
        payload = {
            "code": "def add(a, b): return a + b",
            "testCases": [
                {"input": [1, 2], "expected": 3},
                {"input": [2, 2], "expected": 4},
                {"input": [0, 0], "expected": 0},
                {"input": [-1, 1], "expected": 0}
            ],
            "functionName": "add"
        }
        response = requests.post(f"{BASE_URL}/ppa_test_run", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("results", response.json())

    def test_ppa_test_run_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/ppa_test_run", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Bad Request, missing data')

    def test_ppa_submit_success(self):
        payload = {
            "code": "def add(a, b): return a + b",
            "testCases": [
                {"input": [1, 2], "expected": 3},
                {"input": [2, 2], "expected": 4},
                {"input": [0, 0], "expected": 0},
                {"input": [-1, 1], "expected": 0}
            ],
            "functionName": "add"
        }
        response = requests.post(f"{BASE_URL}/ppa_submit", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("results", response.json())

    def test_ppa_submit_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/ppa_submit", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Bad Request, missing data')


    def test_get_pseudocode_success(self):
        payload = {"question": "Write a function to add two numbers."}
        response = requests.post(f"{BASE_URL}/pseudocode", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("pseudocode", response.json())

    def test_get_pseudocode_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/pseudocode", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'No question provided')

    def test_analyze_success(self):
        payload = {"code": "def add(a, b): return a + b"}
        response = requests.post(f"{BASE_URL}/analyze", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("issues", response.json())

    def test_analyze_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/analyze", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'No code provided')

    def test_feedback_success(self):
        payload = {
            "code": "def add(a, b): return a + b",
            "results": [
                {"input": [1, 2], "expected": 3, "output": 3, "result": "Passed"},
                {"input": [2, 2], "expected": 4, "output": 4, "result": "Passed"}
            ]
        }
        response = requests.post(f"{BASE_URL}/feedback", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("feedback", response.json())

    def test_feedback_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/feedback", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'No code provided')

    def test_improvement_success(self):
        payload = {"code": "def add(a, b): return a + b"}
        response = requests.post(f"{BASE_URL}/improvement", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("improvements", response.json())

    def test_improvement_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/improvement", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'No code provided')

    def test_gaanswers_success(self):
        payload = {"answers": [{"question_id": 1, "selected": "A"}]}
        response = requests.post(f"{BASE_URL}/gaanswers", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("correct_count", response.json())
        self.assertIn("feedback", response.json())

    def test_gaanswers_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/gaanswers", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Missing answers'})

    def test_gaimprovement_success(self):
        payload = {"feedback": [{"question": "Sample question?", "correct_answer": "A", "selected_answer": "B"}]}
        response = requests.post(f"{BASE_URL}/gaimprovement", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("improvements", response.json())

    def test_gaimprovement_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/gaimprovement", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'No feedback provided')

    def test_paanswers_success(self):
        payload = {"answers": [{"question_id": 1, "selected": "A"}]}
        response = requests.post(f"{BASE_URL}/paanswers", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("correct_count", response.json())
        self.assertIn("feedback", response.json())

    def test_paanswers_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/paanswers", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Bad Request, missing or incorrect data')

    def test_pahint_success(self):
        payload = {"question_id": 1}
        response = requests.post(f"{BASE_URL}/pahint", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("hint", response.json())

    def test_pahint_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/pahint", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Question ID is required')

    def test_paimprovement_success(self):
        payload = {"feedback": [{"question": "Sample question?", "correct_answer": "A", "selected_answer": "B"}]}
        response = requests.post(f"{BASE_URL}/paimprovement", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("improvements", response.json())

    def test_paimprovement_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/paimprovement", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'No feedback provided')

    def test_chat_success(self):
        payload = {"prompt": "Hello, how are you?"}
        response = requests.post(f"{BASE_URL}/chat", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("chat", response.json())

    def test_chat_bad_request(self):
        payload = {}
        response = requests.post(f"{BASE_URL}/chat", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'No prompt provided')
if __name__ == '__main__':
    unittest.main()
