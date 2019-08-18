<template>
  <v-dialog v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-icon  v-on="on">{{icone}}<span>{{title}}</span></v-icon> 
      <a href="#"  v-on="on">
        <span v-if="showTitle">{{title}}</span>
      </a>
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

  props:{
    icone:{
      type: String,
      default: 'fas fa-sliders-h'
    },
    title:{
      type: String,
      default: ''
    },
    showTitle:{
      type: Boolean,
      default: false,
    }
  }

};
</script>