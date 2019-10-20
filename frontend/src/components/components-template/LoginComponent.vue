<style scoped src="@/assets/LoginPageComponent.css"></style>
<template>
	<v-card class="elevation-12">
		<v-toolbar dark color="primary">
			<v-toolbar-title>{{currentTitle}}</v-toolbar-title>
			<v-spacer></v-spacer>
			<v-tooltip bottom>
				<template v-slot:activator="{ on }">
					<v-btn icon large target="_blank" v-on="on" @click="displayRegisterMethod()">
						<v-icon>fas fa-user-plus</v-icon>
						
					</v-btn>
				</template>
				<span>Novo Cadastro</span>
			</v-tooltip>
		</v-toolbar>
		<template>
			<v-window v-model="step">
				<v-window-item :value="1">
					<v-card-text>
						<v-form>
							<v-text-field prepend-icon="person" name="login" label="Email" type="text" v-model="emailLogin"></v-text-field>
							<v-text-field id="password" prepend-icon="lock" name="password" label="Senha" type="password" v-model="senhaLogin"></v-text-field>
						</v-form>
					</v-card-text>
					<v-card-actions>
						<v-spacer></v-spacer> 
						<v-btn color="primary" class="esqueceusenha" @click="displayAbrirEsqueciSenha()">
							Esqueceu a Senha <v-icon style="font-size: 13px; top:-1px; position:relative;margin-left:5px">fas fa-question</v-icon>
						</v-btn>
						<v-btn color="primary" @click="doLogin()">Acessar</v-btn>
					</v-card-actions>
				</v-window-item>
				<v-window-item :value="2">
					<v-card-text>
						<v-text-field
						label="Email"
						value=""
						v-model="dataRegister.emailRegistro"
						></v-text-field>
					</v-card-text>
				</v-window-item>
				
				<v-window-item :value="3">
					<v-card-text>
						<v-text-field
						label="Senha"
						type="password"
						v-model="dataRegister.senhaRegistro"
						></v-text-field>
						<v-text-field
						label="Confirmar Senha"
						type="password"
						v-model="dataRegister.senhaConfirmaRegistro"
						></v-text-field>
						<span class="caption grey--text text--darken-1">
							Entre com sua senha
						</span>
					</v-card-text>
				</v-window-item>
				
				<v-window-item :value="4">
					<v-card-text>
						<v-text-field
						label="Nome Completo"
						required
						v-model="dataRegister.nomeRegistro"
						></v-text-field>
						<v-menu
						ref="menu"
						v-model="menu"
						:close-on-content-click="false"
						:nudge-right="40"
						lazy
						transition="scale-transition"
						offset-y
						full-width
						min-width="290px"
						max-heigth="100px"
						>
						<template v-slot:activator="{ on }">
							<v-text-field
							v-model="dataRegister.niverRegistro"
							label="Data de Nascimento"
							readonly
							v-on="on"
							></v-text-field>
						</template>
						<v-date-picker
						ref="picker"
						v-model="dataRegister.niverRegistro"
						:max="new Date().toISOString().substr(0, 10)"
						min="1950-01-01"
						@change="displaySaveDate"
						></v-date-picker>
					</v-menu>
					<v-text-field
					label="Celular"
					placeholder="(99) 99999-9999"
					mask="(##) ####-#####"
					v-model="dataRegister.celRegistro"
					></v-text-field>
					<span class="caption grey--text text--darken-1">
						Insira seus Dados Pessoais
					</span>
				</v-card-text>				
			</v-window-item>
			
			<v-window-item :value="5">
				<div class="pa-3 text-xs-center">
					<v-icon>fas fa-check-circle</v-icon>
					<h3 class="title font-weight-light mb-2">Seja bem vindo!</h3>
					<span class="caption grey--text">Cadastro efetuado com sucesso</span>
				</div>
			</v-window-item>

			<v-window-item :value="6">
				<div class="pa-3 text-xs-center">
					<v-card-text>
						<v-text-field
						label="Email"
						value=""
						></v-text-field>
					</v-card-text>
					<span class="caption grey--text">Verifique sua caixa de entrada, e clique no link informado.</span>
				</div>
			</v-window-item>
		</v-window>
		
		<v-divider></v-divider>
		
		<v-card-actions v-if="step > 1">
			<v-btn
			:disabled="step === 1 || step === 5"
			flat
			@click="step--"
			v-if="step !== 6"
			>
			Voltar
		</v-btn>
		<v-btn
		v-if="step === 6"
		flat
		@click="step = 1"
		>
		Voltar
	</v-btn>
	<v-spacer></v-spacer>
	<v-btn

	color="primary"
	depressed
	@click="step++"
	v-if="step < 4"
	>
	Avançar
</v-btn>
<v-btn

color="primary"
depressed
@click="step = 1"
v-if="step == 5"
>
Entrar no painel
</v-btn>
<v-btn		
color="primary"
@click="displayRegisterUser()"
v-if="step == 4"
>
Cadastrar
</v-btn>
<v-btn		
color="primary"
@click="enviarEsqueceuSenha()"
v-if="step == 6"
>
Enviar
</v-btn>
</v-card-actions>
</template>
<v-alert
:value="error_message"
color="error"
icon="warning"
outline
>
{{error_message}}
</v-alert>
<v-progress-linear :indeterminate="true" :active="progressLinear"></v-progress-linear>
</v-card>	
</template>
<script type="text/javascript">
import {APP_ROUTERS} from '../constants.js';
import axios from 'axios';
export default {
	name: "LoginComponent",
	data() { 
		return {
			step: 1,
			displayRegister: false,
			date: null,
			menu: false,
			emailLogin: '',
			senhaLogin: '',
			dataRegister: {
				nomeRegistro: '',
				emailRegistro: '',
				senhaRegistro: '',
				niverRegistro: '',
				celRegistro: ''
			},		
			progressLinear: false,
			error_message: ''

		}},
		mounted(){
			this.displayRegister = false
			this.progressLinear = false
		},
		beforeCreate: function () {
			if (this.$session.exists()) {
				this.$router.push('/painel')
			}else{
				this.$session.destroy()
			}
		},
		computed: {
			currentTitle () {
				switch (this.step) {
					case 1: return 'Painel de Acesso'
					case 2: return 'Registrar'
					case 3: return 'Registrar'
					case 4: return 'Registrar'
					case 5: return 'Cadastro Concluido!'
					case 6: return 'Recuperar a senha'
					default: return 'Registrado com Sucesso'
				}
			}
		},
		watch: {
			menu (val) {
				val && setTimeout(() => (this.$refs.picker.activePicker = 'YEAR'))
			}
		},
		methods : {
			displayRegisterMethod() {
				this.step = 2
				this.displayRegister = true				
			},
			displayAbrirEsqueciSenha(){
				this.step = 6
			},
			displayRegisterUser() {								
				this.progressLinear = true
				if(this.dataRegister.senhaRegistro != this.dataRegister.senhaConfirmaRegistro){
					this.error_message = "Senha e Confirmar Senha não sao iguais"
					this.progressLinear = false
					return true
				}
				if(this.dataRegister.senhaRegistro == ""){
					this.error_message = "Senha em branco"
					this.progressLinear = false
					return true
				}
				if(this.dataRegister.senhaConfirmaRegistro == ""){
					this.error_message = "Confirmar Senha em branco"
					this.progressLinear = false
					return true
				}
				if(this.dataRegister.emailRegistro == ""){
					this.error_message = "Email em Branco"
					this.progressLinear = false
					return true
				}
				axios.post("http://localhost:5000/api/user/", this.dataRegister)
				.then((response) => {
					if(response.data.sucesso == false || response.data.sucesso){
						this.progressLinear = false
						this.error_message = "Ocorreu algum problema tente novamente."
						this.step = 1						
					}else{
						this.dataRegister = {
							nomeRegistro: '',
							emailRegistro: '',
							senhaRegistro: '',
							niverRegistro: '',
							celRegistro: ''
						}
						this.progressLinear = false
						this.step = 5
					}
				})
			},
			displaySaveDate (date) {
				var split = date.split("-")
				var reversed = split.reverse()
				var datereverse = reversed.join("-")
				this.date = datereverse
				this.$refs.menu.save(datereverse)
			},
			doLogin() {
				const dataLogin = {
					email: this.emailLogin,
					password: this.senhaLogin
				}
				this.progressLinear = true
				this.error_message = ""
				axios.post("http://localhost:5000/api/login/", dataLogin)
				.then((response) => {
					this.progressLinear = false
					console.log(response.data)
					if(response.data.id){
						this.$session.set('name', response.data.name)
						this.$session.set('email', response.data.email)
						this.$session.set('id_user', response.data.id)
						this.$session.start()
						this.$router.push(APP_ROUTERS.panel)
						
					}
				})
				.catch(()=> {
					this.progressLinear = false
					this.error_message = "Email ou Senha inválido."
				})
			}
		}

	}


	</script>