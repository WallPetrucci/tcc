<template>
  <v-dialog v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-icon v-on="on">fas fa-chart-area </v-icon>
    </template>


    <slot ></slot>

  </v-dialog>
</template>
<script type="text/javascript">
export default {
  name: "ModalComponent",
  data: () => ({
    dialog:false
  }),

};
</script>