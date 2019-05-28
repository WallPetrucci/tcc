<style scoped src="@/assets/HeaderComponent.css"></style>

<template>
    <v-toolbar app class="header-content">
      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">MATERIAL DESIGN</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
      flat
      href="https://github.com/vuetifyjs/vuetify/releases/latest"
      target="_blank"
      >
      <span class="mr-2">Latest Release</span>
    </v-btn>
  </v-toolbar>
</template>

<script type="text/javascript">
  export default {
    name: 'HeaderComponent',
    data(){
      return {}
    }
  }
</script>