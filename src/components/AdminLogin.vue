<template>
    <div class="container d-flex justify-content-center align-items-center">
        <div class="login-form">
            <h2>Admin Login</h2>
            <br />
            <form @submit.prevent="adminLogin">
                <div class="form-group">
                    <label for="adminUsername">Username</label>
                    <input type="text" id="adminUsername" v-model="adminLoginForm.username" class="form-control">
                </div>
                <br />
                <div class="form-group">
                    <label for="adminPassword">Password</label>
                    <input type="password" id="adminPassword" v-model="adminLoginForm.password" class="form-control">
                </div>
                <br />
                <button type="submit" class="btn btn-primary">Login</button>
            </form>
        </div>
    </div>
</template>

<script>
// import axios from 'axios';

export default {
    data() {
        return {
            adminLoginForm: {
                username: '',
                password: ''
            },
        };
    },
    methods: {
        async adminLogin() {
            try {
                // const response = await axios.post('/login', {
                //     username: this.adminLoginForm.username,
                //     password: this.adminLoginForm.password
                // });

                // const token = response.data.token;
                // const expirationDays = 7;
                // const expirationDate = new Date();
                // expirationDate.setDate(expirationDate.getDate() + expirationDays);
                // document.cookie = `admin_token=${token}; expires=${expirationDate.toUTCString()}; path=/`;

                // console.log('API response:', response.data);

                localStorage.setItem('username', this.adminLoginForm.username)
                localStorage.setItem('userRole', 'admin')
                this.onSuccessfulLogin();

            } catch (error) {
                // Handle any errors that occurred during the API call
                console.error('API error:', error);
            }
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