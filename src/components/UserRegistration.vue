<template>
    <div class="container d-flex justify-content-center align-items-center">
        <div class="login-form">
            <h2>User Registration</h2>
            <br />
            <form @submit.prevent="userRegistration">
                <div class="form-group">
                    <label for="firstname">First Name</label>
                    <input type="text" id="firstname" v-model="userRegistrationForm.firstname" class="form-control">
                </div>
                <br />
                <div class="form-group">
                    <label for="lastname">Password</label>
                    <input type="text" id="lastname" v-model="userRegistrationForm.lastname" class="form-control">
                </div>
                <br />
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" v-model="userRegistrationForm.username" class="form-control">
                </div>
                <br />
                <div class="form-group">
                    <label for="adminUsername">Email</label>
                    <input type="email" id="adminUsername" v-model="userRegistrationForm.email" class="form-control">
                </div>
                <br />
                <div class="form-group">
                    <label for="adminPassword">Password</label>
                    <input type="password" id="adminPassword" v-model="userRegistrationForm.password" class="form-control">
                </div>
                <br />
                <button type="submit" class="btn btn-primary">Sign Up</button>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            userRegistrationForm: {
                email: '',
                firstname: '',
                lastname: '',
                username: '',
                password: ''
            },
        };
    },
    methods: {
        async userRegistration() {
            try {
                const rawResponse = await fetch('http://127.0.0.1:8081/api/signup', {
                    method: "POST",
                    body: JSON.stringify(this.userRegistrationForm),
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                    },
                });

                const response = await rawResponse.json()
                console.log('API response:', response);
                this.onSuccessfulRegistration();

            } catch (error) {
                // Handle any errors that occurred during the API call
                console.error('API error:', error);
            }
        },
        onSuccessfulRegistration() {
            // this.$router.push('/');
            window.location.href = '/login';
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