<template>
  <v-dialog v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <slot name="top"> </slot>
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