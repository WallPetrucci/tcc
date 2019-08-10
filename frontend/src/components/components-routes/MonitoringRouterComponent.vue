<style scoped src="@/assets/MonitoringComponent.css"></style>
<template>
	<v-content>
		<Header></Header>
		<v-container fluid fill-height>
			<v-layout justify-start>
				<v-flex text-xs-center>
					<v-layout row align-baseline align-start>
							<CardComponent>
								<ListenSocket>
								</ListenSocket>	
							</CardComponent>
							<CardComponent>
								<ListenSocket>
								</ListenSocket>	
							</CardComponent>
							<CardComponent>
								<ListenSocket>
								</ListenSocket>	
							</CardComponent>
					</v-layout>
				</v-flex>
			</v-layout>
		</v-container>
	</v-content>	
</template>

<script type="text/javascript">
	import ListenSocket from '../components-helpers/ListenSocket'
	import CardComponent from '../components-template/CardComponent'

	export default {
		name: 'Monitoring',
		components: {
			ListenSocket,
			CardComponent
		},
		data() {
			return {
				paramRoute: this.monitorToken
			}
		},
		mounted(){

		},
		props: {
			monitorToken: {
				type: String,
				default: ''
			}
		}
	}

</script>