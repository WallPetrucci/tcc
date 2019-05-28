<style scoped src="@/assets/HeaderComponent.css"></style>

<template>
  <div>
    <SideBarAlertComponent> </SideBarAlertComponent>
    <v-toolbar color="header-content" dark fixed app>
      <v-spacer></v-spacer>
      <v-toolbar-title>Configuração</v-toolbar-title>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
    </v-toolbar>
  </div>
</template>

<script type="text/javascript">
  import SideBarAlertComponent from './SideBarAlertComponent'
  export default {
    name: 'HeaderComponent',
    components: {
      SideBarAlertComponent,
    },
    data(){
      return {}
    },
    props:{
      drawer: Boolean
    }
  }
</script>