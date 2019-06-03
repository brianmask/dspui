import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import WelcomeImage from '@/components/nav/WelcomeImage'
import StoryBoard from '@/components/story/StoryBoard'

export default new Router({
  routes: [
    {
      path: '/',
      component: WelcomeImage
    },
    {
      path: '/story/:id/',
      name: 'story',
      component: StoryBoard,
      props: true
    }
  ]
})
