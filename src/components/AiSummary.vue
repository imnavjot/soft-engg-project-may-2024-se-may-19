<template>
  <div>
    <button class="ai-button" @mouseover="aiButtonHover" @mouseleave="aiButtonLeave" @click="showOptions = !showOptions">{{ aiButtonText }}</button>
    <div v-if="showOptions" class="ai-options">
      <button class="close-button" @click="showOptions = false">⛌</button>
      <h5>Summarize Lecture</h5>
      <hr>
      <ul>
        <li @click="summarize('complete')">Complete Lecture</li>
        <li @click="summarize('partial')">From Start to Paused Point</li>
      </ul>
    </div>
  </div>
  <div v-if="loading" class="loading-message">Generating summary...</div>
  <div v-if="summaryResult && !loading" class="summary-result">
    <h5>Summary:</h5>
    <markdown-renderer :markdown-text="summaryResult"></markdown-renderer>
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
      showOptions: false,
      summaryResult: null,
      aiButtonText: 'AI',
      loading: false
    };
  },
  props: {
    videoId: {
      type: Number,
      required: true
    },
    currentTime: {
      type: Number,
      required: true
    }
  },
  methods: {
    async summarize(option) {
      this.loading = true;
      let data = { videoId: this.videoId };

      if (option === 'complete') {
        data.type = 'complete';
      } else if (option === 'partial') {
        data.type = 'partial';
        data.endTime = this.currentTime;
        console.log("End time for partial summary before request:", this.currentTime); // Debugging line
      }

      try {
        const response = await fetch('http://127.0.0.1:5000/content_summary', {
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


    watch: {
      currentTime(newTime) {
        console.log("Updated currentTime in AiSummary:", newTime); // Debugging line
        this.endTime = newTime;
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

.ai-options {
  position: absolute;
  top: 10px;
  right: 20px;
  background: white;
  border: 1px solid #ccc;
  padding: 15px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px; /* Rounded corners */
}

.ai-options ul {
  list-style-type: none;
  padding: 5px;
}

.ai-options li {
  margin: 10px 0;
  cursor: pointer;
  transition: background-color 0.3s; /* Smooth transition for background color */
  padding: 10px 15px; /* Padding for the choices */
  border-radius: 5px; /* Rounded corners for the choices */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle box shadow */
}

.ai-options li:hover {
  background-color: #f2f2f2; /* Light background color on hover */
}

.ai-options li.active {
  background-color: #007bff; /* Highlighted background color for selected option */
  color: white; /* Text color for selected option */
}

.close-button {
  position: absolute;
  top: 12px;
  right: 15px;
  padding: 7px 10px;
  font-size: 12px;
  background-color: transparent;
  color: #333;
  border: none;
  border-radius: 40px;
  cursor: pointer;
  transition: color 0.3s; /* Smooth transition for color change */
}

.close-button:hover {
  color: #555;
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

.summary-button {
padding: 10px 12px;
font-size: 15px;
bottom: 10px;
background-color: transparent;
color: #333;
border: none;
border-radius: 7px;
cursor: pointer;
transition: color 0.3s; /* Smooth transition for color change */
}

.summary-result {
margin-top: 20px;
margin-bottom: 20px;
padding: 10px;
border: 1px solid #ddd;
border-radius: 5px;
box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.ai-options button {
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
}

.ai-options button:hover {
  background-color: #0056b3;
}
</style>
