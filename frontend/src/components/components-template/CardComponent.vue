<template>
  <v-flex xs12 sm4 offset-rg1>
    <v-card>
      <v-card-title primary-title>
        <v-icon>mdi-heart-pulse</v-icon>
        <div>
          <div class="headline">{{title}}</div>
          <span class="grey--text" v-model="value">{{value}}</span>
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
    title: String,
    value: String,
    icon: String,
    medida: String
  },
  data() {
    return {};
  }
};
</script>