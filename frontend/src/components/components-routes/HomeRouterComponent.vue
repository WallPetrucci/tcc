<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout justify-start>
        <v-flex text-xs-center>
          <v-layout row align-baseline align-start>
            <div>{{content}}</div>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script type="text/javascript">
// import Header from "../components-template/HeaderComponent"
export default {
  name: "Home",
  // components: {
  // 	Header
  // },
  data() {
    return {
      content: "Home Page"
    };
  },
  mounted() {}
};
</script>