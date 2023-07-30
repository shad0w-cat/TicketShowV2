<template>
    <header>
        <div class="user-info">
            <h4>Hello, {{ username }}</h4>
            <div class="button">
                <button @click="goToProfile">Profile</button>
                <button @click="logout">Logout</button>
            </div>
        </div>
    </header>
</template>

<script>
export default {
    props: ['username'],
    methods: {
        logout() {
            // Implement your logout logic here
            // For example, clearing the token and redirecting to the login page
            // Assuming you have implemented a logout function that handles this.
            this.$emit('logout');
        },
        goToProfile() {
            // Implement logic to navigate to the user's profile page
            // For example, using Vue Router:
            this.$router.push('/profile');
        },
    },
};
</script>

<style>
/* Styles for the user header */
</style>
