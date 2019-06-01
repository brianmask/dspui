import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import WelcomeImage from '@/components/nav/WelcomeImage'
import SetupClient from '@/components/setup/SetupClient'

export default new Router({
  routes: [
    {
      path: '/',
      component: WelcomeImage
    },
    {
      path: '/setup',
      name: 'setup',
      component: SetupClient
    }
  ]
})
