import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "about",
    component: Home
  },
  {
    path: "/shape",
    name: "shape",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Shape.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
