<template>	
	<v-card class="elevation-12">
		<v-toolbar dark color="primary">
			<v-toolbar-title>Monitorar Usuário</v-toolbar-title>
			<v-spacer></v-spacer>
			<v-tooltip bottom>
				<template v-slot:activator="{ on }">
					<v-icon>fas fa-search</v-icon>
				</template>
			</v-tooltip>
		</v-toolbar>
		<template >
			<v-form
			ref="form"
			lazy-validation
			class="monitoring-search"
			>
			<v-text-field
			:counter="30"
			label="Token de Monitoramento"
			v-model="token_user"
			required
			></v-text-field>

			<v-card-actions>
				<v-spacer></v-spacer>
				<v-btn color="primary" @click="searchUserForMonitoring()">Enviar</v-btn>
			</v-card-actions>
		</v-form>
		<v-progress-linear :indeterminate="true" :active="progressLinear"></v-progress-linear>
	</template>
</v-card>	
</template>

<style type="text/css">
	.monitoring-search{
		padding: 20px !important;
	}
</style>

<script type="text/javascript">
import {APP_ROUTERS} from '../constants.js';
import axios from 'axios';
	export default {
		name: "MonitoringSearch",
		data(){
			return {
				progressLinear: false,
				token_user: ''
				// valid: ''
			}
		},
		methods: {
			searchUserForMonitoring(){
				this.progressLinear = true
				console.log(this.token_user)
				// axios.post("http://localhost:5000/api/monitoring/", {token: this.token_user})
				// .then((response) => {
					if(this.token_user){
						// this.$session.start()
						this.$router.push(APP_ROUTERS.monitoring + "/" + this.token_user)
						
					}
				// })
				// .catch(()=> {
				// 	this.progressLinear = false
				// 	this.error_message = "Token inválido."
				// })
			}
		}
	}
</script>