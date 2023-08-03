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
            this.$emit('logout');
        },
        goToProfile() {
            this.$router.push('/profile');
        },
    },
};
</script>

<style>
/* Styles for the user header */
</style>
