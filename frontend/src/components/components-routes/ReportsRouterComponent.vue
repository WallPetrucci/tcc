<template>
	<v-content>
		<Header></Header>
		<v-container fluid fill-height>
			<v-layout justify-start>
				<v-flex text-xs-center>
					<v-layout row align-baseline align-start>
						<ReportsComponents> </ReportsComponents>
					</v-layout>
				</v-flex>
			</v-layout>
		</v-container>
	</v-content>
</template>

<script type="text/javascript">
import ReportsComponents from '../components-template/ReportsComponent'
import Header from '../components-template/HeaderComponent'

export default {
	name: "ReportsRouter",
	components: {
		ReportsComponents,
		Header
	},
	beforeCreate: function () {
		if (!this.$session.exists()) {
			this.$router.push(APP_ROUTERS.login)
		}
	},
}

</script>