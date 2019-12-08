import Vue from 'vue'
import Router from 'vue-router'
import DashboardLayout from '@/layout/DashboardLayout'
import AuthLayout from '@/layout/AuthLayout'
Vue.use(Router)

export default new Router({
  linkExactActiveClass: 'active',
  routes: [
    {
      path: '/',
      redirect: 'dashboard',
      component: DashboardLayout,
      meta: {
        requiresAuth: true,
      },
      children: [
        {
          path: '/dashboard',
          name: 'dashboard',

          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "demo" */ './views/Dashboard.vue')
        },
        {
          path: '/icons',
          name: 'icons',
          component: () => import(/* webpackChunkName: "demo" */ './views/Icons.vue')
        },
        {
          path: '/segment/:id',
          name: 'segment',
          component: () => import(/* webpackChunkName: "demo" */ './views/Segment.vue')
        },
        {
          path: '/maps',
          name: 'maps',
          component: () => import(/* webpackChunkName: "demo" */ './views/Maps.vue')
        },
        {
          path: '/audios',
          name: 'audios',
          component: () => import(/* webpackChunkName: "demo" */ './views/Audios.vue')
        },
        {
          path: '/segments/:id',
          name: 'segments',
          component: () => import(/* webpackChunkName: "demo" */ './views/Segments.vue')
        },
        {
          path: '/logout',
          name: 'logout',

          component: () => import(/* webpackChunkName: "demo" */ './views/logout.vue')
        }
      ]

    },
    {
      path: '/',
      redirect: 'login',
      component: AuthLayout,
      meta: {
        requiresVisitor: true,
      },
      children: [
        {
          path: '/login',
          name: 'login',
          component: () => import(/* webpackChunkName: "demo" */ './views/Login.vue'),

        },
        {
          path: '/register',
          name: 'register',
          component: () => import(/* webpackChunkName: "demo" */ './views/Register.vue'),

        },

      ]

    }
  ]
})
