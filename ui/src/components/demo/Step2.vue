<template>
  <div>
    <v-row>
      <v-col>
        <h1>Step 2: Scan the QR code</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h2>
          Scan the QR code, using the smartphone with your Verifiable
          Credentials on it.
        </h2>
        <p>1. Open your smartphone’s camera app.</p>
        <p>2. Point the camera at the QR code.</p>
        <p>
          3. A notification appears on your phone, asking if you’d like to open
          the QR code. Tap it.
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <p>Here’s how it looks.</p>
        TODO
      </v-col>
    </v-row>
    <v-row>
      <v-col> TODO </v-col>
    </v-row>
    <v-row v-if="$vuetify.breakpoint.lgAndUp && !mobileContext">
      <v-col>
        <DemoWalletQrCode />
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col>
        <DemoWalletButton />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <IconCard icon="mdi-autorenew">
          <p><strong>Waiting for your action</strong></p>
          <p>
            This page will automatically update when you’ve scanned and opened
            the QR code correctly.
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

declare global {
  interface Window {
    mobileContext: boolean;
  }
}

interface Data {
  mobileContext: boolean;
  links: NavLink[];
}

const helpLinks: NavLink[] = [
  {
    path: "",
    label: "I don’t have a Verifiable Credential yet.",
  },
  {
    path: "",
    label: "I accidentally dismissed the link to open the QR code.",
  },
  {
    path: "",
    label: "My camera app isn’t recognizing the QR code.",
  },
  {
    path: "",
    label: "I can’t scan the code because it’s on the screen on my smartphone.",
  },
  {
    path: "",
    label: "I have an impairment that prevents me scanning the QR code.",
  },
  {
    path: "",
    label: "This page isn’t updating, even though I scanned the QR code.",
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
      mobileContext: window?.mobileContext,
      links: helpLinks,
    };
  }
}
</script>