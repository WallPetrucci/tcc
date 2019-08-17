<template>
	<v-flex xs12 sm12 md11 lg11 >
		<v-toolbar flat color="white">
			<v-toolbar-title>Monitores</v-toolbar-title>
			<v-spacer></v-spacer>
			<v-dialog v-model="dialog" max-width="500px">
				<template v-slot:activator="{ on }">
					<v-btn color="primary" dark class="mb-2" v-on="on">Cadastrar</v-btn>
				</template>
				<v-card>
					<v-card-title>
						<span class="headline">{{ formTitle }}</span>
					</v-card-title>

					<v-card-text>
						<v-container grid-list-md>
							<v-layout wrap>
								<v-flex xs12 sm6 md4>
									<v-text-field v-model="editedItem.nome" label="Nome"></v-text-field>
								</v-flex>
								<v-flex xs12 sm6 md4>
									<v-text-field v-model="editedItem.email" label="Email"></v-text-field>
								</v-flex>
								<v-flex xs12 sm6 md4>
									<v-text-field v-model="editedItem.tel" label="Telefone"></v-text-field>
								</v-flex>
								<v-flex xs12 sm6 md4>
									<v-text-field v-model="editedItem.cel" label="Celular"></v-text-field>
								</v-flex>
							</v-layout>
						</v-container>
					</v-card-text>

					<v-card-actions>
						<v-spacer></v-spacer>
						<v-btn color="blue darken-1" flat @click="close">Cancelar</v-btn>
						<v-btn color="blue darken-1" flat @click="save">Salvar</v-btn>
					</v-card-actions>
				</v-card>
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
			<td class="text-xs-center">{{ props.item.nome }}</td>
			<td class="text-xs-center">{{ props.item.email }}</td>
			<td class="text-xs-center">{{ props.item.tel }}</td>
			<td class="text-xs-center">{{ props.item.cel }}</td>
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
</v-flex>
</template>

<style type="text/css">
.monitoring-search{
	padding: 20px !important;
}
</style>

<script type="text/javascript">
export default {
	data: () => ({
		dialog: false,
		headers: [
		{
			text: 'Nome',
			align: 'center',
			sortable: false,
			value: 'nome'
		},
		{ 
			text: 'Email', 
			value: 'email', 
			align: 'center',
			sortable: false,
		},
		{ text: 'Telefone', value: 'tel', align: 'center', sortable: false },
		{ text: 'Celular', value: 'cel', align: 'center', sortable: false },
		{ text: 'Ações', value: 'actions', align: 'center', sortable: false }
		],
		desserts: [],
		editedIndex: -1,
		editedItem: {
		},
		defaultItem: {
		}
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
	},

	methods: {
		initialize () {
			this.desserts = [
			{
				nome: 'Wallace P Neves',
				email: 'wallacep@gmaiu.com',
				tel: 35353535,
				cel: 89279399
			},
			{
				nome: 'Higao da Silva',
				email: 'higaoss@gmaiu.com',
				tel: 123123123,
				cel: 123123123
			}
			]
		},

		editItem (item) {
			this.editedIndex = this.desserts.indexOf(item)
			this.editedItem = Object.assign({}, item)
			this.dialog = true
		},

		deleteItem (item) {
			const index = this.desserts.indexOf(item)
			confirm('Tem certeza que deseja deletar o monitor?') && this.desserts.splice(index, 1)
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
			} else {
				this.desserts.push(this.editedItem)
			}
			this.close()
		}
	}
}
</script>