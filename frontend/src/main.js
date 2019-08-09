import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import VueRouter from 'vue-router'
import VueSocketio from 'vue-socket.io';
import Vuetify from 'vuetify'
import io from 'socket.io-client';
import router from './components/RouterComponent.js'
import VueSession from 'vue-session'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'
import store from './store'



// Helpers
import colors from 'vuetify/es5/util/colors'
const SocketInstance = io.connect('http://localhost:5000');

Vue.use(new VueSocketio({
	debug: false, 
	connection: SocketInstance
}))
Vue.use(Vuetify,{
	theme: {
		primary: colors.teal.lighten2
	},
	iconfont: 'fas'
})
Vue.use(VueSession)
Vue.use(Vuex)
Vue.use(VueRouter)
Vue.use(VueAxios, axios)
Vue.config.productionTip = false
new Vue({
	router,
	store,
	render: h => h(App),	
}).$mount('#app')
