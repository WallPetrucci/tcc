<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout justify-start>
        <v-flex text-xs-center>
          <v-layout row align-baseline align-start>
			<div>
				{{content}}
			</div>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>	
</template>

<script type="text/javascript">
	export default {
		name: "Page404",
		data() {
			return{
				content: "404 Page"
			}
		}
	}


</script>