<style scoped src="@/assets/HeaderComponent.css"></style>

<template>
  <div v-if="this.show">
    <SideBarAlertComponent></SideBarAlertComponent>
    <v-toolbar color="header-content" dark fixed app>
      <div>
        <strong>Seja bem vindo, {{nameUser}}</strong>
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
        </ul>
      </nav>
      <v-spacer></v-spacer>

      <ModalComponent icone='fas fa-user-cog' title='Editar Meus Dados' :showTitle=falses>     
        <EditDataComponent />
      </ModalComponent>
      <ModalComponent icone='fas fa-sliders-h' title='Configurar WHM' v-on:getSettingsMethod="getUserSettings" :getSettings="true">     
        <SettingsComponent />
      </ModalComponent>
      <template>
        <div>
          <v-icon @click="logOut">fas fa-sign-out-alt</v-icon>         
        </div>
      </template>

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
i.v-icon.v-icon--link.fas.fa-user-cog.theme--dark, i.v-icon.v-icon--link.fas.fa-sliders-h.theme--dark {
  margin-right: 15px;
}

.navigation-header ul li a:hover, i.v-icon.v-icon--link:hover, i.v-icon.fa-sign-out-alt:hover{
  color: #03504c;
}

i.v-icon.fa-sign-out-alt{
  cursor: pointer;
}

</style>
<script type="text/javascript">
import SideBarAlertComponent from "./SideBarAlertComponent";
import ModalComponent from "./ModalComponent";
import SettingsComponent from "./SettingsComponent";
import EditDataComponent from "./EditDataComponent";
import {APP_ROUTERS} from "../constants.js";
import axios from 'axios';
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
  mounted(){
    this.nameUser = this.$session.get('name')
    this.user_id = this.$session.get('id_user')
  },
  data (){
    return{
      show: false,
      nameUser: '',
      userSettings: {},
      user_id: ''
    }
  },
  methods: {
    logOut()  {
      var dataLogOut = {
        user_name: this.$session.get('name'),
        user_email: this.$session.get('email')  
      }
      axios.put("http://localhost:5000/api/login/", dataLogOut)
      .then((response) => {
        this.progressLinear = false
        if(!response.data.is_loggedin){
          this.$session.destroy()
          this.$router.push(APP_ROUTERS.login)         
        }
      })
      .catch(()=> {
        this.progressLinear = false
        this.error_message = "Email ou Senha inválido."
      })     
    },
    

  }
};
</script>