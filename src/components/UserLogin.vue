<template>
    <div class="container d-flex justify-content-center align-items-center">
        <div class="login-form">
            <h2>User Login</h2>
            <br />
            <form @submit.prevent="userLogin" class="needs-validation">
                <div class="form-group">
                    <label for="userUsername">Username</label>
                    <input type="text" id="userUsername" v-model="userLoginForm.username" class="form-control" required>
                    <div class="invalid-feedback">Please enter your username.</div>
                </div>
                <br />
                <div class="form-group">
                    <label for="userPassword">Password</label>
                    <input type="password" id="userPassword" v-model="userLoginForm.password" class="form-control" required>
                    <div class="invalid-feedback">Please enter your password.</div>
                </div>
                <br />
                <button type="submit" class="btn btn-primary">Login</button> &nbsp;
                <button class="btn btn-secondary" @click.prevent="redirectToUserRegistration">Register</button>
            </form>
        </div>
    </div>
</template>

<script>
// import axios from 'axios';
export default {
    data() {
        return {
            userLoginForm: {
                username: '',
                password: ''
            },
        };
    },
    methods: {
        async userLogin() {
            try {
                // const response = await axios.post('http://127.0.0.1:8081/login', {
                //     username: this.userLoginForm.username,
                //     password: this.userLoginForm.password
                // });

                // // Handle the response from the API here
                // // For example, you can check the response status or data
                // const token = response.data.token;
                // const expirationDays = 7;
                // const expirationDate = new Date();
                // expirationDate.setDate(expirationDate.getDate() + expirationDays);
                // document.cookie = `user_token=${token}; expires=${expirationDate.toUTCString()}; path=/`;

                // console.log('API response:', response.data);

                localStorage.setItem('username', this.userLoginForm.username)
                localStorage.setItem('userRole', 'user')
                this.onSuccessfulLogin();
            } catch (error) {
                // Handle any errors that occurred during the API call
                console.error('API error:', error);
            }
        },
        redirectToUserRegistration() {
            // Handle redirection to user registration page
            console.log('Redirect to user registration');
        },
        onSuccessfulLogin() {
            // this.$router.push('/');
            window.location.href = '/';
        }
    }
};
</script>

<style>
.container {
    height: 100vh;
    /* background-color: darkkhaki; */
}

.login-form {
    width: 500px;
    /* height: 300px; */
    padding: 50px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: lightgray;
}
</style>