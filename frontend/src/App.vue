<template>
  <v-app >
    <router-view> </router-view> 
  </v-app>  
</template>

<script>  
  import HeaderComponent from './components/components-template/HeaderComponent'
  import ContentComponent from './components/components-template/ContentComponent'
  import FooterComponent from './components/components-template/FooterComponent'


  export default {
    name: 'App',
    data: () => ({
      verifyUser: false,
    }),
    components: {
      HeaderComponent,
      ContentComponent,
      FooterComponent
    },
    methods: {
      clickPage(){
        // console.log('clicou')
      }
    }
  }
</script>
