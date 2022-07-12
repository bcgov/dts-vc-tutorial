<template>
  <div>
    <v-row>
      <v-col>
        <h1>Step 3: Confirm what to share</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h2>Use your digital wallet app to confirm what you’ll share.</h2>
        <p>Scanning the QR code will have opened your digital wallet app.</p>
        <p>
          The digital wallet matched your Verifiable Credentials to what’s being
          requested.
        </p>
        <p>
          It is now asking you to confirm what to share. You can confirm or
          decline. If you decline, nothing will be shared. The verifier will be
          notified either way.
        </p>
        <p>
          <strong
            >Use your digital wallet app to confirm the sharing of
            {{ "TODO" }}.</strong
          >
        </p>
        <p>Switch back to this web browser afterwards.</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col> TODO </v-col>
    </v-row>
    <v-row>
      <v-col>
        <IconCard icon="mdi-autorenew">
          <p><strong>Waiting for your action</strong></p>
          <p>
            This page will automatically update when you’ve confirmed what to
            share in your digital wallet app.
          </p>
        </IconCard>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <Troubleshoot>
          <ul>
            <li v-for="link in links" :key="link.label">
              <router-link :to="link.path">{{ link.label }} </router-link>
            </li>
          </ul>
        </Troubleshoot>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import DemoWalletQrCode from "./WalletQrCode.vue";
import DemoWalletButton from "./WalletButton.vue";
import IconCard from "../shared/IconCard.vue";
import Troubleshoot from "./Troubleshoot.vue";
import { NavLink } from "../layout/header/Header.vue";

interface Data {
  links: NavLink[];
}

const helpLinks: NavLink[] = [
  {
    path: "",
    label: "The digital wallet app didn’t open automatically.",
  },
  {
    path: "",
    label:
      "The digital wallet app says I don’t have the information being requested.",
  },
  {
    path: "",
    label: "The digital wallet isn’t asking me anything.",
  },
  {
    path: "",
    label: "I need to scan the QR code again.",
  },
  {
    path: "",
    label: "I don’t have a digital wallet app yet.",
  },
  {
    path: "",
    label: "This page isn’t updating, even though I confirmed what to share.",
  },
  {
    path: "",
    label: "Something else isn’t working.",
  },
];

@Component({
  components: {
    DemoWalletQrCode,
    DemoWalletButton,
    IconCard,
    Troubleshoot,
  },
})
export default class DemoStep2 extends Vue {
  data(): Data {
    return {
      links: helpLinks,
    };
  }
}
</script>