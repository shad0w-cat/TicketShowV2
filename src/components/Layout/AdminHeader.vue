<template>
    <header>
        <div class="user-info">
            <h4>Hello, {{ username }}</h4>
            <div class="button">
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
    },
};
</script>

<style>
/* Styles for the admin header */
</style>
