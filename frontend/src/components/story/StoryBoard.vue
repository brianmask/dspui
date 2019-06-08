<template>
  <v-layout>
    <v-flex>
      <v-tabs
        v-model="active"
        grow
      >
        <v-tab 
          v-for="(item, index) in TableOfContents"
          :key="index"
          ripple
          grow
        >
        {{ item.name }}
        </v-tab>
        <v-tab-item
          v-for="(item, index) in TableOfContents"
          :key="item.text"
        >
          <v-card>
            <v-card-text><vue-markdown>{{ item.text }}</vue-markdown></v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>  
    </v-flex>
  </v-layout>
</template>

<script>
  import { mapState } from 'vuex'
  import VueMarkdown from 'vue-markdown' 

  export default {
    name: 'StoryBoard',
    props: {
      id: undefined
    },
    components: {
      VueMarkdown
    },
    data: () => {
        return {
          active: 0
        }
    },
    computed: {
      ...mapState ({
        currentStory: 'currentStory'
      }),
      TableOfContents: function () {
        if (this.currentStory === undefined) {
          return [{
            name: 'loading',
            text: 'loading content... please wait....'
          }]
        } else {
          return this.currentStory.menu
        }
      }
    },
    watch: {
      id: function (newValue) {
        if (newValue !== undefined) {
          this.active = 0
          this.$store.dispatch('loadStory', { id: newValue })
        }
      }
    },
    beforeMount: function () {
      if (this.currentStory === undefined || this.id !== this.currentStory.id) {
        this.$store.dispatch('loadStory', { id: this.id })
      }
    }
  }
</script>