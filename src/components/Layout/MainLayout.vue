<template>
    <div>
        <AdminHeader v-if="userRole === 'admin'" :username="username" @logout="logout" />
        <UserHeader v-else :username="username" @logout="logout" />

        <main>
            <router-view></router-view>
        </main>
    </div>
</template>

<script>
import AdminHeader from './AdminHeader.vue';
import UserHeader from './UserHeader.vue';

export default {
    data() {
        return {
            username: localStorage.getItem('username'),
            userRole: localStorage.getItem('userRole'),
        };
    },
    methods: {
        logout() {
            this.clearToken();
            this.redirectToLoginPage();
        },
        clearToken() {
            document.cookie = "admin_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        },
        redirectToLoginPage() {
            this.$router.push('/login');
        },
    },
    components: {
        AdminHeader,
        UserHeader,
    },
};
</script>

<style>
header {
    background-color: #f0f0f0;
    padding: 10px;
}

.user-info {
    display: flex;
    align-items: center;
    flex-direction: row;
    justify-content: space-between;
}

.button {
    display: flex;
    align-items: center;
    flex-direction: row;
    justify-content: space-between;
    gap: 10px;
}
</style>
