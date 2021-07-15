<template>
  <div>
    <v-row>
      <v-col>
        <h1>Step 1: Get shown a QR code</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h2>You start by being shown a QR code.</h2>
        <p>
          It basically says, “please provide me with information to verify.”
        </p>
        <p>{{ "TODO" }}</p>
        <p>
          <em>Important:</em> you never need to show someone your digital wallet
          app, or give them your phone, to use your Verifiable Credentials.
        </p>
        <p>
          <strong
            >There is nothing to do on this step. We will show you a QR code in
            Step 2.</strong
          >
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn link class="text-capitalize" to="/demo/step/2">
          <v-icon>mdi-chevron-right-circle</v-icon>
          <span>Go to Step 2</span>
        </v-btn>
      </v-col>
    </v-row>
  </div>
</template>