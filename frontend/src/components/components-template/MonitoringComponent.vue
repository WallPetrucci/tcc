<style scoped src="@/assets/MonitoringComponent.css"></style>
<template>
	<v-flex class="inner-monitoring">
		<slot></slot>
		<slot name="header"></slot>		
		<v-layout row class="bottom-monitoring">
			<v-layout row wrap >
				<CardComponent title="Frequência Cardiaca" icon="fas fa-heartbeat" colorIcons="red">
					<ListenSocket type="heart" measure="bpm" :deviceID="this.deviceID">
					</ListenSocket>	
				</CardComponent>
				<CardComponent title="Temperatura" icon="fas fa-thermometer-quarter" colorIcons="orange">
					<ListenSocket type="temperature" measure="ºC" :deviceID="this.deviceID">
					</ListenSocket>	
				</CardComponent>
				<CardComponent title="Oximetria" icon="fas fa-tint" colorIcons="blue">
					<ListenSocket type="oximetry" measure="%" :deviceID="this.deviceID">
					</ListenSocket>	
				</CardComponent>
			</v-layout>
		</v-layout>
	</v-flex>
</template>
<style type="text/css">
.inner-monitoring  .v-card.v-sheet.theme--light {
	width: 97%
}
</style>
<script type="text/javascript">
import ListenSocket from '../components-helpers/ListenSocket'
import CardComponent from '../components-template/CardComponent'
export default {
	name: "MonitoringComponent",
	mounted() {
		console.log("Dentro de MonitoringComponent " + this.deviceID)
	},
	components:{
		ListenSocket,
		CardComponent
	},
	props:{
		deviceID: {
			type: String,
			default: 'teste'
		}
	}
}
</script>