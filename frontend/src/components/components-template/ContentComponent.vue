<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout justify-start>
        <v-flex text-xs-center>
          <v-layout row align-baseline align-start>
            <CardComponent title="Frequencia Cardiaca" value="45 BPM" :icon="'mdi-heart-pulse'"></CardComponent>
            <CardComponent title="Oximetria" value="80"></CardComponent>
            <CardComponent title="Temperatura" value="36º"></CardComponent>
            <SocketIo></SocketIo>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script type="text/javascript">
  import CardComponent from "./CardComponent";
  import SocketIo from '../ListenSocket'
  export default {
    name: "ContentComponent",
    components: {
      CardComponent,
      SocketIo
    },
    data() {
      return {
      }
    }
  };
</script>
