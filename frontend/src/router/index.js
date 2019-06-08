import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import WelcomeImage from '@/components/nav/WelcomeImage'
import StoryBoard from '@/components/story/StoryBoard'
import LoginForm from '@/components/user/LoginForm'
import HelloWorld from '@/components/HelloWorld'

export default new Router({
  routes: [
    {
      path: '/',
      component: WelcomeImage
    },
    {
      path: '/setup/:id/',
      name: 'setup',
      component: StoryBoard,
      props: true
    },
    {
      path: '/login/',
      name: 'login',
      component: LoginForm
    },
    {
      path: '/test/',
      component: HelloWorld
    }
  ]
})
