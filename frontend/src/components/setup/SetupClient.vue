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
              <v-card-text>{{ item.content }}</v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs>  
      </v-flex>
      
    </v-layout>
  </span>
</template>

<script>
  export default {
      name: 'SetupClient',
      data: () => {
          return {
            active: null,
            TableOfContents: [
              {
                name: 'loading',
                content: 'loading content... please wait....'
              }
            ]
          }
      }
  }
</script>