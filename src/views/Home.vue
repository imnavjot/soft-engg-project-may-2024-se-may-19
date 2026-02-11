<template>
  <div class="container text-center mt-5">
    <img src="../assets/iitmlogo.png" alt="Institute Logo" style="max-width: 200px;" />
    <h1 class="display-4">Welcome to the Project</h1>
    <p class="lead">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <div class="card mx-auto" style="max-width: 400px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
      <div class="card-body">
        <h5 class="card-title">Get Started</h5>
        <p class="card-text">Choose an option below to begin.</p>
        <div class="d-grid gap-2">
          <router-link to="/login" class="btn btn-primary">Login</router-link>
          <router-link to="/signup" class="btn btn-secondary">Sign Up</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
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
</style>
