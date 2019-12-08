<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-body px-lg-5 py-lg-5">
          <div class="text-center text-muted mb-4">
            <small>Sign in with credentials</small>
          </div>
          <form action="#" @submit.prevent="login">
            <!--<input 
              class="input-group-alternative mb-3"
              placeholder="Email"
              name="username"
              id="username"
              addon-left-icon="ni ni-email-83"
              v-model="model.username"
            >
            <input
              class="input-group-alternative"
              placeholder="Password"
              type="password"
              name="password"
              id="password"
              addon-left-icon="ni ni-lock-circle-open"
              v-model="model.password"
            >
            -->
            <div class="form-control">
              <label for="email">Username/Email</label>
              <input
                type="text"
                name="username"
                id="username"
                class="login-input"
                v-model="model.username"
              />
            </div>

            <div class="form-control mb-more">
              <label for="password">Password</label>
              <input
                type="password"
                name="password"
                id="password"
                class="login-input"
                v-model="model.password"
              />
            </div>
            <base-checkbox class="custom-control-alternative">
              <span class="text-muted">Remember me</span>
            </base-checkbox>
            <div class="text-center">
              <button type="submit" class="btn my-4">Sign in</button>
            </div>
          </form>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-6">
          <a href="#" class="text-light">
            <small>Forgot password?</small>
          </a>
        </div>
        <div class="col-6 text-right">
          <router-link to="/register" class="text-light">
            <small>Create new account</small>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "login",
  data() {
    return {
      model: {
        username: "",
        password: ""
      }
    };
  },
  methods: {
    login() {
      //console.log(this.model.username);
      this.$store
        .dispatch("retrieveToken", {
          username: this.model.username,
          password: this.model.password
        })
        .then(response => {
          this.$router.push({ name: "dashboard" });
        });
      //console.log("wasap")
    }
  }
};
</script>
<style>
</style>
