import Vue from 'vue'
import VueRouter from 'vue-router'

import Painel from './components-routes/PainelRouterComponent.vue';
import Login from './components-routes/LoginRouterComponent';
import Page404 from './components-routes/Page404Component';
import store from '../store';

Vue.use(VueRouter)

const router_components = [
{ path: '/login', component: Login, beforeEnter: (to, from, next) => {
	userSession = this.$session.get('user_session')
	if(userSession){	
		next('/painel')
	}else{
		next('/login')	
	}
} },
{ path: '/painel', component: Painel, beforeEnter: (to, from, next) => {
	if(store.getters.hasSession && store.getters.getTokenSession.length !== 0){	
		next('/painel')
	}else{
		next('/login')	
	}
}},    
{ path: '/', redirect: '/painel'},
{ path: '*', component:  Page404 },
];


export default new VueRouter({mode: 'history', routes: router_components})