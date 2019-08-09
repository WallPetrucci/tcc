<template>
	<v-content>
		<Header />
		<v-container fluid fill-height>
			<v-layout justify-start>
				<v-flex text-xs-center>
					<v-layout row align-baseline align-start>
						<div>
							{{content}}
						</div>
					</v-layout>
				</v-flex>
			</v-layout>
		</v-container>
	</v-content>	
</template>

<script type="text/javascript">
	import Header from "../components-template/HeaderComponent"
	export default {
		name: "Painel",
		components: {
			Header
		},
		beforeCreate: function () {
			if (!this.$session.exists()) {
				this.$router.push('/login')
			}
		},
		data() {
			return{
				content: "Home Page"
			}
		},
		mounted() {
			alert("Montou "+this.content);
		}
	}
	
	
</script>