<template>
  <v-dialog v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-icon v-on="on">fas fa-sliders-h
      <span>Configurar WHM</span></v-icon> 

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