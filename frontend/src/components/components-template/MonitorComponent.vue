<template>
	<v-flex xs12 sm12 md11 lg11 >
		<v-toolbar flat color="white">
			<v-toolbar-title>Monitores</v-toolbar-title>
			<v-spacer></v-spacer>
			<v-dialog v-model="dialog" max-width="500px">
				<template v-slot:activator="{ on }">
					<v-btn color="primary" dark class="mb-2" v-on="on">Cadastrar</v-btn>
				</template>
				<template>
					<v-card class="elevation-12">
						<v-toolbar dark color="primary">
							<v-toolbar-title>{{formTitle}}</v-toolbar-title>
							<v-spacer></v-spacer>
						</v-toolbar>
						<template>
							<v-window>
								<v-window-item>
									<v-card-text>
										<v-container grid-list-md>
											<v-layout wrap>
												<v-flex xs12 sm12 md12>
													<v-text-field v-model="editedItem.name" label="Nome"></v-text-field>
												</v-flex>
												<v-flex xs12 sm12 md12>
													<v-text-field v-model="editedItem.email" label="Email"></v-text-field>
												</v-flex>
												<v-flex xs12 sm12 md12>
													<v-text-field v-model="editedItem.telephone" label="Telefone"></v-text-field>
												</v-flex>
											</v-layout>
										</v-container>
									</v-card-text>
								</v-window-item>
							</v-window>

							<v-divider></v-divider>

							<v-card-actions>
								<v-spacer></v-spacer>
								<v-btn color="blue darken-1" flat @click="close">Cancelar</v-btn>
								<v-btn color="blue darken-1" flat @click="save">Salvar</v-btn>
							</v-card-actions>
						</template>						
					</v-card>
				</template>
			</v-dialog>
		</v-toolbar>
		<v-data-table
		:headers="headers"
		:items="desserts"
		:rows-per-page-items=this.qtdPages
		class="elevation-1"
		rows-per-page-text="Itens por página"
		no-data-text="Sem cadastro no momento"		
		>
		<template v-slot:items="props">
			<td class="text-xs-center">{{ props.item.name }}</td>
			<td class="text-xs-center">{{ props.item.email }}</td>
			<td class="text-xs-center">{{ props.item.telephone }}</td>
			<td class="justify-center layout px-0">
				<v-icon
				small
				class="mr-2"
				@click="editItem(props.item)"
				>
				edit
			</v-icon>
			<v-icon
			small
			@click="deleteItem(props.item)"
			>
			delete
		</v-icon>
	</td>
</template>
</v-data-table>
	<v-progress-linear :indeterminate="true" :active="progressLinear"></v-progress-linear>
</v-flex>
</template>

<style type="text/css">
.monitoring-search{
	padding: 20px !important;
}
.v-progress-linear {
    margin: 0px;
}
</style>

<script type="text/javascript">
import axios from 'axios';
export default {
	data: () => ({
		dialog: false,
		headers: [
		{
			text: 'Nome',
			align: 'center',
			sortable: false,
			value: 'name'
		},
		{ 
			text: 'Email', 
			value: 'email', 
			align: 'center',
			sortable: false,
		},
		{ text: 'Celular', value: 'telephone', align: 'center', sortable: false },
		{ text: 'Ações', value: 'actions', align: 'center', sortable: false }
		],
		desserts: [],
		editedIndex: -1,
		editedItem: {
		},
		defaultItem: {
		},
		progressLinear: false
	}),
	props: {
		qtdPages: {
			type: Array,
			default: ()=>{ return [5,10, {"text":"Todos","value":-1}]}
		}
	},

	computed: {
		formTitle () {
			return this.editedIndex === -1 ? 'Novo Monitor' : 'Editar Monitor'
		}
	},

	watch: {
		dialog (val) {
			val || this.close()
		}
	},

	created () {
		this.initialize()
		this.progressLinear = false
	},
	mounted(){
		this.getAllMonitors()
	},
	methods: {
		getAllMonitors(){
			axios.get("http://localhost:5000/api/monitor/"+this.$session.get('id_user'))
			.then((response) => {
				if(response.data.length > 0){
					this.desserts = response.data
					this.progressLinear = false
				}
			})
			.catch(()=> {
				this.progressLinear = false
				this.error_message = "Erro ao carregar monitores."
			})
		},

		editItem (item) {
			this.editedIndex = this.desserts.indexOf(item)
			this.editedItem = Object.assign({}, item)
			this.dialog = true
		},

		deleteItem (item) {
			const index = this.desserts.indexOf(item)
			this.progressLinear = true
			if(confirm('Tem certeza que deseja deletar o monitor?')){
				axios.delete("http://localhost:5000/api/monitor/"+item.id)
				.then((response) => {					
					if(response.data.msg){
						this.desserts.splice(index, 1)
						this.progressLinear = false
					}
				})
				.catch(()=> {
					this.progressLinear = false
					this.error_message = "Erro ao Deletar Monitor"
				})				
			}
		},

		close () {
			this.dialog = false
			setTimeout(() => {
				this.editedItem = Object.assign({}, this.defaultItem)
				this.editedIndex = -1
			}, 300)
		},

		save () {
			if (this.editedIndex > -1) {
				Object.assign(this.desserts[this.editedIndex], this.editedItem)
			    var userEdited = {
			    	idMonitor: this.desserts[this.editedIndex].id,
			    	name: this.desserts[this.editedIndex].name,
			    	email: this.desserts[this.editedIndex].email,
			    	telephone: this.desserts[this.editedIndex].telephone
			    }
			    console.log(userEdited)
				axios.put("http://localhost:5000/api/monitor/"+userEdited.idMonitor, userEdited)
				.then((response) => {
					console.log(response.data)
					if(!response.data.user.is_loggedin){
						console.log(response.data)
						this.$session.destroy()
						this.$router.push(APP_ROUTERS.login)         
					}
				})
				.catch(()=> {
					this.progressLinear = false
					this.error_message = "Erro ao editar monitor."
				})
			} else {
				this.progressLinear = true
				var createUser = {
					name: this.editedItem.name,
					email:this.editedItem.email,
					telephone: this.editedItem.telephone,
					id_user: this.$session.get('id_user')
				}
				axios.post("http://localhost:5000/api/monitor/", createUser)
				.then((response) => {
					console.log(response.data)
					if(response.data.id_monitor){
						this.getAllMonitors()     
					}
				})
				.catch(()=> {
					this.progressLinear = false
					this.error_message = "Erro ao salvar monitor."
				})
			}
			this.close()
		}
	}
}
</script>