// router.js
import { createRouter, createWebHistory } from 'vue-router';
import store from '../store';
import HomePage from '../views/Home.vue';
import LoginPage from '../views/Login.vue';
import SignupPage from '../views/Signup.vue';
import DashboardPage from '../views/Dashboard.vue';
import CoursePage from '../views/Course.vue';
import PdfViewer from '../views/PdfViewer.vue';
import PracticeAssignment from '../views/PracticeAssignment.vue';
import GradedAssignment from '../views/GradedAssignment.vue';
import CodePracticeAssignment from '../views/CodePracticeAssignment.vue';

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/signup', name: 'Signup', component: SignupPage },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardPage,
    meta: { requiresAuth: true }
  },
  {
    path: '/course/:id/lecture/:lectureId',
    name: 'CoursePage',
    component: CoursePage,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: '/course/:courseId/lecture/:lectureId/pdf',
    name: 'PdfViewer',
    component: PdfViewer,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: '/course/:courseId/code/:weekId',
    name: 'CodePracticeAssignment',
    component: CodePracticeAssignment,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: '/course/:courseId/practice/:weekId',
    name: 'PracticeAssignment',
    component: PracticeAssignment,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: '/course/:courseId/graded/:weekId',
    name: 'GradedAssignment',
    component: GradedAssignment,
    props: true,
    meta: { requiresAuth: true }
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.isLoggedIn) {
      next({ name: 'Login' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
