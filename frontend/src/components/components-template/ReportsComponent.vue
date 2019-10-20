<template>
	<v-flex>
		<v-toolbar tabs>
			<v-toolbar-title>Relatórios</v-toolbar-title>

			<v-spacer></v-spacer>

			<template v-slot:extension>
				<v-tabs
				v-model="tabs"
				fixed-tabs
				color="transparent"
				>
				<v-tabs-slider></v-tabs-slider>
				<v-tab href="#fc" class="primary--text">
					<v-icon>fas fa-heartbeat</v-icon>
				</v-tab>

				<v-tab href="#temp" class="primary--text">
					<v-icon>fas fa-thermometer-quarter</v-icon>
				</v-tab>

				<v-tab href="#ox" class="primary--text">
					<v-icon>fas fa-tint</v-icon>
				</v-tab>
			</v-tabs>
		</template>
	</v-toolbar>

	<v-tabs-items v-model="tabs" class="white elevation-1">
		<v-tab-item
		value="fc"
		>
		<v-card>
			<v-card-text>
				<highcharts :options="chartOptionsFc">
				</highcharts>
			</v-card-text>
		</v-card>
	</v-tab-item>
	<v-tab-item
	value="temp"
	>
	<v-card>
		<v-card-text>
			<highcharts :options="chartOptionsTemp">
			</highcharts>
		</v-card-text>
	</v-card>
</v-tab-item>
<v-tab-item
value="ox"
>
<v-card>
	<v-card-text>
		<highcharts :options="chartOptionsOx">
			
		</highcharts>
	</v-card-text>
</v-card>
</v-tab-item>
</v-tabs-items>
</v-flex>
</template>

<script type="text/javascript">
import axios from 'axios';
export default {
	name: "Reports",
	mounted(){
		var id_user = this.$session.get('id_user')
		axios.get("http://localhost:5000/api/resultsmetrics/"+id_user)
		.then((response) => {
			// console.log(response.data)
			var heart_data = []
			var ox_data = []
			var temp_data = []
			console.log(response.data)
			if(response.data){
				// console.log(response.data)
				response.data.heart.forEach((el, ind, array)=>{
					heart_data.push({x: new Date(el.data), y: el.result})
				})
				response.data.oximetry.forEach((el, ind, array)=>{
					ox_data.push({x: new Date(el.data), y: el.result})
				})
				response.data.temperature.forEach((el, ind, array)=>{
					temp_data.push({x: new Date(el.data), y: el.result})
				})
				console.log(heart_data)
				this.chartOptionsFc.series[0].data = heart_data
				this.chartOptionsOx.series[0].data = ox_data
				this.chartOptionsTemp.series[0].data = temp_data
				// this.chartOptionsFc.series.addPoint([x, y], true, false)

			}
		})
		.catch(()=> {
			this.progressLinear = false
			this.error_message = "Email ou Senha inválido."
		})
	},
	data() {
		return {
			chartOptionsFc: { 
				title: {
					text: 'Frequência Cardiaca'
				},

				xAxis: {
					type: 'datetime',
					tickPixelInterval: null,
					pointInterval: 24 * 3600 * 1000,
					dateTimeLabelFormats: {
						day: '%e of %b'
					}

				},

				series: [{
					data: [	
					],
					name: "Frequência Cárdiaca"
				}]

			},
			chartOptionsTemp: {
				title: {
					text: 'Temperatura Corporal'
				},
				xAxis: {
					type: 'datetime',
					tickPixelInterval: null,
					// pointInterval: 24 * 3600 * 1000,
					dateTimeLabelFormats: {
						day: '%e of %b'
					}

				},
				series: [{
					data: []
				}]
			},
			chartOptionsOx: {
				title: {
					text: 'Oximetria'
				},
				xAxis: {
					type: 'datetime',
					tickPixelInterval: null,
					pointInterval: 24 * 3600 * 1000,
					dateTimeLabelFormats: {
						day: '%e of %b'
					}

				},
				series: [{
					data: []
				}]
			},
			tabs: null,
			text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
		}
	}
}
</script>