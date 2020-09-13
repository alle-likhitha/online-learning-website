<template>
  <div class="baseclass">
    <img class="imageCss" :src="imageLink" />
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: "BaseContainer",
  props: {
    msg: String,
    imageLink: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.baseclass {
  border-style: groove;
  width: 20rem;
  height: 20rem;
}
.imageCss {
  max-width: 100%;
  max-height: 100%;
  display: block;
}
</style>
