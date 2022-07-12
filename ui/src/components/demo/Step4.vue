<template>
  <div>
    <v-row>
      <v-col>
        <h1>Step 4: Verification Confirmed</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h2>Congratulations! You successfully used your Verifiable Credential.</h2>
        <p>Your {{ "TODO " }} was received from your Verifiable Credential.</p>
        <p>
          Nothing else was shared from your Verifiable Credential. Verifiers
          should only ask for what they need.
        </p>
        <p>
          The issuer of your Verifiable Credential was not notified that you
          used it in this demo. Verification can happen without it.
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <NextSteps />
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import IconCard from "../shared/IconCard.vue";
import NextSteps from "../content/NextSteps.vue";
import { NavLink } from "../layout/header/Header.vue";

interface Data {
  links: NavLink[];
}

@Component({
  components: {
    IconCard,
    NextSteps,
  },
})
export default class DemoStep4 extends Vue {
  data(): Data {
    return {
      links: [],
    };
  }
}
</script>