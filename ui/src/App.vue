<template>
  <div>
    <v-app>
      <Header />
      <v-main>
        <v-container>
          <router-view></router-view>
        </v-container>
      </v-main>
      <Footer />
    </v-app>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Header from "./components/layout/header/Header.vue";
import Footer from "./components/layout/footer/Footer.vue";

@Component({
  components: {
    Header,
    Footer,
  },
})
export default class App extends Vue {}
</script>
