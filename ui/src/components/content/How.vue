<template>
  <div>
    <v-row>
      <v-col>
        <h1 class="text-center">How do Verifiable Credentials work?</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h2>
          The way you get, store and use Verifiable Credentials is similar to
          physical credentials.
        </h2>
        <p>Your Verifiable Credentials are stored on your smartphone.</p>
        <p>
          They get given—“issued”—to you by someone like a government department
          or an organization.
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card color="grey lighten-2" elevation="0">
          <v-card-title>Example</v-card-title>
          <v-card-text>
            You might want to be issued with a driving license Verifiable
            Credential, from the government department responsible for driving
            licenses.</v-card-text
          >
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <p>
          You store them—“hold” them—in a digital wallet app that you install on
          your smartphone.
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card color="grey lighten-2" elevation="0">
          <v-card-title>Example</v-card-title>

          <v-card-text>
            You might install the <a href="">Lissi wallet app</a> on your
            iPhone, and use it to receive and store the driving license
            Verifiable Credential.</v-card-text
          >
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <p>
          Then, you use your Verifiable Credentials by “presenting” them to a
          verifier.
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card color="grey lighten-2" elevation="0">
          <v-card-title>Example</v-card-title>
          <v-card-text>
            You might present your driving license Verifiable Credential to a
            rental agency, in order to rent a car.</v-card-text
          >
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <p>
          Issuing and presenting your Verifiable Credentials usually happens
          wirelessly and over the Internet. You never have to physically show
          your digital wallet app to anyone, nor give them your phone.
        </p>
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
export default class ContentHow extends Vue {}
</script>
