<template>
<v-content>
		<v-container fluid fill-height>
			<Header></Header>
			<v-layout justify-center>
				<v-flex ms12>				
					<MonitorContent> </MonitorContent>	
				</v-flex>	
			</v-layout>
		</v-container>
	</v-content>	
</template>

<script type="text/javascript">
	import Header from "../components-template/HeaderComponent"
	import MonitorContent from '../components-template/MonitorComponent'
	import {APP_ROUTERS} from '../constants.js'
	export default {
		name: "Monitor",
		components: {
			Header,
			MonitorContent
		},
		beforeCreate: function () {
			if (!this.$session.exists()) {
				this.$router.push(APP_ROUTERS.login)
			}
		},
		data() {
			return{
				content: "Monitor Page"
			}
		},
		mounted() {
			// alert("Montou "+this.content);
		}
	}
	
	
</script>