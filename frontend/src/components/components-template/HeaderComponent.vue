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
            <router-link to="/monitor"> <v-icon>fas fa-users</v-icon> Monitores</router-link>
          </li>
          <li>            
            <router-link to="/monitoring"> <v-icon>fas fa-eye</v-icon> Monitorar</router-link>
          </li>
          <li>            
            <router-link to="/reports"> <v-icon>fas fa-chart-area </v-icon> Relatórios</router-link>
          </li>
          <li>
            <ModalComponent icone='fas fa-edit' title='Editar Meus Dados' v-bind:showTitle=true>     
              <EditDataComponent />
            </ModalComponent>
          </li>
        </ul>
      </nav>
      <v-spacer></v-spacer>

      <ModalComponent icone='fas fa-sliders-h' title='Configurar WHM'>     
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
import EditDataComponent from "./EditDataComponent";
export default {
  name: "HeaderComponent",
  components: {
    SideBarAlertComponent,
    ModalComponent,
    SettingsComponent,
    EditDataComponent
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