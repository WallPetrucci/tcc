<template>
  <v-flex xs12 sm4 offset-rg1>
    <v-card>
      <v-card-title primary-title>
        <v-icon>mdi-heart-pulse</v-icon>
        <div>
          <!-- <div class="headline">{{title}}</div>
          <div class="grey--text" v-model="value">{{value}}</div> -->
          <slot></slot>
        </div>
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
    }
  },
  data() {
    return {};
  }
};
</script>