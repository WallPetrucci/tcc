<template>
  <div>
    <div><h5>Conexão com Servidor</h5> <p> {{status_conn}} </p> </div>
    <div class="dados">{{data_client[0][type]}} {{measure}}</div>
    <div>Ultima alteração: {{data_client[0]['date']}}</div>
  </div>
</template>

<script>
  var socket = null
  export default {
    name: "ListenSocket",
    props: {
      type: String,
      measure: String
    },
    data () {
      return {
        data_client: [],
        status_conn: ''
      }
    },
    created() {      
      socket = this.$socket
    },
    sockets:{
      connect(){
        this.status_conn = "Conectado"
      },
      response_front(data) {
         this.data_client = data
      },
      disconnect(){
        this.status_conn = "Desconectado"
      },
    },
  }
</script>