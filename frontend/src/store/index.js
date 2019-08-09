import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


const ModuleSession = {
    state: {existSession: true, tokenSession: '123123123'},
    mutations: {
        changeSession(state) {
            state.existSession = true
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