<template>
  <v-flex xs12 sm6 md6 lg4 mb-3 >
    <v-card>
      <v-card-title primary-title>          
        <v-flex>
          <div class="headline"><v-icon :color="this.colorIcons" >{{icon}}</v-icon> {{title}}</div>
          <!-- <span class="grey--text" v-model="value">{{value}}</span> -->
          <slot></slot>
        </v-flex>
      </v-card-title>
    </v-card>
  </v-flex>
</template>

<script type="text/javascript">
  export default {
    name: "CardComponent",
    props: {
      title: {
        type: String,
        default: ''
      },
      value: {
        type: String,
        default: ''
      },
      icon: {
        type: String,
        default: ''
      },
      medida: {
        type: String,
        default: ''
      },
      colorIcons:{
        type: String,
        default: ''
      }
    },
    data() {
      return {};
    }
  };
</script>