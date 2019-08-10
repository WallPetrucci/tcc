<template>
  <div>
    <div>
      <h5>Conexão com Servidor</h5> 
      <div v-if="this.status_conn"> <v-icon color="green">fas fa-check-circle</v-icon> </div> 
      <div v-else> <v-icon color="red">fas fa-times-circle</v-icon> </div> 
    </div>
   <!--  <div class="dados">{{data_client[0][type]}} {{measure}}</div>
    <div>Ultima alteração: {{data_client[0]['date']}}</div> -->
  </div>
</template>
<style type="text/css">
  .dados{
    font-size:25px;
  }
</style>
<script>
  var socket = null
  export default {
    name: "ListenSocket",
    props: {
      type: {
        type: String,
        default: ''
      },
      measure: {
        type: String,
        default: ''
      }
    },
    data () {
      return {
        data_client: [],
        status_conn: false
      }
    },
    created() {      
      var socket = this.$socket
    },
    sockets:{
      connect(){
        this.status_conn = true
      },
      response_front(data) {
        if(data.length > 0){
         this.data_client = data
        }else{
          this.data_client = []
        }
      },
      disconnect(){
        this.status_conn = false
      },
    },
  }
</script>