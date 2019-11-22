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
            v-bind:minMaxRange="data_settings.fc"
            v-bind:step="0.5"
            />
            <SliderComponent 
            title="Oximetria"  
            v-bind:minMaxRange="data_settings.ox" 
            v-bind:step="1" 
            />
            <SliderComponent
            title="Temperatura Corporal"  
            v-bind:minMaxRange="data_settings.temp" 
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
  import axios from 'axios';
  export default {
    name: "SettingsComponent",
    components: {
      SliderComponent
    },
    data: () => ({
      title: 'Configurações do Dispositivo',
      data_settings: {
        fc: [50, 150],
        ox: [70, 100],
        temp: [34.5, 37]
      }
    }),

    mounted(){
      this.getAllSettings()
    },

    methods: {
      getAllSettings(){
        axios.get("http://localhost:5000/api/usersettings/"+this.$session.get('id_user'))
        .then((response) => {
         if(response.data.id_Settings){
          const my_settings = response.data
          console.log("My log " + my_settings)
          this.data_settings = {
            fc: [my_settings.heartRate.min, my_settings.heartRate.max],
            ox: [my_settings.oximetry.min, my_settings.oximetry.max],
            temp: [my_settings.temperature.min, my_settings.temperature.max]
          }
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