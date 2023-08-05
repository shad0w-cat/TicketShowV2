import { createRouter, createWebHistory } from 'vue-router';
import Layout from '@/components/Layout/MainLayout.vue';
import UserRegistration from '../components/UserRegistration.vue';
import AdminDashboard from '../components/AdminDashboard.vue';
import UserDashboard from '../components/UserDashboard.vue';
import UserLogin from '../components/UserLogin.vue';
import { getUserRole } from '@/utils';
import BookingShows from '@/components/BookingShows.vue';
import UserProfile from '@/components/UserProfile.vue';

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
      path: '/signup',
      name: 'Registration',
      component: UserRegistration,
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
          component: async () => {
            const userRole = await getUserRole();
            console.log(userRole);

            if (userRole === UserRoles.Admin) {
              return AdminDashboard;
            } else {
              return UserDashboard;
            }
          },
        },
        {
          path: 'booking/:showId',
          component: BookingShows,
        },
        {
          path: 'profile',
          component: UserProfile,
        },
      ],
    },
  ],
});

router.beforeEach(async (to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
  if (requiresAuth) {
    if (!isLoggedIn()) {
      next('/login');
    } else {
      const requiredRoles = to.meta.requiredRoles;
      const userRole = await getUserRole();
      console.log(userRole);
      if (!userRole || !requiredRoles.includes(userRole)) {
        console.log('HERE ysrad sdafgsd');

        next('/login');
      } else {
        next();
      }
    }
  } else {
    next();
  }
});

function isLoggedIn() {
  const token = localStorage.getItem('token');
  console.log(!!token);
  return !!token;
}

export default router;
