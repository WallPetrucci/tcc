import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


const ModuleSession = {
    state: {existSession: false, tokenSession: ''},
    mutations: {
        changeSession(state, payload) {
            if(payload){
                state.existSession = true
                state.tokenSession = payload
            }
        }
    },
    getters: {
        hasSession(state) {
            return state.existSession
        },
        getTokenSession(state) {
            return state.tokenSession
        }
    }
}

export default new Vuex.Store({
  modules: {
    authSession: ModuleSession
  },
})