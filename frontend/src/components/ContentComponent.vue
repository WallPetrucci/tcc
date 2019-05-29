<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout justify-center align-center>
        <v-flex text-xs-center>
          <CardComponent></CardComponent>
          <CardComponent></CardComponent>
          <CardComponent></CardComponent>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script type="text/javascript">
import CardComponent from "./CardComponent";
export default {
  name: "ContentComponent",
  components: {
    CardComponent
  },
  data() {
    return {
      ecosystem: [
        {
          text: "vuetify-loader",
          href: "https://github.com/vuetifyjs/vuetify-loader"
        },
        {
          text: "github",
          href: "https://github.com/vuetifyjs/vuetify"
        },
        {
          text: "awesome-vuetify",
          href: "https://github.com/vuetifyjs/awesome-vuetify"
        }
      ],
      importantLinks: [
        {
          text: "Documentation",
          href: "https://vuetifyjs.com"
        },
        {
          text: "Chat",
          href: "https://community.vuetifyjs.com"
        },
        {
          text: "Made with Vuetify",
          href: "https://madewithvuetifyjs.com"
        },
        {
          text: "Twitter",
          href: "https://twitter.com/vuetifyjs"
        },
        {
          text: "Articles",
          href: "https://medium.com/vuetify"
        }
      ],
      whatsNext: [
        {
          text: "Explore components",
          href: "https://vuetifyjs.com/components/api-explorer"
        },
        {
          text: "Select a layout",
          href: "https://vuetifyjs.com/layout/pre-defined"
        },
        {
          text: "Frequently Asked Questions",
          href:
            "https://vuetifyjs.com/getting-started/frequently-asked-questions"
        }
      ]
    };
  }
};
</script>
