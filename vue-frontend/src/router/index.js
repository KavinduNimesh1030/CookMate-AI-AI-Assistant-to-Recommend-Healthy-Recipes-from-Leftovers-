import { createRouter, createWebHistory } from "vue-router";
import Home from "../pages/Home.vue";
import Recipe from "../pages/Recipe.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/recipe/:id", component: Recipe, props: true },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
