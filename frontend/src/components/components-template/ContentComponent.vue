<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout justify-start>
        <v-flex text-xs-center>
          <v-layout row align-baseline align-start>
            <CardComponent title="Frequencia Cardiaca" icon="'mdi-heart-pulse'">
              <ListenSocket type="fc" measure="BPM"> </ListenSocket>
            </CardComponent>
            <CardComponent title="Oximetria">
              <ListenSocket type="ox" measure="SpO2"> </ListenSocket>
            </CardComponent>
            <CardComponent title="Temperatura">
              <ListenSocket type="temp" measure="Cº"> </ListenSocket>
            </CardComponent>     
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script type="text/javascript">
  import CardComponent from "./CardComponent";
  import ListenSocket from '../components-helpers/ListenSocket'
  export default {
    name: "ContentComponent",
    components: {
      CardComponent,
      ListenSocket
    },
    data() {
      return {
      }
    },
    methods: {

    }
  };
</script>
