import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import 'vuetify/src/stylus/app.styl'

Vue.use(Vuetify, {
  iconfont: 'md',
  theme: {
    primary: '#607d8b',
    secondary: '#009688',
    accent: '#4caf50',
    error: '#f44336',
    warning: '#ff9800',
    info: '#00bcd4',
    success: '#3f51b5'
  }
})
