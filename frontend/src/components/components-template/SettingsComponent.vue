<template>
  <v-card class="elevation-12">
    <v-toolbar dark color="primary">
      <v-toolbar-title>{{title}}</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <template>
      <v-window>
        <v-window-item>
          <v-card-text>
            <v-text-field label="Código do Dispositivo" required></v-text-field>
            <v-spacer></v-spacer>
            <SliderComponent title="Frequência Cardíaca"  v-bind:minMaxRange="[0,160]"/>
            <SliderComponent title="Oximetria"  v-bind:minMaxRange="[0,100]"/>
            <SliderComponent title="TemperaturaCorporal"  v-bind:minMaxRange="[20, 40]"/>
          </v-card-text>
        </v-window-item>
      </v-window>

      <v-divider></v-divider>

      <v-card-actions >
        <v-spacer></v-spacer>
        <v-btn color="primary" >Salvar</v-btn>
      </v-card-actions>
    </template>
  </v-card>
</template>
<script type="text/javascript">
import SliderComponent from "./SliderComponent";
export default {
  name: "SettingsComponent",
  components: {
    SliderComponent
  },
  data: () => ({
    title: 'Configurações do Dispositivo',
  }),

};
</script>