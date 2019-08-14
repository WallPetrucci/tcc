<template>
  <v-card-text>
    <v-layout row>
      <v-flex>
        <v-subheader class="pl-0 font-weight-regular subheading">{{this.title}}</v-subheader>
        <v-range-slider v-model="minMaxModel"
          thumb-label="always"
          :thumb-size="30"
          :max="minMaxRange[1]"
          :min="minMaxRange[0]"
          :step="step"
          
          >
        </v-range-slider>
        <span class="caption grey--text text--darken-1" >
         Você receberá um alerta quando sua {{this.title}} estiver abaixo de {{this.minMaxModel[0]}} ou acima de {{this.minMaxModel[1]}}
        </span>
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
      step:{
        type: Number,
        default:1
      },
    }
  }
</script>