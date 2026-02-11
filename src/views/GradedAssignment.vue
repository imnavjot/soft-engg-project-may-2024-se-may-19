<template>
  <div class="container-fluid mt-5">
    <div class="row">
      <!-- Sidebar -->
      <SideBar
        :course="course"
        :activeWeek="activeWeek"
        @toggle-week="toggleWeek"
        @select-lecture="selectLecture"
        @signout="signout"
        @go-to-dashboard="goToDashboard"
      />
      <main class="col-md-9 ml-sm-auto col-lg-9 px-md-4" style="position: relative; width: 80%; margin-left: auto;">
        <h2 class="impressive-header">Graded Assignment</h2>
        <div v-if="questions.length === 0">
          <p>Loading questions...</p>
        </div>
        <div v-else>
          <div v-for="(question, index) in questions" :key="question.id" class="mb-4">
            <p>{{ index + 1 }}. {{ question.text }}</p>
            <div v-for="option in question.options" :key="option.label" class="form-check">
              <input
                class="form-check-input"
                type="radio"
                :name="'question-' + question.id"
                :id="'option-' + question.id + '-' + option.label"
                :value="option.label"
                v-model="answers[question.id]"
                :disabled="showCorrectAnswers"
              />
              <label class="form-check-label" :for="'option-' + question.id + '-' + option.label">
                {{ option.label }}. {{ option.text }}
              </label>
            </div>
            <div v-if="showCorrectAnswers">
              <p class="text-success">
                Correct Answer: {{ question.correct_answer }}
              </p>
              <p v-if="answers[question.id] !== question.correct_answer" class="text-danger">
                Your Answer: {{ answers[question.id] }}
              </p>
            </div>
          </div>
          <button class="btn btn-primary mt-3" @click="submitAnswers">Submit</button>
        </div>
        <div v-if="feedback.length > 0">
          <button class="btn btn-secondary mt-3" @click="getImprovements">Get Improvements</button>
        </div>
        <div v-if="improvements && !loading" class="result">
          <h5>AI generated feedback:</h5>
            <markdown-renderer :markdown-text="improvements"></markdown-renderer>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import SideBar from '../components/SideBar.vue';
import MarkdownRenderer from '../components/MarkdownRenderer.vue';

export default {
  name: 'PracticeAssignment',
  components: {
    SideBar,
    MarkdownRenderer
  },
  data() {
    return {
      course: null,
      activeWeek: null,
      questions: [],
      answers: {},
      feedback: [],
      improvements: '',
      showCorrectAnswers: false
    };
  },
  created() {
    this.fetchData();
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    async fetchData() {
      const courseId = this.$route.params.courseId;
      const weekId = this.$route.params.weekId;

      try {
        const response = await fetch(`http://localhost:5000/course/${courseId}`);
        const data = await response.json();
        this.course = data;
        this.activeWeek = parseInt(weekId, 10) || (this.course.weeks[0] ? this.course.weeks[0].id : null);
        this.fetchQuestions();
      } catch (error) {
        console.error('Error fetching course data:', error);
      }
    },
    async fetchQuestions() {
      if (this.course && this.activeWeek) {
        const week = this.course.weeks.find(week => week.id === this.activeWeek);
        if (week) {
          this.questions = week.questions.filter(question => question.type === 'MCQ');
        } else {
          this.questions = [];
        }
        this.showCorrectAnswers = false;
        this.answers = {};
      }
    },
    toggleWeek(weekId) {
      this.activeWeek = this.activeWeek === weekId ? null : weekId;
    },
    async submitAnswers() {
      try {
        const response = await fetch('http://localhost:5000/gaanswers', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ answers: Object.entries(this.answers).map(([question_id, selected]) => ({ question_id, selected })) })
        });
        const data = await response.json();
        if (response.ok) {
          this.feedback = data.feedback;
          this.showCorrectAnswers = true;
          this.questions.forEach(question => {
            const feedbackItem = this.feedback.find(item => item.question === question.text);
            if (feedbackItem) {
              question.correct_answer = feedbackItem.correct_answer;
            } else {
              question.correct_answer = question.options.find(option => option.label === this.answers[question.id]).label;
            }
          });
        } else {
          console.error('Error:', data.error);
        }
      } catch (error) {
        console.error('Error submitting answers:', error);
      }
    },
    async getImprovements() {
      this.loading = true;
      try {
        const response = await fetch('http://localhost:5000/gaimprovement', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ feedback: this.feedback })
        });
        const data = await response.json();
        if (response.ok) {
          this.improvements = data.improvements;
        } else {
          console.error('Error:', data.error);
        }
      } catch (error) {
        console.error('Error fetching improvements:', error);
      } finally {
        this.loading = false;
      }
    },
    selectLecture(lecture) {
      this.$router.push({ name: 'CoursePage', params: { id: this.course.id, lectureId: lecture.id } });
    },
    async signout() {
      try {
        const response = await fetch('http://localhost:5000/signout', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
        });

        if (response.ok) {
          this.$router.push('/login');
        } else {
          console.error('Error during signout:', response.statusText);
          // Handle error (e.g., show error message)
        }
      } catch (error) {
        console.error('Error during signout:', error);
        // Handle error (e.g., show error message)
      }
    },
    goToDashboard() {
      this.$router.push('/dashboard');
    }
  }
};
</script>

<style scoped>
.impressive-header {
  display: inline-block;
  font-size: 1.1em;
  font-weight: bold;
  color: #2c3e50;
  padding: 10px 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px 0;
  border-left: 5px solid #007bff;
  text-align: left;
}

.loading-message {
  margin-top: 20px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9;
  text-align: center;
  font-size: 16px;
  font-weight: bold;
}

.result {
  margin-top: 20px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
</style>
