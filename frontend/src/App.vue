<template>
  <v-app>
    <router-view> </router-view>
    <FooterComponent />
  </v-app>  
</template>

<script> 
  import FooterComponent from './components/components-template/FooterComponent'


  export default {
    name: 'App',
    data: () => ({
      verifyUser: false,
    }),
    components: {
      FooterComponent
    },
    methods: {
      clickPage(){
        // console.log('clicou')
      }
    }
  }
</script>
