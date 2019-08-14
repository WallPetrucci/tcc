<template>
  <v-card-text>
    <v-layout row>
      <v-flex>
        <v-subheader class="pl-0 font-weight-regular subheading">{{this.title}}</v-subheader>
        <v-range-slider v-model="this.minMaxModel"
          thumb-label="always"
          :thumb-size="26"
          :max="minMaxRange[1]"
          :min="minMaxRange[0]"
          :step="0.5">
        </v-range-slider>
      </v-flex>
    </v-layout>
  </v-card-text>

</template>

<script>
  export default {
    name: 'SliderComponent',
    data:() =>({
      minMaxModel: []
    }),

    mounted(){
      this.minMaxModel =  this.minMaxModel == false ?  this.minMaxRange : this.minMaxModel
    },
    props:{
      title:{
        type: String,
        default: '',
      },
      minMaxRange:{
        type: Array,
        default: () => {return [0,10]}
      },
    }

  }
</script>