<template>
  <div>
    <button class="ai-button" @mouseover="aiButtonHover" @mouseleave="aiButtonLeave" @click="summarize" title="Click the button to get the AI-generated summary of the slide">{{ aiButtonText }}</button>
    <div v-if="loading" class="loading-message">Generating summary...</div>
    <div v-if="summaryResult && !loading" class="summary-result">
      <h5>Summary:</h5>
      <markdown-renderer :markdown-text="summaryResult"></markdown-renderer>
    </div>
  </div>
</template>

<script>
import MarkdownRenderer from '../components/MarkdownRenderer.vue';

export default {
  components: {
    MarkdownRenderer
  },
  data() {
    return {
      loading: false,
      summaryResult: null,
      aiButtonText: 'AI'
    };
  },
  props: {
    pdfUrl: {
      type: String,
      required: true
    }
  },
  methods: {
    async summarize() {
      this.loading = true;
      const data = { pdfUrl: this.pdfUrl};

      try {
        const response = await fetch('http://127.0.0.1:5000/pdf_summary', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const responseData = await response.json();
        this.summaryResult = responseData.summary;
      } catch (error) {
        console.error('Error fetching summary:', error);
      } finally {
        this.loading = false;
      }
    },
    aiButtonHover() {
      this.aiButtonText = 'Learn with AI';
    },
    aiButtonLeave() {
      this.aiButtonText = 'AI';
    }
  }
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

.summary-result {
  margin-top: 20px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
</style>
