<template>
  <div class="container-fluid mt-5">
    <div class="row">
      <SideBar
        :course="course"
        :activeWeek="activeWeek"
        @toggle-week="toggleWeek"
        @signout="signout"
        @go-to-dashboard="goToDashboard"
      />
      <main class="col-md-9 ml-sm-auto col-lg-9 px-md-4" style="position: relative; width: 80%; margin-left: auto;">
        <h2 class="impressive-header">Programming Assignment</h2>
        <p v-html="questionText"></p>
        <hr>
        <div v-if="analysisloading" class="analysis-loading-message">Analysing code...</div>

        <div v-else-if="qualityAnalysis && !analysisloading" class="analysis-result">
          <h5>Code Analysis Report:</h5>
          <ul>
            <markdown-renderer :markdown-text="qualityAnalysis"></markdown-renderer>
          </ul>
        </div>

        <div v-else class="analysis-result">
          <h5>Code Analysis Report:</h5>
          <p>
            Once you start writing your Python code in the editor, a comprehensive analysis will be displayed here.
            This report will evaluate your code for various quality aspects, including:
          </p>
          <ul>
            <li><strong>Code Smells:</strong> Identifying patterns in your code that may indicate deeper issues or areas for improvement.</li>
            <li><strong>Technical Debt:</strong> Highlighting areas where quick fixes or suboptimal solutions may lead to future maintenance challenges.</li>
            <li><strong>Blocker Bugs:</strong> Detecting critical issues that could cause your code to fail or behave unpredictably.</li>
            <li><strong>Vulnerabilities:</strong> Uncovering potential security risks in your code that could be exploited.</li>
          </ul>
          <p>
            As you continue coding, this analysis will be updated in real-time to provide you with insights on how to improve
            the quality and security of your code. Please start coding to see your report.
          </p>
        </div>
        <div class="editor-container" id="editor"></div>

        <!-- Icons Outside the Editor -->
        <div class="icon-container">
          <!-- Expand Icon -->
          <svg class="expand-icon"  @click="expandEditor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" width="24px" height="24px">
            <path d="M0 0h24v24H0z" fill="none"/>
            <path d="M5 15v4h4l-5 5-5-5h4v-4zm14-6v-4h-4l5-5 5 5h-4v4zm-14 0v-4h-4l5-5 5 5h-4v4zm14 6v4h4l-5 5-5-5h4v-4z"/>
          </svg>
          <!-- Compress Icon (initially hidden) -->
          <svg class="compress-icon" @click="compressEditor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" width="24px" height="24px" style="display: none;">
            <path d="M0 0h24v24H0V0z" fill="none"/>
            <path d="M19 19h-4v2h6v-6h-2v4zm0-14h-4V3h6v6h-2V5zM9 3H3v6h2V5h4V3zM5 19v-4H3v6h6v-2H5z"/>
          </svg>
        </div>

        <button class="btn btn-outline-secondary ml-2 mb-3" @click="testRun">Test Run</button>
        <div class="vr" style="border-left: 1px solid #100; height: 35px;"></div>
        <button class="btn btn-dark ml-2 mb-3" @click="submit">Submit</button>
        <div v-if="loading" class="loading-message">Running test cases...</div>

        <div v-if="testResults">
          <h3>Public Test Results:</h3>
          <ul>
            <li v-for="(result, index) in testResults.public" :key="index" class="test-result-horizontal">
              <p>
                <strong>Test Case {{ index + 1 }}:</strong>
                <span class="test-detail"><strong>Input:</strong> {{ result.input }}</span>
                <span class="separator">|</span>
                <span class="test-detail"><strong>Expected:</strong> {{ result.expected }}</span>
                <span class="separator">|</span>
                <span class="test-detail"><strong>Output:</strong> {{ result.output }}</span>
                <span class="separator">|</span>
                <span class="test-detail"><strong>Result:</strong> <span :class="{'text-success': result.result === 'Passed', 'text-danger': result.result !== 'Passed'}">{{ result.result }}</span></span>
              </p>
            </li>
          </ul>
        </div>

        <div v-if="submitResults">
          <h3>Private Test Results:</h3>
          <ul>
            <li v-for="(result, index) in submitResults.private" :key="index" class="test-result-horizontal">
              <p>
                <strong>Test Case {{ index + 1 }}:</strong>
                <span class="test-detail"><strong>Result:</strong> <span :class="{'text-success': result.result === 'Passed', 'text-danger': result.result !== 'Passed'}">{{ result.result }}</span></span>
              </p>
            </li>
          </ul>
        </div>

        <CodingWithAI :code="code" :questionText="questionText" :testResults="testResults?.public" :submitResults="submitResults?.private" />
      </main>
    </div>
  </div>
</template>

<script>
import MarkdownRenderer from '../components/MarkdownRenderer.vue';
import SideBar from '../components/SideBar.vue';
import CodingWithAI from '../components/CodingWithAI.vue';
import ace from 'ace-builds/src-noconflict/ace';
import 'ace-builds/src-noconflict/mode-python';
import 'ace-builds/src-noconflict/theme-monokai';

export default {
  name: 'CodePracticeAssignment',
  components: {
    SideBar,
    CodingWithAI,
    MarkdownRenderer
  },
  data() {
    return {
      analysisloading: false,
      code: '',
      questionText: '',
      testCases: [],
      loading: false,
      testResults: null,
      submitResults: null,
      course: null,
      activeWeek: null,
      editor: null
    };
  },
  created() {
    this.fetchData();
  },
  watch: {
    '$route': 'fetchData',
    code() {
      this.analyzeCode();
    },
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
        if (this.$route.name === 'CodePracticeAssignment') {
          this.fetchQuestions();
        }
      } catch (error) {
        console.error('Error fetching course data:', error);
      }
    },
    async fetchQuestions() {
      if (this.course && this.activeWeek) {
        const week = this.course.weeks.find(week => week.id === this.activeWeek);
        const codingQuestion = week ? week.questions.find(q => q.type === 'Coding') : null;
        if (codingQuestion) {
          this.questionText = codingQuestion.text;
          this.testCases = codingQuestion.test_cases;
        } else {
          this.code = '';
          this.questionText = '';
          this.testCases = [];
        }
        this.setupEditor();
        this.analyzeCode();
      }
    },
    toggleWeek(weekId) {
      this.activeWeek = this.activeWeek === weekId ? null : weekId;
    },
    setupEditor() {
      const editor = ace.edit('editor');
      editor.setTheme('ace/theme/monokai');
      editor.session.setMode('ace/mode/python');
      editor.setValue(this.code, 1);
      editor.on('change', () => {
        this.code = editor.getValue();
      });
      this.editor = editor;
    },
    extractFunctionName(code) {
      const functionNameMatch = code.match(/^def (\w+)/);
      return functionNameMatch ? functionNameMatch[1] : null;
    },
    expandEditor() {
      this.editor.container.style.width = '100%';
      this.editor.container.style.height = '350px';

      // Hide the expand icon
      this.$el.querySelector('.expand-icon').style.display = 'none';
      // Show the compress icon
      this.$el.querySelector('.compress-icon').style.display = 'inline';
    },
    compressEditor() {
      this.editor.container.style.width = '50%';
      this.editor.container.style.height = '350px';

      // Show the expand icon
      this.$el.querySelector('.expand-icon').style.display = 'inline';
      // Hide the compress icon
      this.$el.querySelector('.compress-icon').style.display = 'none';
    },
    async testRun() {
      this.loading = true;
      this.testResults = null;
      this.submitResults = null;
      const code = this.editor.getValue();
      const functionName = this.extractFunctionName(code);
      try {
        const response = await fetch('http://localhost:5000/ppa_test_run', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ code, testCases: this.testCases, functionName })
        });
        const data = await response.json();
        this.testResults = data.results;
      } catch (error) {
        console.error('Error running test cases:', error);
      } finally {
        this.loading = false;
      }
    },
    async submit() {
      this.loading = true;
      this.testResults = null;
      this.submitResults = null;
      const code = this.editor.getValue();
      const functionName = this.extractFunctionName(code);
      try {
        const response = await fetch('http://localhost:5000/ppa_submit', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ code, testCases: this.testCases, functionName })
        });
        const data = await response.json();
        this.submitResults = data.results;
      } catch (error) {
        console.error('Error submitting assignment:', error);
      } finally {
        this.loading = false;
      }
    },
    async analyzeCode() {
      this.analysisloading = true;
      try {
        const response = await fetch('http://localhost:5000/analyze', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ code: this.code }),
        });
        const data = await response.json();
        this.qualityAnalysis = data.issues;
      } catch (error) {
        console.error('Error analyzing code:', error);
      } finally {
        this.analysisloading = false;
      }
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

.editor-container {
  height: 350px;
  width: 50%;
  border: 1px solid #ddd;
  border-radius: 5px;
  margin-bottom: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  position: relative; /* Relative positioning to allow for absolute positioning of icons */
}

.icon-container {
  position: absolute;
  right: 20px;
  z-index: 20; /* Ensure the icons are on top of other elements */
}

.icon-container svg {
  cursor: pointer;
  background-color: white; /* Optional: add background color to make icons stand out */
  padding: 5px;
  border-radius: 50%;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin-left: 5px; /* Space between icons */
}

.loading-message {
  margin-top: 20px;
  margin-bottom: 20px;
  color: #ff0000;
}

.analysis-loading-message {
  position: absolute;
  right: 20px;
  width: 46%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  text-align: center;
  font-size: 16px;
  font-weight: bold;
}
.analysis-result {
  position: absolute;
  right: 20px;
  width: 46%;
  height: 350px;
  margin-left: 18px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
}

.vr {
  display: inline-block;
  border-left: 1px solid #000;
  margin: 0 15px;
  height: 100%;
  position: relative;
  top: 4px;
}
.test-result-horizontal p {
  margin: 0;
  font-size: 14px;
  display: flex;
  flex-wrap: nowrap;
  gap: 10px;
  align-items: center;
}

.test-detail {
  margin-right: 8px;
  flex-shrink: 0;
}

.separator {
  margin-right: 8px;
  color: #666;
}

.text-success {
  color: green;
}

.text-danger {
  color: red;
}


</style>
