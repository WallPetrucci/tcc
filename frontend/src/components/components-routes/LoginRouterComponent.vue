<style scoped src="@/assets/LoginPageComponent.css"></style>
<template>
		<v-container fluid fill-height>
			<v-layout align-center justify-center>
				<v-flex xs12 sm8 md4>
					<img src="/img/logotcc.png" class="logo_login">
					<LoginComponent />
				</v-flex>
			</v-layout>
		</v-container>
</template>

<script type="text/javascript">
	import LoginComponent from '../components-template/LoginComponent.vue'

	export default {
		name: "Login",
		components: {
			LoginComponent
		}
	}


</script>