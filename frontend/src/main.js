import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import VueRouter from 'vue-router'
import VueSocketio from 'vue-socket.io';
import io from 'socket.io-client';
import router_components from './components/RouterComponent.js'


const SocketInstance = io.connect('http://localhost:5000');

Vue.use(new VueSocketio({
    debug: false, 
    connection: SocketInstance
}))
Vue.use(VueRouter)


const router = new VueRouter({routes: router_components, mode: 'history'});


Vue.config.productionTip = false
new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
