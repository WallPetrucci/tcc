<style scoped src="@/assets/MonitoringComponent.css"></style>
<template>
	<v-content>
		<Header></Header>
		<v-container fluid grid-list-md align-center justify-center>
			<MonitoringComponent :deviceID="userMonitoring.device_id">
				<template v-slot:header>
					<v-layout row class="top-monitoring">				
						<v-flex xs12 md6>
							<h1 class="headline">
								{{userMonitoring.name}}
							</h1>
							<div>
								<span class="subheading">Data de Nascimento: {{userMonitoring.date_birth}}</span>
							</div>
							<div>
								<span class="subheading">Sexo: Masculino</span>
							</div>
							<div>
								<span class="subheading">Celular: {{userMonitoring.cel}}</span>
							</div>
						</v-flex>
						<v-flex xs12 md6 >
							<img justify-end class="logo_monitoring" src="http://localhost:8080/img/logotcc.png">				
						</v-flex>
					</v-layout>	
				</template>	
			</MonitoringComponent>
		</v-container>
	</v-content>	
</template>

<script type="text/javascript">
	import Header from '../components-template/HeaderComponent'
	import MonitoringComponent from '../components-template/MonitoringComponent'
	import axios from 'axios';
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
				headerShow: false,
				userMonitoring: {
					name: '',
					cel: '',
					date_birth: '',
					user_sex: '',
					device_id: ''
				}
			}
		},
		mounted(){
			axios.post("http://localhost:5000/api/monitoring/", {token: this.monitorToken})
			.then((response) => {
				// console.log(response)
				if(response.data.device_id){
					this.userMonitoring = {
						name: response.data.user_name,
						cel: response.data.cel,
						date_birth: response.data.date_birth,
						user_sex: response.data.user_sex,
						device_id: response.data.device_id
					}
				}
				console.log(this.userMonitoring)		
			})
			.catch(()=> {
				this.progressLinear = false
				this.error_message = "Token inválido."
			})
		},
		props: {
			monitorToken: {
				type: String,
				default: ''
			}
		}
	}

</script>