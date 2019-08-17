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
            <SliderComponent
              title="Frequência Cardíaca" 
              v-bind:minMaxRange="[0,160]"
              v-bind:step="0.5"
            />
            <SliderComponent 
              title="Oximetria"  
              v-bind:minMaxRange="[0,100]" 
              v-bind:step="1" 
            />
            <SliderComponent
              title="Temperatura Corporal"  
              v-bind:minMaxRange="[20, 40]" 
              v-bind:step="0.5" 
            />
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
<style>
::-webkit-scrollbar {
  width: 5px;
  height: 5px;
}


::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px grey; 
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: #4db6ac; 
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #4db6ac; 
}
</style>
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