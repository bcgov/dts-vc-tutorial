<template>
  <div>
    <v-row>
      <v-col>
        <h1>Try a live demonstration</h1>
        <p>
          This interactive demo shows you how to present your Verifiable
          Credentials for verification.
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" md="6">
        <IconCard icon="mdi-message-alert">
          <p>
            You’ll need a {{ "TODO" }} Verifiable Credential on your smartphone
            for this demo.
          </p>
          <p>
            Don’t have a {{ "TODO" }} Verifiable Credential yet? Find out
            <router-link to=""
              >how to get your Verifiable Credentials</router-link
            >.
          </p>
          <p>
            Alternatively, just get an overview of
            <router-link to="/demo/overview">how verification works</router-link
            >.
          </p>
        </IconCard>
      </v-col>
      <v-col cols="12" md="6">
        <v-card class="mb-4" elevation="0">
          <v-card-title>Data privacy</v-card-title>
          <v-card-text
            >In this demo, only {{ "TODO" }} will be requested from your
            Verifiable Credential. This website does not store your information,
            and no one will be notified that you completed this demo. (See our
            <router-link to="">privacy policy</router-link> for more
            information.)</v-card-text
          >
          <v-card-actions class="justify-center">
            <v-btn class="text-capitalize" to="/demo/step/pre"
              >Start the demo</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import IconCard from "../shared/IconCard.vue";

@Component({
  components: {
    IconCard,
  },
})
export default class DemoHome extends Vue {}
</script>
