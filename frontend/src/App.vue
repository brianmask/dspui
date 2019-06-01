<template>
  <v-app id="inspire" dark>
    <main-nav></main-nav>
    <v-content>
      <v-container>        
          <router-view></router-view>
      </v-container>
    </v-content>
    <v-footer app fixed>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
  import MainNav from '@/components/nav/MainNav'

  export default {
    components: {
      MainNav
    },
    props: {
      source: String
    },
    methods: {

    }
  }
</script>

