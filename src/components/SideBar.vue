<template>
  <nav class="col-md-3 col-lg-3 d-md-block bg-light sidebar" style="width: 20%;">
    <div class="d-flex flex-column justify-content-between sideMenu-content" style="height: 100%;">
      <div v-if="course">
        <img src="../assets/iitmlogo.png" alt="Institute Logo" style="max-width: 170px;" class="img-fluid" />
        <h4 class="course-title">{{ course.title }}</h4>
        <hr>
        <div class="menu-section">
        <ul class="nav nav-pills flex-column mb-auto">
          <li v-for="week in course.weeks" :key="week.id" class="nav-item">
            <a class="nav-link dropdown-toggle" :class="{'active': activeWeek === week.id}" @click="toggleWeek(week.id)" role="button" aria-expanded="false">
              {{ week.title }}
            </a>
            <div class="collapse" :id="'week' + week.id" :class="{'show': activeWeek === week.id}">
              <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                <li v-for="lecture in week.lectures" :key="lecture.id">
                  <router-link :to="{ name: 'CoursePage', params: { id: course.id, lectureId: lecture.id } }" class="nav-link link-dark">
                    {{ lecture.title }}
                  </router-link>
                  <router-link :to="{ name: 'PdfViewer', params: { courseId: course.id, lectureId: lecture.id } }" class="nav-link link-secondary">
                    View PDF
                  </router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'CodePracticeAssignment', params: { courseId: course.id, weekId: week.id } }" class="nav-link link-dark">
                    Coding Assignment
                  </router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'PracticeAssignment', params: { courseId: course.id, weekId: week.id } }" class="nav-link link-dark">
                    Practice Assignment
                  </router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'GradedAssignment', params: { courseId: course.id, weekId: week.id } }" class="nav-link link-dark">
                    Graded Assignment
                  </router-link>
                </li>
              </ul>
            </div>
          </li>
        </ul>
        </div>
      </div>
      <div v-else>
        <p>Loading...</p> <!-- Optional: Show a loading indicator while course data is loading -->
      </div>
      <div class="mt-auto">
        <hr>
        <button class="btn btn-light ml-2 mb-3" @click="signout">Sign Out</button>
        <div class="vr" style="border-left: 1px solid #000; height: 24px;"></div>
        <button class="btn btn-light mr-2 mb-3" @click="goToDashboard">Home</button>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'SideBar',
  props: {
    course: {
      type: Object,
      required: true
    },
    activeWeek: {
      type: Number,
      required: false
    }
  },
  methods: {
    toggleWeek(weekId) {
      this.$emit('toggle-week', weekId);
    },
    signout() {
      this.$emit('signout');
    },
    goToDashboard() {
      this.$emit('go-to-dashboard');
    }
  }
};
</script>

<style scoped>
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  z-index: 100;
  padding-top: 30px; /* Height of the fixed navbar */
  overflow-x: hidden;
  overflow-y: hidden;
  background-color: #f8f9fa;
  border-right: 2px solid #dee2e6;
}

.course-title {
  font-size: 1.25em;
  font-weight: bold;
  margin: 15px 0 10px;
  text-align: left;
  padding-left: 10px;
  border-left: 4px solid #007bff;
}


.menu-section {
  overflow-y: auto;
}

.nav-link {
  text-align: left;
  padding: 10px 15px; /* Adjust padding for better spacing */
  font-size: 1rem;
  font-weight: 450;
  color: #333; /* Darker color for better readability */
  transition: background-color 0.3s ease, color 0.3s ease; /* Smooth transitions */
}

.nav-link:hover {
  background-color: #e9ecef; /* Light gray on hover */
  color: #000;
}

.nav-link.active {
  background-color: #007bff; /* Bootstrap primary color */
  color: #fff; /* White text on active */
}

.btn-toggle-nav .nav-link {
  padding-left: 30px; /* Indent nested links */
}
</style>
