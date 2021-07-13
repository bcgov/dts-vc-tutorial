<template>
  <div>
    <v-row>
      <v-col cols="12">
        <div class="text-center">
          <h1>Improve The Privacy And Security Of Your Information</h1>
          <p>
            Learn about Verifiable Credentials: a secure, privacy-focused way to
            store and share your personal information using your smartphone.
          </p>
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-for="link in links" :key="link.path" cols="12" md="6">
        <v-card outlined class="mb-4">
          <v-card-title class="card-title">{{ link.title }}</v-card-title>
          <v-card-text class="card-content">{{ link.description }}</v-card-text>
          <v-card-actions>
            <v-btn
              :small="$vuetify.breakpoint.smAndDown"
              block
              class="text-capitalize"
              :to="link.path"
              >{{ link.enhancedLabel }}</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { EnhancedNavLink, links } from "../components/layout/header/Header.vue";

interface Data {
  links: EnhancedNavLink[];
}

@Component
export default class Home extends Vue {
  data(): Data {
    return {
      links: links,
    };
  }
}
</script>

<style lang="scss" scoped>
.card-title {
  word-break: break-word;
}
.card-content {
  min-height: 5rem;
}
</style>