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
import { getUserRole } from '@/utils.js';

export default {
    data() {
        return {
            username: localStorage.getItem('username'),
            userRole: null,
        };
    },
    methods: {
        logout() {
            this.clearToken();
            this.redirectToLoginPage();
        },
        clearToken() {
            localStorage.removeItem('token')
        },
        redirectToLoginPage() {
            this.$router.push('/login');
        },
    },
    components: {
        AdminHeader,
        UserHeader,
    },

    async created() {
        this.userRole = await getUserRole();
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
