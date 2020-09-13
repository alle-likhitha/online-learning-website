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
      <v-row no-gutters>
          <v-col>
      <v-flex xs11 mr-1 ml-1 :key="shapeDetailsLocal.name">
        <v-card>
        <v-img :src="shapeDetailsLocal.baseImage" aspect-ratio="1"></v-img>
        </v-card>
      </v-flex>
      </v-col>
      <v-col>
      <v-flex xs10 mr-1  :key="shapeDetailsLocal.name">
        <v-card>
          <v-card-title primary-title>
            <div>
              <h2 class="headline mb-0">{{shapeDetailsLocal.name}}</h2>
              <p>{{shapeDetailsLocal.description}} </p>
            </div>
          </v-card-title>
        </v-card>
      </v-flex>


      <v-row>
        <v-col v-for="variableName in variableForShape" :key="variableName.name">
        <v-flex xs6 :key="variableName.name">
          <v-card>
            <v-card-title primary-title>
              <div>
                <label>{{variableName.name}} : </label>
                <input v-model.number="variableName.value" v-on:change="variableChanged" type="number" >    
              </div>
            </v-card-title>
          </v-card>
        </v-flex>
        </v-col>
      </v-row>
      
      <v-row   v-for="formula in formulas" :key="formula.name">
        <v-flex xs8 mr-1  :key="formula.name">
          <v-card>
            <v-card-title primary-title>
              <div>
                <p :id="formula.name" >$${{formula.name}} = {{formula.expression}} $$</p><p> = {{formula.computedValue}} </p>
              </div>
            </v-card-title>
          </v-card>
        </v-flex>
      </v-row>
      
      
      
      </v-col>
      
      </v-row>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
import Vue from "vue";
import MathLive from "mathlive";
// import math from "mathjs";
import "mathlive/dist/mathlive.core.css";
import "mathlive/dist/mathlive.css";
/* eslint-disable */
export default {
 name:"shape",
 data () {
    return {
      shapeDetailsLocal:'',
      formulas:[],
      variableForShape:[],
      x:12,
      loading: true
    }
  },
    created() {
        this.shapePassed = this.$route.query.shape;
    },
    mounted () {  
        axios.get("http://localhost:9000/get-shape-defination?shape=" + this.shapePassed)
        .then(response => {
            this.shapeDetailsLocal = response.data
            this.formulas= response.data.formulas
            this.variableForShape = response.data.variable
            this.loading = false
            this.renderMath()
        })
  },
  
  methods: {
    renderMath() {
      this.$nextTick(() => {
          for (var x in this.formulas){
            MathLive.makeMathField(this.formulas[x].name);
          }
      });
    },
    getRequiredGeonetricalMeasures(datum){
        axios.get("http://localhost:9000/get-shape-geometry?"+datum).then(response => {
            var formulasGiven = this.formulas
            for (var f in formulasGiven){
              formulasGiven[f]["computedValue"] = response.data[formulasGiven[f]["name"]] 
              Vue.set(this.formulas, f , formulasGiven[f])  
            }
            console.log(this.formulas)
            // this.formulas = formulasGiven
        })
    },variableChanged(event){
      var dataHolder = []
      for (var x in this.variableForShape){
        dataHolder.push(encodeURIComponent(this.variableForShape[x]["name"]) + '=' + encodeURIComponent(this.variableForShape[x]["value"]));
      }
      dataHolder.push("shape=" + encodeURIComponent(this.shapePassed))
      this.getRequiredGeonetricalMeasures(dataHolder.join('&'))  
    } 
  }
}
</script>