<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout justify-center>
        <v-flex text-xs-center>
          <v-layout align-center justify-center row fill-height>
				<Page404Component></Page404Component>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>	
</template>

<script type="text/javascript">
import Page404Component from '../components-template/Page404Component'
	export default {
		name: "Page404",
		components : {
			Page404Component
		},
		data() {
			return{
				content: "404 Page"
			}
		},

	}


</script>