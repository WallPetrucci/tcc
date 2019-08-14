<style scoped src="@/assets/MonitoringComponent.css"></style>
<template>
	<v-content>
		<Header></Header>
		<v-container fluid grid-list-md align-center justify-center>
			<MonitoringComponent></MonitoringComponent>
		</v-container>
	</v-content>	
</template>

<style type="text/css">
.logo_monitoring{
	width:300px;
	float: right;	
}
.flex.inner-monitoring {
	/*width: 370px;*/
	margin: 0 auto;
}
div.inner-monitoring {
	width: 70%;
	margin: 0 auto;
	box-shadow: 0px 0px 20px 4px rgba(0, 0, 0, 0.16);
	padding: 20px;
	background: #4db6ac;
	color: white;
}
.container.grid-list-md .top-monitoring.row {
	margin-bottom: 30px;
}
.title-monitoring {
	margin-bottom: 20px;
	font-weight: 500;
	font-size: 40px;
}
.date-monitoring{

}
</style>

<script type="text/javascript">
import Header from '../components-template/HeaderComponent'
import MonitoringComponent from '../components-template/MonitoringComponent'
import {APP_ROUTERS} from '../constants.js'

export default {
	name: 'Monitoring',
	components: {
		MonitoringComponent,
		Header
	},
	data() {
		return {
			paramRoute: this.monitorToken,
			currentDate: '',
			headerShow: false
		}
	},
	beforeMount(){
		if(this.monitorToken !== 'wallacetoken'){
			this.$router.push(APP_ROUTERS.monitoring)
		}
	},
	props: {
		monitorToken: {
			type: String,
			default: ''
		}
	}
}

</script>