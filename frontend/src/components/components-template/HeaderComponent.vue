<style scoped src="@/assets/HeaderComponent.css"></style>

<template>
  <div>
    <SideBarAlertComponent></SideBarAlertComponent>
    <v-toolbar color="header-content" dark fixed app>
      <nav>
        <router-link to="/panel">Painel</router-link>
        <router-link to="/monitoring">Monitorar Usuário</router-link>
        <router-link to="/login">Relatórios</router-link>
      </nav>
      <v-spacer></v-spacer>

      <ModalComponent>
        <SettingsComponent />
      </ModalComponent>
    </v-toolbar>
  </div>
</template>

<script type="text/javascript">
import SideBarAlertComponent from "./SideBarAlertComponent";
import ModalComponent from "./ModalComponent";
import SettingsComponent from "./SettingsComponent";
export default {
  name: "HeaderComponent",
  components: {
    SideBarAlertComponent,
    ModalComponent,
    SettingsComponent
  },
  data (){
    return{}
  }
};
</script>