<template>
	<v-card>
		<v-tabs v-model="tab" background-color="white accent-4" center-active dark
		color="#00b9b4" centered>
		<v-tab>Editar Dados</v-tab>
		<v-tab>Editar Senha</v-tab>

		<v-tabs-items>
			<v-tab-item>
				<v-card-text>
					<v-text-field label="Nome Completo" v-model="name"></v-text-field>
					<v-text-field label="Email" value="" v-model="email"></v-text-field>
					<v-menu ref="menu" :close-on-content-click="false" :nudge-right="40" lazy
					transition="scale-transition" offset-y full-width min-width="290px" max-heigth="100px">
					<template v-slot:activator="{ on }">
						<v-text-field v-model="date" label="Data de Nascimento" readonly v-on="on"></v-text-field>
					</template>
					<v-date-picker ref="picker" v-model="date" @change="displaySaveDate" :max="new Date().toISOString().substr(0, 10)"
					min="1950-01-01"></v-date-picker>
				</v-menu>
				<v-text-field label="Celular" placeholder="(99) 99999-9999" mask="(##) ####-#####" v-model="cel"></v-text-field>
			</v-card-text>
		</v-tab-item>
		<v-tab-item>
			<v-card-text>
				<v-text-field label="Senha" type="password"></v-text-field>
				<v-text-field label="Confirmar Senha" type="password"></v-text-field>
			</v-card-text>
		</v-tab-item>
	</v-tabs-items>
</v-tabs>
<v-card-actions>
	<v-spacer></v-spacer>
	<v-btn color="primary" @click="editDataUser">
		Enviar
	</v-btn>
</v-card-actions>
<v-progress-linear :indeterminate="true" :active="progressLinear"></v-progress-linear>
</v-card>
</template>

<script>
import axios from 'axios';
export default {
	name: "EditDataComponent",
	data () {
		return {
			menu: false,
			name: '',
			cel: '',
			tab: 0,
			email: '',
			email_confirm: '',
			date: null,
			step:0,
			progressLinear: false,
		}
	},
	mounted(){
		console.log("Teste")
		axios.get("http://localhost:5000/api/user/"+this.$session.get('id_user'))
		.then((response) => {
			if(response.data.id){
				this.date = response.data.date_birth
				this.name = response.data.name
				this.cel = response.data.cel
				this.email = response.data.email
			}
		})
		.catch(()=> {
			this.progressLinear = false
			this.error_message = "Email ao carregar usuario."
		})
	},
	methods : {
		displaySaveDate (date) {
			var split = date.split("-")
			var reversed = split.reverse()
			var datereverse = reversed.join("-")
			this.date = datereverse
			this.$refs.menu.save(datereverse)
		},
		editDataUser(){
			const userdata = {
				nomeRegistro: this.date,
				niverRegistro: this.name,
				celRegistro: this.cel,
				emailRegistro: this.email
			}
			this.progressLinear = true
			axios.put("http://localhost:5000/api/user/"+this.$session.get('id_user'), userdata)
			.then((response) => {
				if(response.data.idUser){
					console.log(response.data)
				}
			})
			.catch(()=> {
				this.progressLinear = false
				this.error_message = "Erro ao carregar info de usuarios."
			})
		}
	}
}
</script>