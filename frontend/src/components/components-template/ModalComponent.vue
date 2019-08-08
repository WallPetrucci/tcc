<template>
  <v-dialog v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-toolbar-title v-on="on">Configurações</v-toolbar-title>
    </template>

    <v-card>
      <v-slot></v-slot>
    </v-card>
  </v-dialog>
</template>
<script type="text/javascript">
export default {
  name: "ModalComponent",
  data: () => ({
    step: 1,
    displayRegister: false,
    date: null,
    menu: false
  }),

  props: {
    component: {
      type: Object,
      default: {}
    }
  }
};
</script>