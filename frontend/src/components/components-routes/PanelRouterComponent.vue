<template>
	<v-content>
		<Header></Header>
		<v-container fluid fill-height style="padding:10px">
			<v-layout justify-start>
				<v-flex text-xs-center>
					<v-layout row align-baseline align-start>
						<PanelComponent>
						</PanelComponent>
					</v-layout>
				</v-flex>
			</v-layout>
		</v-container>
	</v-content>	
</template>

<script type="text/javascript">
	import Header from "../components-template/HeaderComponent"
	import PanelComponent from "../components-template/PanelComponent"
	import {APP_ROUTERS} from '../constants.js'
	export default {
		name: "Panel",
		components: {
			Header,
			PanelComponent
		},
		beforeCreate: function () {
			if (!this.$session.exists()) {
				this.$router.push(APP_ROUTERS.login)
			}
		},
		data() {
			return{
				content: "Panel Page"
			}
		},
		mounted() {
			// alert("Montou "+this.content);
		}
	}
	
	
</script>