<style scoped src="@/assets/SideBarAlertComponent.css"></style>

<template>
  <v-navigation-drawer fixed right app>
    <template>
      <v-layout row>
        <v-flex xs12 s12>
          <v-list two-line>
            <v-list-tile>
              <v-list-tile-action>
                <v-icon class="alert-icon">fas fa-exclamation-circle</v-icon>
              </v-list-tile-action>

              <v-list-tile-content>
                <v-toolbar-title class="alert-title">Alertas</v-toolbar-title>
              </v-list-tile-content>
            </v-list-tile>
            
            <div class="info-usuario" v-for="alerts in dataAlerts">
              <v-divider class="separador-full"></v-divider>
              <v-list-item>
                <v-list-tile-content class="user-data">
                  <v-list-tile-title class="user-name">Wallace Petrucci Neves</v-list-tile-title>
                  <v-list-tile-sub-title>Data: {{convertToDate(alerts.alert_date)}}</v-list-tile-sub-title>
                  <v-list-tile-sub-title class="date-hour">Horas: {{convertToHour(alerts.alert_date)}}</v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-item>
              
              <v-list-item class="user-data">
                <v-list-tile-content >
                  <v-list-tile-sub-title>Problema</v-list-tile-sub-title>
                  <v-list-tile-sub-title class="cause">{{alerts.messages}} </v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-item>
              <v-list-item class="user-data">
                <v-list-tile-content>
                  <v-list-tile-sub-title>FC: {{alerts.heart}} bpm</v-list-tile-sub-title>
                  <v-list-tile-sub-title>Oxi: {{alerts.oximetry}} saO2</v-list-tile-sub-title>
                  <v-list-tile-sub-title>TC: {{alerts.temperature}} °C</v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-item>
            </div>

          </v-list>
        </v-flex>
      </v-layout>
    </template>
  </v-navigation-drawer>
</template>
<script type="text/javascript">
import axios from 'axios';
export default {
  name: "SideBarAlertComponent",
  data: () => ({
    dataAlerts: []
  }),
  mounted(){
    this.getAlert()
  },
  methods:{
    getAlert(){
      axios.get("http://localhost:5000/api/alerts/"+this.$session.get('id_user'))
      .then((response) => {
        console.log(response)
        this.dataAlerts = response.data
      })
      .catch(()=> {
        this.progressLinear = false
        this.error_message = "Email ou Senha inválido."
      })
    },
    convertToHour(date){
      const hour = new Date(date).getHours()
      const minute = new Date(date).getMinutes()

      const geralHour = hour +":"+ minute
      return geralHour
    },
    convertToDate(date){
      const day = new Date(date).getDay()
      const month = new Date(date).getMonth()
      const year = new Date(date).getYear()

      const geralDate = day +"/"+ month+"/"+year
      return geralDate
    }
  }
};
</script>