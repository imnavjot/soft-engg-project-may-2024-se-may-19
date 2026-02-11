import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

// Import Bootstrap and BootstrapVue CSS files
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
// Import Bootstrap JS and its dependencies
import 'bootstrap/dist/js/bootstrap.bundle.min';
import '@fortawesome/fontawesome-free/css/all.css';

createApp(App).use(store).use(router).mount('#app');
