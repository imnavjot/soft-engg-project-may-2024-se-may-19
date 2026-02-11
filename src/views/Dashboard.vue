<template>
  <div class="container-fluid mt-5">
    <div class="row">
      <!-- Sidebar -->
      <nav class="col-md-3 col-lg-3 d-md-block bg-light sidebar" style="width: 20%;">
        <div class="d-flex flex-column justify-content-between sideMenu-content" style="height: 100%;">
          <div>
            <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
              <img src="../assets/iitmlogo.png" alt="Institute Logo" style="max-width: 150px;" class="img-fluid" />
            </a>
            <hr>
            <ul class="nav nav-pills flex-column mb-auto">
              <li class="nav-item">
                <router-link to="/dashboard" class="nav-link active" aria-current="page">
                  My Current Courses
                </router-link>
              </li>
              <li>
                <router-link to="/dashboard/updates" class="nav-link link-dark">
                  Latest Updates
                </router-link>
              </li>
              <li>
                <router-link to="/dashboard/exam" class="nav-link link-dark">
                  Hall Tickets
                </router-link>
              </li>
              <li>
                <router-link to="/dashboard/completed" class="nav-link link-dark">
                  Completed Courses
                </router-link>
              </li>
              <li>
                <router-link to="/dashboard/calendar" class="nav-link link-dark">
                  Academic Calendar
                </router-link>
              </li>
              <li>
                <router-link to="/dashboard/support" class="nav-link link-dark">
                  Support
                </router-link>
              </li>
            </ul>
          </div>
          <div class="mt-auto">
            <hr>
            <button class="btn btn-light mb-3" @click="signout">Sign Out</button>
          </div>
        </div>
      </nav>
      <!-- Right side: My current courses -->
      <main class="col-md-9 ml-sm-auto col-lg-9 px-md-4" style="position: relative; width: 80%; margin-left: auto;">
        <h2 class="text-left mb-4">My Current Courses</h2>
        <div class="row">
          <div class="col-md-4" v-if="loading">
            <p>Loading...</p>
          </div>
          <div class="col-md-4" v-for="course in courses" :key="course.id">
            <div class="card course-card mb-4">
              <img src="../assets/logo.png" class="card-img-top" alt="Course Image">
              <div class="card-body">
                <h5 class="card-title">{{ course.title }}</h5>
                <hr>
                <router-link :to="'/course/' + course.id + '/lecture/' + course.first_lecture_id" class="course-link">Go to course page</router-link>
              </div>
            </div>
          </div>
          <div class="col-md-4" v-if="error">
            <p>Error loading courses: {{ error }}</p>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DashboardPage',
  data() {
    return {
      courses: [],
      loading: false,
      error: null
    };
  },
  created() {
    this.fetchCourses();
  },
  methods: {
    async fetchCourses() {
      this.loading = true;
      try {
        const response = await fetch('http://localhost:5000/courses');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const courses = await response.json();
        this.courses = courses;
        console.log("Fetched courses:", this.courses);
      } catch (error) {
        console.error("Error fetching courses:", error);
        this.error = error.message;
      } finally {
        this.loading = false;
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
  overflow-y: auto;
  background-color: #f8f9fa;
  border-right: 2px solid #dee2e6;
}

.nav-link {
  text-align: left;
  padding-left: 15px;
  font-size: 1rem;
  font-weight: 450;
}

.nav-link.active {
  background-color: rgba(0, 0, 0, 0.1); /* Slightly dark and transparent */
}

.course-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: none;
  border-radius: 0.5rem;
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
}

.card-img-top {
  height: 100px;
  object-fit: cover;
  border-top-left-radius: 0.5rem;
  border-top-right-radius: 0.5rem;
}

.card-body {
  text-align: left;
}

.card-title {
  font-size: 1.1rem;
  margin: 5px 0;
}

.course-link {
  display: inline-block;
  text-decoration: none;
  font-weight: 500;
  float: right;
}

.course-link:hover {
  text-decoration: underline;
}

.card:hover {
  transform: translateY(-5px);
  transition: transform 0.2s;
}
</style>
