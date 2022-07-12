<template>
  <div>
    <v-row>
      <v-col>
        <h1 class="text-center">How do I get a Verifiable Credential?</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h2>
          First, get a digital wallet app, and then get your Verifiable
          Credentials.
        </h2>
        <v-row>
          <v-col>
            <h3>1. Download a digital wallet app</h3>
            <p>
              A digital wallet app receives, stores and presents your Verifiable
              Credentials.
            </p>
            <p>
              There are many digital wallet apps on the App Store for iOS, and
              the Google Play store for Android.
            </p>
            <p>Options include:</p>
            <ul>
              <li><a href="">Trinsic wallet (iOS / Android)</a></li>
              <li><a href="">Lissi wallet (iOS / Android)</a></li>
              <li><a href="">esatus wallet (iOS / Android)</a></li>
            </ul>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <h3>2. Get a Verifiable Credential issued to your wallet</h3>
            <p>Get a {{ "TODO" }} Verifiable Credential from {{ "TODO" }}.</p>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <ContentNextSteps />
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import ContentNextSteps from "./NextSteps.vue";

@Component({
  components: {
    ContentNextSteps,
  },
})
export default class ContentGet extends Vue {}
</script>
