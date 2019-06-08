<template>
  <span>
    <v-navigation-drawer
      v-model="drawer"
      clipped
      fixed
      app
    >
      <v-list dense>   
        <v-list-tile @click="openHome()">
          <v-list-tile-action>
            <v-icon>dashboard</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <div v-if="navItems !== undefined">
        <template v-for="(item, index) in navItems">
          <v-list-tile @click="openStory(item.id)" :key="index">
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ item.name }}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>         
        </template> 
        </div>        
      </v-list>  
    </v-navigation-drawer>
    <v-toolbar app fixed clipped-left>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Ranik's Realm - FFXI</v-toolbar-title>
    </v-toolbar>
  </span>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    data: () => ({
      drawer: null
    }),
    computed: {
      ...mapState ({
        navItems: 'stories'
      })
    },
    methods: {
      openHome () {
        this.$router.push('/')
      },
      openStory (id) {
        this.$router.push({ name: 'setup', params: { id: id } })
      }
    },
    beforeMount: function () {
      if (this.navItems === undefined) {
        this.$store.dispatch('loadStories')
      }
    }
  }
</script>


