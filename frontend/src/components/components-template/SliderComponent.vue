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
          :step="0.5"
          >
        </v-range-slider>
        <!-- <span class="caption grey--text text--darken-1" >
         Você receberá um alerta quando sua {{this.title}} estiver abaixo de {{this.minMaxAux[0]}} ou acima de {{this.minMaxAux[1]}}
        </span> -->
      </v-flex>
    </v-layout>
  </v-card-text>

</template>

<script>
  export default {
    name: 'SliderComponent',
    data:() =>({
      minMaxModel: [],
      message: '',
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
        default:[0,10]
      },
    },

    // watch:{
    //   minMaxModel: function(newMinMax){
    //     console.log('Cheguei')
    //     this.minMaxAux = newMinMax
    //   }
    // }
  }
</script>