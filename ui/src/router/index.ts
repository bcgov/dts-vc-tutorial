import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Home from "../views/Home.vue";
import ContentHow from "../components/content/How.vue";
import ContentWhat from "../components/content/What.vue";
import ContentWhy from "../components/content/Why.vue";
import ContentGet from "../components/content/Get.vue";
import DemoHome from "../components/demo/Home.vue";
import DemoOverview from "../components/demo/Overview.vue";
import DemoPreCheck from "../components/demo/PreCheck.vue";
import DemoPreCheckYes from "../components/demo/PreCheckYes.vue";
import DemoPreCheckNo from "../components/demo/PreCheckNo.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/why",
    component: ContentWhy,
  },
  {
    path: "/what",
    component: ContentWhat,
  },
  {
    path: "/how",
    component: ContentHow,
  },
  {
    path: "/get",
    component: ContentGet,
  },
  {
    path: "/demo",
    component: () => import(/* webpackChunkName: "demo" */ "../views/Demo.vue"),
    children: [
      { path: "", component: DemoHome },
      { path: "overview", component: DemoOverview },
      {
        path: "step/pre",
        component: DemoPreCheck,
        children: [
          { path: "yes", component: DemoPreCheckYes },
          { path: "no", component: DemoPreCheckNo },
        ],
      },
      { path: "step/1", component: undefined },
      { path: "step/2", component: undefined },
      { path: "step/3", component: undefined },
      { path: "step/4", component: undefined },
    ],
  },
];

const router = new VueRouter({
  mode: "hash",
  base: process.env.BASE_URL,
  routes,
});

export default router;
