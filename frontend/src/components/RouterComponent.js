import Vue from 'vue'
import VueRouter from 'vue-router'

import Painel from './components-routes/PainelRouterComponent.vue';
import Login from './components-routes/LoginRouterComponent';
import Page404 from './components-routes/Page404Component';

Vue.use(VueRouter)

const router_components = [
{ path: '/login', component: Login},
{ path: '/painel', component: Painel },    
{ path: '/', redirect: '/painel' },
{ path: '*', component:  Page404 },
];


export default new VueRouter({mode: 'history', routes: router_components})