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
							<v-text-field prepend-icon="person" name="login" label="Email" type="text"></v-text-field>
							<v-text-field id="password" prepend-icon="lock" name="password" label="Senha" type="password"></v-text-field>
						</v-form>
					</v-card-text>
					<v-card-actions>
						<v-spacer></v-spacer> 
						<v-btn color="primary" class="esqueceusenha">
							Esquecer Senha <v-icon>fas fa-question</v-icon>
						</v-btn>
						<v-btn color="primary">Acessar</v-btn>
					</v-card-actions>
				</v-window-item>
				<v-window-item :value="2">
					<v-card-text>
						<v-text-field
						label="Email"
						value=""
						></v-text-field>
					</v-card-text>
				</v-window-item>

				<v-window-item :value="3">
					<v-card-text>
						<v-text-field
						label="Senha"
						type="password"
						></v-text-field>
						<v-text-field
						label="Confirmar Senha"
						type="password"
						></v-text-field>
						<span class="caption grey--text text--darken-1">
							Entre com sua senha
						</span>
					</v-card-text>
				</v-window-item>

				<v-window-item :value="4">
					<div class="pa-3 text-xs-center">
						<v-icon>fas fa-check-circle</v-icon>
						<h3 class="title font-weight-light mb-2">Seja bem vindo!</h3>
						<span class="caption grey--text">Cadastro efetuado com sucesso</span>
					</div>
				</v-window-item>

				<v-window-item :value="5">
					<div class="pa-3 text-xs-center">
						<v-icon>fas fa-check-circle</v-icon>
						<h3 class="title font-weight-light mb-2">Seja bem vindo!</h3>
						<span class="caption grey--text">Cadastro efetuado com sucesso</span>
					</div>
				</v-window-item>
			</v-window>

			<v-divider></v-divider>

			<v-card-actions v-if="step > 1">
				<v-btn
				:disabled="step === 1 || step === 4"
				flat
				@click="step--"
				>
				Voltar
			</v-btn>
			<v-spacer></v-spacer>
			<v-btn
			:disabled="step === 3"
			color="primary"
			depressed
			@click="step++"
			v-if="step !== 3"
			>
			Avançar
		</v-btn>
		<v-btn		
		color="primary"
		@click="registerUser()"
		v-else
		>
		Cadastrar
	</v-btn>
</v-card-actions>
</template>
</v-card>	
</template>
<script type="text/javascript">
	
	export default {
		name: "LoginComponent",
		data: () => ({
			step: 1,
			displayRegister: false
		}),
		mounted(){
			this.displayRegister = false
		},
		computed: {
			currentTitle () {
				switch (this.step) {
					case 1: return 'Painel de Acesso'
					case 2: return 'Registrar'
					case 3: return 'Registrar'
					default: return 'Registrado com Sucesso'
				}
			}
		},
		methods : {
			displayRegisterMethod() {
				this.step = 2
				this.displayRegister = true
			},
			registerUser() {
				this.step = 4
			}
		}

	}


</script>