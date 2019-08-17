<style scoped src="@/assets/MonitoringComponent.css"></style>
<template>
	<v-content>
		<Header></Header>
		<v-container fluid grid-list-md align-center justify-center>
			<MonitoringComponent>
				<template v-slot:header>
					<v-layout row class="top-monitoring">				
						<v-flex xs12 md6>
							<h1 class="headline">
								Wallace Petrucci Neves
							</h1>
							<div>
								<span class="subheading">Idade: 26 anos</span>
							</div>
							<div>
								<span class="subheading">Sexo: Masculino</span>
							</div>
							<div>
								<span class="subheading">Telefone: (19) 3535-3535</span>
							</div>
							<div>
								<span class="subheading">Celular: (19) 971676978</span>
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