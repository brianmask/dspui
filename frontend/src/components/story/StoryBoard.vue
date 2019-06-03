<template>
  <span>
    <v-layout align-start justify-space-between fill-height row grow>
      <v-flex grow>
        <v-tabs
          v-model="active"
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
            :key="index"
          >
            <v-card flat grow>
              <v-card-text v-html="item.text"></v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs>  
      </v-flex>
      
    </v-layout>
  </span>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'StoryBoard',
    props: {
      id: undefined
    },
    data: () => {
        return {
          active: null
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
          return this.currentStory.story
        }
      }
    },
    watch: {
      id: function (newValue, oldValue) {
        if (newValue !== undefined) {
          this.active = null
          this.$store.dispatch('loadStory', { id: newValue })
        }
      }
    },
    beforeMount: function () {
      if (this.currentStory === undefined) {
        this.$store.dispatch('loadStory', { id: this.id })
      }
    }
  }
</script>