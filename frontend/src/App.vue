<template>
  <v-app>
   <!--  <HeaderComponent> </HeaderComponent>
    <ContentComponent> </ContentComponent>
    <FooterComponent> </FooterComponent> -->
    <router-view> </router-view>
    <FooterComponent> </FooterComponent>
  </v-app>
</template>

<script>  
  // import HeaderComponent from './components/components-template/HeaderComponent'
  // import ContentComponent from './components/components-template/ContentComponent'
  import FooterComponent from './components/components-template/FooterComponent'


  export default {
    name: 'App',
    components: {
    //   HeaderComponent,
    //   ContentComponent,
      FooterComponent
    }
  }
</script>
