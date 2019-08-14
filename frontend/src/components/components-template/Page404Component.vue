<template>
	<div>
		<v-icon class="notfound-icon">fas fa-frown</v-icon>
		<v-flex class="notfound-message"> 
			Página não encontrada. Tente em outro lugar.
		</v-flex>
		<v-flex>
			<button @click="backRouter()">Voltar</button>
		</v-flex>
	</div>	
</template>

<style type="text/css">
	.theme--light.v-icon.notfound-icon{
		font-size: 25em;
		color: #00b9b4;
		margin-bottom: 35px;
	}
	.notfound-message{
		font-size: 3em;
		text-transform: uppercase;
	}
</style>

<script type="text/javascript">
export default {
	name: "Page404",
	methods: {
		backRouter(){
			this.$router.push('/')
		}
	}

}
</script>

