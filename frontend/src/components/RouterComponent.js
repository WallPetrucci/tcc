import Home from './components-routes/HomeRouterComponent.vue';
import Register from './components-routes/RegisterRouterComponent';
import Login from './components-routes/LoginRouterComponent';
import Page404 from './components-routes/Page404Component';

const router_components = [
    { path: '/', component: Home },
    { path: '/register', component: Register },
    { path: '/login', component: Login },
    { path: '*', component:  Page404 },
];


export default router_components;