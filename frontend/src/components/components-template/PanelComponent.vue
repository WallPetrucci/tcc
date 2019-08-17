
<template>
	<v-container>
		<v-layout row wrap>
			<v-flex xs12 mb-2>
				<Monitoring>
				</Monitoring>
			</v-flex>
			<v-flex xs6>
				<Monitor>
				</Monitor>
			</v-flex>
			<v-flex xs6>
				<Reports>
				</Reports>
			</v-flex>
		</v-layout>
	</v-container>
</template>
<style scoped src="@/assets/PanelComponent.css"></style>
<script type="text/javascript">
import Monitoring from './MonitoringComponent'
import Monitor from './MonitorComponent'
import Reports from './ReportsComponent'

export default {

	name: "Panel",
	components: {
		Monitoring,
		Monitor,
		Reports
	},
	data() {
		return {
		}
	}
}
</script>