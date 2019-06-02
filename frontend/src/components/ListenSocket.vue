<template>
  <div>
    <input type="text" v-model="message"/>
    <button @click="emitEvent">emit</button>
  </div>
</template>

<script>
  export default {
    name: "ListenSocket",
    data () {
      return {
        message: ''
      }
    },
    sockets:{
      connect(){
        console.log("Connect Socket")
        this.$socket.emit('response_socket');
      },
      disconnect(){
        console.log("Disconnect Socket")
      }
    },
    methods: {
      emitEvent () {
        console.log("Foi")
        this.$socket.emit('my message', {msg: this.message})
      }
    }
  }
</script>