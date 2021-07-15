<template>
  <v-card color="grey lighten-2" elevation="0">
    <v-card-title>Next Steps</v-card-title>
    <v-card-text>
      <ul>
        <li v-for="link in links" :key="link.path">
          <router-link :to="link.path">{{ link.label }} </router-link>
        </li>
      </ul>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { EnhancedNavLink, links } from "../layout/header/Header.vue";

interface Data {
  links: EnhancedNavLink[];
}

@Component
export default class ContentNextSteps extends Vue {
  data(): Data {
    return {
      links,
    };
  }
}
</script>
