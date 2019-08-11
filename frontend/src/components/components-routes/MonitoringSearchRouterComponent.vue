<template>
	<v-content>
		<v-container fluid fill-height>
			<Header v-if="this.headerShow"></Header>
			<v-layout align-center justify-center>
				<v-flex xs12 sm8 md4>
					<MonitoringSearch> </MonitoringSearch>
				</v-flex>
			</v-layout>
		</v-container>
	</v-content>
</template>

<script type="text/javascript">
import MonitoringSearch from '../components-template/MonitoringSearchComponent'
import Header from '../components-template/HeaderComponent'
export default {
	name: "MonitoringSearchRouter",
	components: {
		MonitoringSearch,
		Header,
	},
	data(){
		return {
			headerShow: false
		}
	},
	beforeMount(){
		if (this.$session.exists()) {
			this.headerShow = true
		}	
	}
}
</script>