<style scoped src="@/assets/HeaderComponent.css"></style>

<template>
  <div v-if="this.show">
    <SideBarAlertComponent></SideBarAlertComponent>
    <v-toolbar color="header-content" dark fixed app>
      <div>
        <strong>Seja bem vindo, Wallace Petrucci Neves</strong>
      </div>
      <nav class="navigation-header">
        <ul>
          <li>            
            <router-link to="/panel"> <v-icon>fas fa-home</v-icon> Painel</router-link>
          </li>
          <li>            
            <router-link to="/monitoring"> <v-icon>fas fa-eye</v-icon> Monitorar Usuário</router-link>
          </li>
          <li>            
            <router-link to="/reports"> <v-icon>fas fa-chart-area </v-icon> Relatórios</router-link>
          </li>
        </ul>
      </nav>
      <v-spacer></v-spacer>

      <ModalComponent>
        <v-toolbar-title v-on="on" v-slot:header>
          <v-icon>fas fa-chart-area </v-icon>
          <span class="">Configurações</span>
        </v-toolbar-title>
        <SettingsComponent />
      </ModalComponent>
    </v-toolbar>
  </div>
</template>

<style type="text/css">
.navigation-header ul li a{
  color: white;
  text-decoration: none;
  font-weight: 600;
  letter-spacing: 1.3px;
}
.navigation-header ul li{
  list-style: none;
  float: left;
  padding: 10px;
}

</style>
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
  beforeMount(){
    if (this.$session.exists()) {
      this.show = true
    } 
  },
  data (){
    return{
      show: false,
    }
  }
};
</script>