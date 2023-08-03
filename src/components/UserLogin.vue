<template>
    <div class="container d-flex justify-content-center align-items-center">
        <div class="login-form">
            <h2>User Login</h2>
            <br />
            <form @submit.prevent="userLogin" class="needs-validation">
                <div class="form-group">
                    <label for="userUsername">Email</label>
                    <input type="email" id="userUsername" v-model="userLoginForm.email" class="form-control" required>
                    <div class="invalid-feedback">Please enter your email.</div>
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
                email: '',
                password: ''
            },
        };
    },
    methods: {
        async userLogin() {
            try {
                const rawResponse = await fetch('http://127.0.0.1:8081/api/login', {
                    method: "POST",
                    body: JSON.stringify(this.userLoginForm),
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                    },
                });

                const response = await rawResponse.json()
                console.log('API response:', response);

                localStorage.setItem('username', response.username)
                localStorage.setItem('token', response.token)
                localStorage.setItem('userId', response.userId)
                this.onSuccessfulLogin();

            } catch (error) {
                // Handle any errors that occurred during the API call
                console.error('API error:', error);
            }
        },
        redirectToUserRegistration() {
            this.$router.push("/signup")
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