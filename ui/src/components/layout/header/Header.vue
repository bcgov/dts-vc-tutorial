<template>
  <div>
    <v-app-bar app color="primary" dark flat>
      <v-app-bar-title>Logo here</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" fixed temporary>
      <v-list nav>
        <v-list-item v-for="link in links" :key="link.path" :to="link.path">{{
          link.label
        }}</v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

interface NavLink {
  path: string;
  label: string;
}

interface Data {
  drawer: boolean;
  links: NavLink[];
}

export interface EnhancedNavLink extends NavLink {
  title: string;
  description: string;
  enhancedLabel: string;
}

export const links: EnhancedNavLink[] = [
  {
    path: "/what",
    label: "What are Verifiable Credentials?",
    enhancedLabel: "Discover what they are",
    title: "What are Verifiable Credentials?",
    description:
      "Your drivers license goes in your wallet, but your Verifiable Credential goes in your digital wallet. Discover what they are and what’s inside them.",
  },
  {
    path: "/why",
    label: "Why are Verifiable Credentials important?",
    enhancedLabel: "Learn about their importance",
    title: "Why Are Verifiable Credentials Important?",
    description:
      "You need to be confident in the security, integrity and confidentiality of your personal information.",
  },
  {
    path: "/get",
    label: "How to get a Verifiable Credential",
    enhancedLabel: "Get your first Verifiable Credentials",
    title: "How Do I Get Verifiable Credentials?",
    description:
      "Find out about digital wallets and how to get your first Verifiable Credentials.",
  },
  {
    path: "/demo",
    label: "Verification demo",
    enhancedLabel: "Try the interactive demo",
    title: "Show Me How They Work",
    description:
      "Learn how to use your Verifiable Credentials using this interactive demo.",
  },
];

@Component
export default class Header extends Vue {
  data(): Data {
    return {
      drawer: false,
      links,
    };
  }
}
</script>
