import Vue from 'vue'
import VueRouter from 'vue-router'

import Panel from './components-routes/PanelRouterComponent';
import Login from './components-routes/LoginRouterComponent';
import Monitoring from './components-routes/MonitoringRouterComponent';
import MonitoringSearch from './components-routes/MonitoringSearchRouterComponent';
import Page404 from './components-routes/Page404RouterComponent';
import Reports from './components-routes/ReportsRouterComponent'
import Monitor from './components-routes/MonitorRouterComponent'
import {APP_ROUTERS} from './constants.js'

Vue.use(VueRouter)

const router_components = [
{ path: APP_ROUTERS.login, component: Login},
{ path: APP_ROUTERS.panel, component: Panel},    
{ path: APP_ROUTERS.notFound, component:  Page404 },
{ path: APP_ROUTERS.monitor, component:  Monitor },
{ path: APP_ROUTERS.base, redirect: APP_ROUTERS.panel },
{ path: `${APP_ROUTERS.monitoring}`, component: MonitoringSearch},
{ path: `${APP_ROUTERS.monitoring}/:monitorToken`, component: Monitoring, props:true},
{ path: `${APP_ROUTERS.reports}`, component: Reports},
{ path: `${APP_ROUTERS.reports}/:typeReports`, component: Reports, props:true},
];


export default new VueRouter({mode: 'history', routes: router_components})

