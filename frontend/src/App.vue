<template>
  <v-app>
      <HeaderComponent> </HeaderComponent> 
      <ContentComponent> </ContentComponent> 
    <v-footer>
    </v-footer>
  </v-app>
</template>

<script>

  import HeaderComponent from './components/HeaderComponent'
  import ContentComponent from './components/ContentComponent'


  export default {
    name: 'App',
    components: {
      HeaderComponent,
      ContentComponent

    },

    data () {
      return {
      //
    }
  }
}
</script>
