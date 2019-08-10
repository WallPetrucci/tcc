<style scoped src="@/assets/MonitoringComponent.css"></style>
<template>
	<v-content>		
		<v-container fluid grid-list-md align-center justify-center>
			<v-flex class="inner-monitoring">
				<div>
					<h1 class="title-monitoring">Tela de Monitoramento</h1>
					<!-- <div class="date-monitoring"> Data: {{now}} </div> -->
				</div>
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
	import ListenSocket from '../components-helpers/ListenSocket'
	import CardComponent from '../components-template/CardComponent'
	import {APP_ROUTERS} from '../constants.js'

	export default {
		name: 'Monitoring',
		components: {
			ListenSocket,
			CardComponent
		},
		data() {
			return {
				paramRoute: this.monitorToken,
				currentDate: ''
			}
		},
		beforeMount(){
			if(this.monitorToken !== 'wallacetoken'){
				this.$router.push(APP_ROUTERS.base)
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