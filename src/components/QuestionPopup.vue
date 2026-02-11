<template>
  <div v-if="showPopup" class="popup-overlay">
    <div class="popup-content">
      <h2>MCQ Assignment</h2>
      <div v-if="questions.length === 0 && !isFetching">
        <p>Loading questions...</p>
        <button class="btn btn-secondary mt-3" @click="closePopup">Close</button>
      </div>
      <div v-else-if="questions.length === 0 && isFetching">
        <p>Fetching questions, please wait...</p>
        <button class="btn btn-secondary mt-3" @click="closePopup">Close</button>
      </div>
      <div v-else>
        <div v-for="(question, index) in questions" :key="index" class="question-item">
          <p><strong>Question {{ index + 1 }}:</strong> {{ question.question }}</p>
          <ul class="list-group">
            <li v-for="option in question.options" :key="option" class="list-group-item">
              <label>
                <input class="form-check-input" type="radio" :name="'question-' + index" :value="option" v-model="answers[index]" :disabled="isSubmitted">
                {{ option }}
              </label>
            </li>
            <!-- Show the correct answer after submission -->
            <span v-if="isSubmitted">
            <p  style="color: black;">
              Correct Answer: {{ question.correct }}
            </p>
            </span>
          </ul>
        </div>
        <div v-if="message" :style="{ color: messageColor }" class="alert alert-secondary mt-3">{{ message }}</div>
        <div class="d-flex justify-content-between mt-3">
          <button class="btn btn-primary" @click="submitAnswers" :disabled="isSubmitted">Submit</button>
          <button class="btn btn-secondary ml-3" @click="closePopup">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'QuestionPopup',
  props: {
    showPopup: {
      type: Boolean,
      default: false
    },
    videoId: {
      type: Number,
      required: true
    },
    currentTime: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      questions: [],
      answers: [],
      isFetching: false,
      isSubmitted: false, // Track if the answers have been submitted
      message: '' // For displaying submission messages
    };
  },
  watch: {
    showPopup(newValue) {
      if (newValue) {
        this.fetchQuestions();
        this.message = ''; // Clear previous messages when a new popup opens
        this.isSubmitted = false; // Reset submission status when a new popup opens
      }
    }
  },
  methods: {
    closePopup() {
      this.$emit('close-popup');
    },
    async fetchQuestions() {
      this.isFetching = true;
      const maxRetries = 5; // Maximum number of retries
      let attempts = 0;

      while (attempts < maxRetries) {
        try {
          const response = await fetch('http://localhost:5000/generate_questions', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              videoId: this.videoId,
              endTime: this.currentTime
            })
          });

          if (!response.ok) {
            throw new Error('Network response was not ok');
          }

          const data = await response.json();
          console.log('Fetched questions:', data.questions);

          if (data.questions && data.questions.length > 0) {
            this.questions = data.questions;
            this.answers = Array(this.questions.length).fill(null);
            break; // Exit loop if questions are successfully fetched
          } else {
            console.warn('No questions received, retrying...');
          }
        } catch (error) {
          console.error('Error fetching questions:', error);
        }

        attempts++;
        if (attempts < maxRetries) {
          await new Promise(resolve => setTimeout(resolve, 5000)); // Wait 5 seconds before retrying
        } else {
          // Final warning if retries are exhausted
          console.warn('Maximum retry attempts reached. No questions received.');
          this.questions = []; // Ensure questions is an empty array
        }
      }

      this.isFetching = false;
    },
    async submitAnswers() {
      try {
        const response = await fetch('http://localhost:5000/evaluate_answers', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            questions: this.questions,
            answers: this.answers
          })
        });
        const data = await response.json();
        const correctCount = data.correct_count;

        if (correctCount >= 3) {
          this.message = `Great job! You answered ${correctCount} out of 5 questions correctly. You can move forward.`;
          this.messageColor = 'green'; // Set the message color to green

        } else {
          this.message = `You answered only ${correctCount} out of 5 questions correctly. Please revisit the lecture.`;
          this.messageColor = 'red'; // Set the message color to red

        }

        this.isSubmitted = true; // Mark as submitted
      } catch (error) {
        console.error('Error evaluating answers:', error);
        this.message = 'An error occurred while evaluating your answers.';
      }
    }
  }
};
</script>


<style scoped>
.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.popup-content {
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 80%;
  max-width: 750px;
  max-height: 80vh;
  overflow-y: auto; /* Make the popup scrollable */
  box-sizing: border-box;
}

.question-item {
  margin-bottom: 20px;
}

.list-group-item {
  border: none;
}

.alert {
  word-wrap: break-word;
}

.popup-content::-webkit-scrollbar {
  width: 10px;
}

.popup-content::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 5px;
}

.popup-content::-webkit-scrollbar-thumb:hover {
  background: #555;
}

.popup-content::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 5px;
}

</style>
