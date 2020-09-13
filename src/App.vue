<template>
  <v-app>
    <v-app-bar app dark>
    <v-toolbar-title class="headline text-uppercase">
        <router-link
        to='/'
        tag='span'
        style='cursor: pointer'>
        Geometry
        </router-link>
      </v-toolbar-title> 
       <v-spacer></v-spacer>
       <v-flex xs12 sm6 md3>
        <v-text-field label='Shape' v-model='searchString'> </v-text-field>
        </v-flex>
    </v-app-bar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    searchString:''
  }),
  methods: {
    searchGeometry () {
      this.$router.push('/search/' + this.searchString)
      this.searchString = ''
    }
  },
  computed: {
    dataAvailable () {
      return this.searchString !== null && this.searchString !== ''
    }
  }
};
</script>
