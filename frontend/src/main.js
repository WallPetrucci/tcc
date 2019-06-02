import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import VueRouter from 'vue-router'
import VueSocketio from 'vue-socket.io';
import io from 'socket.io-client';

const SocketInstance = io.connect('http://localhost:5000');

Vue.use(new VueSocketio({
	debug: true, 
	connection: SocketInstance
}))

Vue.config.productionTip = false
Vue.use(VueRouter)

new Vue({
  render: h => h(App),
}).$mount('#app')
