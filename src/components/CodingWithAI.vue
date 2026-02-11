<template>
  <div>
    <button class="ai-button" @mouseover="aiButtonHover" @mouseleave="aiButtonLeave" @click="provideAI">{{ aiButtonText }}</button>
    <div v-if="loading" class="loading-message">Generating...</div>
    <div v-if="aiOutput && !loading" class="result">
        <h5>AI generated pseudocode:</h5>
      <markdown-renderer :markdown-text="aiOutput"></markdown-renderer>
    </div>
    <div v-if="feedback && !loading" class="result">
      <h5>AI generated feedback:</h5>
        <markdown-renderer :markdown-text="feedback"></markdown-renderer>
    </div>
  </div>
</template>

<script>
import MarkdownRenderer from '../components/MarkdownRenderer.vue';

export default {
  name: 'CodingWithAI',
  components: {
    MarkdownRenderer
  },
  props: {
    code: String,
    questionText: String,
    testResults: Array,
    submitResults: Array,
  },
  data() {
    return {
      loading: false,
      aiOutput: null,
      feedback: null,
      qualityAnalysis: null,
      aiButtonText: 'AI'
    };
  },
  methods: {
    async provideAI() {
      this.loading = true;
      try {
        const response = await fetch('http://127.0.0.1:5000/pseudocode', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ question: this.questionText }),
        });
        const data = await response.json();
        this.aiOutput = data.pseudocode;
      } catch (error) {
        console.error('Error fetching AI pseudocode:', error);
      } finally {
        this.loading = false;
      }
    },
    aiButtonHover() {
      this.aiButtonText = 'Learn with AI';
    },
    aiButtonLeave() {
      this.aiButtonText = 'AI';
    },
    async provideFeedback() {
      this.loading = true;
      try {
        const failedCases = this.testResults.filter(result => result !== 'Passed');
        if (failedCases.length > 0) {
          const response = await fetch('http://127.0.0.1:5000/feedback', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: this.code, results: failedCases }),
          });
          const data = await response.json();
          this.feedback = data.feedback;
        } else {
          const response = await fetch('http://127.0.0.1:5000/improvement', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: this.code }),
          });
          const data = await response.json();
          this.feedback = data.improvements;
        }
      } catch (error) {
        console.error('Error fetching AI feedback:', error);
      } finally {
        this.loading = false;
      }
    },
  },
  watch: {
    testResults(newValue, oldValue) {
      if (newValue !== oldValue) {
        this.provideFeedback();
      }
    },
  },
};
</script>

<style scoped>
.ai-button {
  position: absolute;
  top: 20px;
  right: 20px;
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.ai-button:hover {
  background-color: #0056b3;
  transform: scale(1.05);
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
