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
      <h2 class="impressive-header">Lecture Slides</h2>
        <div class="pdf-container">
          <embed :src="pdfUrl" type="application/pdf" class="pdf-embed" />
        </div>
        <PdfSummary :pdfUrl="pdfUrl" />
        <IntegratedChatComponent />
      </main>
    </div>
  </div>
</template>

<script>
import SideBar from '../components/SideBar.vue';
import PdfSummary from '../components/PdfSummary.vue';
import IntegratedChatComponent from '../components/IntegratedChatComponent.vue';


export default {
  name: 'PdfViewer',
  components: {
    SideBar,
    PdfSummary,
    IntegratedChatComponent
  },
  data() {
    return {
      course: null,
      activeWeek: null,
      pdfUrl: ''
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
    const lectureId = this.$route.params.lectureId;

    try {
      const response = await fetch(`http://localhost:5000/course/${courseId}`);
      const data = await response.json();
      this.course = data;
      console.log('Fetching course data for course ID:', courseId);
      console.log('Fetched course data:', this.course);

      // Set the PDF URL based on the lecture ID
      this.pdfUrl = `/lecture_${lectureId}.pdf`; // Ensure correct path to PDF
    } catch (error) {
      console.error('Error fetching course data:', error);
      // Handle error (e.g., show error message, redirect to error page)
    }
  },
    toggleWeek(weekId) {
      this.activeWeek = this.activeWeek === weekId ? null : weekId;
    },
    selectLecture(lecture) {
      // Navigate back to the CoursePage for the selected lecture
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

.pdf-container {
  display: flex;
  align-items: center;
  height: 80vh; /* Adjust height as needed */
  overflow-x: hidden; /* Prevent horizontal scrolling */
}

.pdf-embed {
  width: 90%;
  height: 90%;
  max-width: 700px; /* Limit maximum width */
  border: 2px solid #ddd; /* Optional: Add border for clarity */
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* Optional: Add shadow for depth */
}
</style>
