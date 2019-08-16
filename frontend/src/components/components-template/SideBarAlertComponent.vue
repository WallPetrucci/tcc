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
              <v-divider class="separador-full" ></v-divider>
            </v-list-tile>
            
            <div class="info-usuario">
              <v-list-tile>
                <v-list-tile-content>
                  <v-list-tile-title class="nome-usuario">Wallace Petrucci Neves</v-list-tile-title>
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
                <v-divider class="separador"></v-divider>
              </v-list-tile>
            </div>

          </v-list>
        </v-flex>
      </v-layout>
    </template>
  </v-navigation-drawer>
</template>
<script type="text/javascript">
export default {
  name: "SideBarAlertComponent",
  data: () => ({
   
  }),
};
</script>