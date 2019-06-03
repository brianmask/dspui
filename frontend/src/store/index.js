import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

/* API Calls */
import { getStoryTopics, getStoryBoard } from '@/api'

export default new Vuex.Store({
    state: {
        stories: undefined,
        currentStory: undefined
    },
    actions: {
        loadStories (context) {
            getStoryTopics()
              .then((response) => {
                  context.commit('setStories', { data: response.data })
              })
        },
        loadStory (context, payload) {
            getStoryBoard(payload.id)
              .then((response) => {
                  context.commit('setCurrentStory', { data: response.data })
              })
        }
    },
    mutations: {
        setStories (state, payload) {
            state.stories = payload.data
        },
        setCurrentStory (state, payload) {
            state.currentStory = payload.data
        }
    }
})