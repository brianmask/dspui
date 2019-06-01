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
        <v-list-tile @click="openSetup()">
          <v-list-tile-action>
            <v-icon>settings</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Client Setup</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>   
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app fixed clipped-left>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Ranik's Realm - FFXI</v-toolbar-title>
    </v-toolbar>
  </span>
</template>

<script>
  export default {
    data: () => ({
      drawer: null
    }),
    props: {
      source: String
    },
    methods: {
      openHome () {
        this.$router.push('/')
      },
      openSetup () {
        this.$router.push({ name: 'setup' })
      }
    }
  }
</script>


