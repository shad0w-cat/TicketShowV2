<template>
    <div>
         <h2 v-if="isAdminRoute">Admin Login</h2>
        <h2 v-else>User Login</h2>
        <form v-if="!isAdminRoute" @submit.prevent="userLogin">
            <div class="form-group">
                <label for="userUsername">Username</label>
                <input type="text" id="userUsername" v-model="userLoginForm.username" class="form-control">
            </div>
            <div class="form-group">
                <label for="userPassword">Password</label>
                <input type="password" id="userPassword" v-model="userLoginForm.password" class="form-control">
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
            <button class="btn btn-secondary" @click.prevent="redirectToUserRegistration">Register</button>
        </form>

       <form v-else @submit.prevent="adminLogin">
            <div class="form-group">
                <label for="adminUsername">Username</label>
                <input type="text" id="adminUsername" v-model="adminLoginForm.username" class="form-control">
            </div>
            <div class="form-group">
                <label for="adminPassword">Password</label>
                <input type="password" id="adminPassword" v-model="adminLoginForm.password" class="form-control">
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
        </form>
        <button v-if="!isAdminRoute" class="btn btn-secondary" @click.prevent="redirectToUserRegistration">Register</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            userLoginForm: {
                username: '',
                password: ''
            },
            adminLoginForm: {
                username: '',
                password: ''
            }
        };
    },
    computed: {
        isAdminRoute() {
            return this.$route.path === '/admin';
        }
    },
    methods: {
        userLogin() {
            // Handle user login logic
            console.log('User login:', this.userLoginForm);
        },
        adminLogin() {
            // Handle admin login logic
            console.log('Admin login:', this.adminLoginForm);
        },
        redirectToUserRegistration() {
            // Handle redirection to user registration page
            console.log('Redirect to user registration');
        }
    }
};
</script>