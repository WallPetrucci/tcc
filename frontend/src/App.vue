<template>
  <v-app>
    <HeaderComponent :drawer="drawer"> </HeaderComponent>
    <ContentComponent> </ContentComponent> 
    <FooterComponent ></FooterComponent>
  </v-app>
</template>

<script>

  import HeaderComponent from './components/HeaderComponent'
  import ContentComponent from './components/ContentComponent'
  import FooterComponent from './components/FooterComponent'


  export default {
    name: 'App',
    components: {
      HeaderComponent,
      ContentComponent,
      FooterComponent

    },

    data () {
      return {
        drawer: null
      }
    }
  }
</script>
