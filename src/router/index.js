import { createRouter, createWebHistory } from 'vue-router';
import Layout from '@/components/Layout/MainLayout.vue';
import AdminLogin from '../components/AdminLogin.vue';
import AdminDashboard from '../components/AdminDashboard.vue';
import UserDashboard from '../components/UserDashboard.vue';
import UserLogin from '../components/UserLogin.vue';
// import axios from 'axios';

const UserRoles = {
  Admin: 'admin',
  User: 'user',
};

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      name: 'User Login',
      component: UserLogin,
      meta: { requiresAuth: false },
    },
    {
      path: '/admin',
      name: 'Admin Login',
      component: AdminLogin,
      meta: { requiresAuth: false },
    },
    {
      path: '/',
      component: Layout,
      meta: {
        requiresAuth: true,
        requiredRoles: [UserRoles.Admin, UserRoles.User],
      },
      children: [
        {
          path: '',
          component: () => {
            const userRole = getUserRole();
            console.log(userRole);

            if (userRole === UserRoles.Admin) {
              return AdminDashboard;
            } else {
              return UserDashboard;
            }
          },
        },
      ],
    },
  ],
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);

  if (requiresAuth && !isLoggedIn()) {
    const requiredRoles = to.meta.requiredRoles;
    const userRole = getUserRole();

    if (!userRole || !requiredRoles.includes(userRole)) {
      next('/login');
    } else {
      next();
    }
  } else {
    next();
  }
});

function isLoggedIn() {
  const token = localStorage.getItem('username');
  return !!token;
}

function getUserRole() {
  return localStorage.getItem('userRole');
  // try {
  //   const response = await axios.get('127.0.0.1:8081/userRole', {
  //     headers: {
  //       Authorization: `Bearer ${localStorage.getItem('token')}`,
  //     },
  //   });
  //   console.log('Data from new API call:', response.data);
  // } catch (error) {
  //   console.error('New API call error:', error);
  // }
}

export default router;
