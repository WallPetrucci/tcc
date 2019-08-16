<template>
  <v-navigation-drawer fixed right app>
    <template>
      <v-layout row>
        <v-flex xs12 s12>
          <v-card>

            <v-list three-line>
              <v-list-tile>
                <v-list-tile-action>
                  <v-icon color="indigo">fas fa-exclamation-circle</v-icon>
                </v-list-tile-action>

                <v-list-tile-content>
                 <v-toolbar-title>Alertas</v-toolbar-title>
                </v-list-tile-content>
              </v-list-tile>
              <v-divider ></v-divider>

              <v-list-tile>
                <v-list-tile-action>

                  <v-list-tile-title>(323) 555-6789</v-list-tile-title>
                  <v-list-tile-content>Work</v-list-tile-content>

                </v-list-tile-action>
              </v-list-tile>

              <v-divider inset></v-divider>
            </v-list>
          </v-card>
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