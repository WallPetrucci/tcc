import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import VueRouter from 'vue-router'
import VueSocketio from 'vue-socket.io';
import Vuetify from 'vuetify'
import io from 'socket.io-client';
import router_components from './components/RouterComponent.js'

// Helpers
import colors from 'vuetify/es5/util/colors'


const SocketInstance = io.connect('http://localhost:5000');

Vue.use(new VueSocketio({
	debug: false, 
	connection: SocketInstance
}))
Vue.use(VueRouter)
Vue.use(Vuetify,{
	theme: {
		primary: colors.teal.lighten2
	},
	iconfont: 'fas'
})

const router = new VueRouter({routes: router_components, mode: 'history'});


Vue.config.productionTip = false
new Vue({
	router,
	render: h => h(App),	
}).$mount('#app')
