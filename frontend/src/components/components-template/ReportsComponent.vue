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
					<v-icon>phone</v-icon>
				</v-tab>

				<v-tab href="#temp" class="primary--text">
					<v-icon>favorite</v-icon>
				</v-tab>

				<v-tab href="#ox" class="primary--text">
					<v-icon>account_box</v-icon>
				</v-tab>
			</v-tabs>
		</template>
	</v-toolbar>

	<v-tabs-items v-model="tabs" class="white elevation-1">
		<v-tab-item
		value="fc"
		>
		<v-card>
			<v-card-text><highcharts :options="chartOptionsFc">
				{{text}}
			</highcharts></v-card-text>
		</v-card>
	</v-tab-item>
	<v-tab-item
		value="temp"
		>
		<v-card>
			<v-card-text><highcharts :options="chartOptionsTemp">
				{{text}}
			</highcharts></v-card-text>
		</v-card>
	</v-tab-item>
	<v-tab-item
		value="ox"
		>
		<v-card>
			<v-card-text><highcharts :options="chartOptionsOx">
				{{text}}
			</highcharts></v-card-text>
		</v-card>
	</v-tab-item>
</v-tabs-items>
</v-flex>
</template>

<script type="text/javascript">
	export default {
		name: "Reports",
		data() {
			return {
				chartOptionsFc: {
					title: {
						text: 'Frequência Cardiaca'
					},
					series: [{
						data: [1,2,3]
					}]
				},
				chartOptionsTemp: {
					title: {
						text: 'Temperatura Corporal'
					},
					series: [{
						data: [1,2,3]
					}]
				},
				chartOptionsOx: {
					title: {
						text: 'Oximetria'
					},
					series: [{
						data: [1,2,3]
					}]
				},
				tabs: null,
				text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
			}
		}
	}
</script>