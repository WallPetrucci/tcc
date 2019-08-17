<style scoped src="@/assets/MonitoringComponent.css"></style>
<template>
	<v-flex class="inner-monitoring">
		<slot></slot>
		<slot name="header"></slot>		
		<v-layout row class="bottom-monitoring">
			<v-layout>
				<CardComponent title="Frequência Cardiaca" icon="fas fa-heartbeat" colorIcons="red">
					<ListenSocket type="89" measure="bpm" >
					</ListenSocket>	
				</CardComponent>
				<CardComponent title="Temperatura" icon="fas fa-thermometer-quarter" colorIcons="orange">
					<ListenSocket type="35.8" measure="C">
					</ListenSocket>	
				</CardComponent>
				<CardComponent title="Oximetria" icon="fas fa-tint" colorIcons="blue">
					<ListenSocket type="100" measure="%">
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
	components:{
		ListenSocket,
		CardComponent
	}
}
</script>