<template>
  <v-card class="mb-4" elevation="0" color="grey lighten-1">
    <v-row class="ma-0 pa-0">
      <v-col class="ma-0 pa-0 flex-grow-0 flex-shrink-1">
        <v-avatar class="ml-2 mt-2">
          <v-icon>{{ icon }}</v-icon>
        </v-avatar>
      </v-col>
      <v-col class="ma-0 pa-0 flex-grow-1 flex-shrink-0">
        <v-card-text class="ml-0 pl-0">
          <slot></slot>
        </v-card-text>
      </v-col>
    </v-row>
  </v-card>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class IconCard extends Vue {
  @Prop({ default: "" }) icon!: string;
}
</script>
