<template>
  <div>
    <v-row>
      <v-col cols="12">
        <h1>How to use your Verifiable Credentials</h1>
        <p>
          Using your Verifiable Credentials is a simple four-step process with
          your smartphone’s camera and a digital wallet app.
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <IconCard icon="mdi-help-circle">
          <p>
            Already have a Verifiable Credential on your phone?
            <router-link to="/demo">Try out the live demo</router-link>.
          </p>
        </IconCard>
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
import IconCard from "../shared/IconCard.vue";
import ContentNextSteps from "../content/NextSteps.vue";

@Component({
  components: {
    IconCard,
    ContentNextSteps,
  },
})
export default class DemoOverview extends Vue {}
</script>
