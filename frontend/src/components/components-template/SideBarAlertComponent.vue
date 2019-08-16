<template>
  <v-navigation-drawer fixed right app>
    <template>
      <v-layout row>
        <v-flex xs12 s12>
          <v-list two-line>
            <v-list-tile>
              <v-list-tile-action>
                <v-icon>fas fa-exclamation-circle</v-icon>
              </v-list-tile-action>

              <v-list-tile-content>
                <v-toolbar-title class="alert-title">Alertas</v-toolbar-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-divider class="separador-full" ></v-divider>

            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title>Wallace Petrucci Neves</v-list-tile-title>
                <v-list-tile-sub-title>Data: 14/08/2019</v-list-tile-sub-title>
                <v-list-tile-sub-title>Horas: 00:00</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
              
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-sub-title>Problema</v-list-tile-sub-title>
                <v-list-tile-sub-title>Frequência Cardíaca Muito alta</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-sub-title>FC: 130bpm</v-list-tile-sub-title>
                <v-list-tile-sub-title>Oxi: 100saO2</v-list-tile-sub-title>
                <v-list-tile-sub-title>TC: 40°C</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>

            <v-divider class="separador"></v-divider>
          </v-list>
        </v-flex>
      </v-layout>
    </template>
  </v-navigation-drawer>
</template>
<style>
  .v-toolbar__title.alert-title{
    font-size:1.5em;
  }
  .separador-full.v-divider.theme--light{
    border: 1.2px solid;
    border-color:black;
    width: 15.5em;
  }
</style>
<script type="text/javascript">
export default {
  name: "SideBarAlertComponent",
  data: () => ({
   
  }),
};
</script>