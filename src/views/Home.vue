
<template>
  <v-container v-if="loading">
    <div class="text-xs-center">
      <v-progress-circular
        indeterminate
        :size="150"
        :width="8"
        color="green">
      </v-progress-circular>
    </div>
  </v-container>
  <v-container v-else grid-list-xl>
    <v-layout wrap>
      <v-flex xs3 v-for="shapeInfo in geometryData" :key="shapeInfo.id" mb-1>
        <v-card>
          <v-img  aspect-ratio="1" :src="shapeInfo.baseImage"></v-img>
          <v-card-title primary-title>
            <div>
              <h2>{{shapeInfo.name}}</h2>
             </div>
          </v-card-title>
          <v-card-actions class="justify-center">
            <v-btn  color="green" @click="shapeDetails(shapeInfo.id)">View</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
  </v-layout>
  </v-container>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
/* eslint-disable */
export default {
  name: "home",
  data() {
    return {
      geometryData: null,
      loading: true
    };
  },
  mounted() {
    axios.get("http://localhost:9000/get-shapes").then(response => {
      // debugger
      this.geometryData = response.data;
      this.loading = false;
    });
  },
  methods:{
     shapeDetails (nameLocal) {
      this.$router.push('/shape?shape=' + nameLocal)
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.home {
  margin: auto;
  width: 50%;
  /* border: 3px solid #73AD21; */
  padding: 10px;
}

.home div {
  float: left;
  margin: 0.2rem;
}
</style>
