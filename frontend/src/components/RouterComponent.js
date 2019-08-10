import Vue from 'vue'
import VueRouter from 'vue-router'

import Panel from './components-routes/PanelRouterComponent';
import Login from './components-routes/LoginRouterComponent';
import Monitoring from './components-routes/MonitoringRouterComponent';
import Page404 from './components-routes/Page404Component';

Vue.use(VueRouter)

const router_components = [
{ path: '/', redirect: '/painel' },
{ path: '/monitoring/:monitorToken', component: Monitoring, props:true},
{ path: '/login', component: Login},
{ path: '/panel', component: Panel},    
{ path: '*', component:  Page404 },
];


export default new VueRouter({mode: 'history', routes: router_components})