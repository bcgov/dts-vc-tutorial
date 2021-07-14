<template>
  <div>
    <v-row>
      <v-col>
        <h1>Before We Start</h1>
        <p>
          Are you looking at this website on the smartphone that has your
          Verifiable Credentials?
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn class="mr-4" to="/demo/step/pre/yes">Yes</v-btn>
        <v-btn class="mr-4" to="/demo/step/pre/no">No</v-btn>
      </v-col>
    </v-row>
    <router-view></router-view>
  </div>
</template>
