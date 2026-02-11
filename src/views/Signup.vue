<template>
  <div class="container mt-5">
    <img src="../assets/iitmlogo.png" alt="Institute Logo" style="max-width: 200px;" class="mx-auto d-block mb-4" />
    <h1 class="text-center">Sign Up</h1>
    <div class="card mx-auto" style="max-width: 400px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
      <div class="card-body">
        <form @submit.prevent="signup">
          <div class="mb-3">
            <label for="email" class="form-label">Email:</label>
            <input type="email" class="form-control" v-model="email" required />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password:</label>
            <input type="password" class="form-control" v-model="password" required />
          </div>
          <button type="submit" class="btn btn-primary btn-block">Sign Up</button>
        </form>
        <p class="mt-3 text-center">
          Already have an account? <router-link to="/login">Login</router-link>
        </p>
        <p class="mt-3 text-center">
          <router-link to="/">Back to Home</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignupPage',
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    async signup() {
      try {
        const response = await fetch('http://localhost:5000/signup', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password
          })
        });
        const data = await response.json();
        if (response.ok) {
          this.$router.push('/login');
        } else {
          alert(data.message);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
};
</script>

<style scoped>
.card {
  background-color: #f8f9fa; /* Light gray background */
  border: none; /* Remove border */
  transition: transform 0.2s; /* Add smooth hover effect */
}

.card:hover {
  transform: translateY(-5px); /* Move card up slightly on hover */
}

.form-control:focus {
  border-color: #80bdff; /* Change border color on focus */
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25); /* Add focus effect */
}
</style>
