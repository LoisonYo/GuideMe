import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
axios.defaults.baseURL = "" //TODO Lien backend

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('access_token') || null,
    authUser: null,
    users: [],
    coffee_counter: 0,
  },
  getters: {
    orderedUsers(state) {
      return state.users.sort((a, b) => (a.coffee_counter < b.coffee_counter) ? 1 : -1)
    },
    loggedIn(state) {
      return state.token != null
    }
  },
  mutations: {
    retrieveToken(state, token) {
      state.token = token
    },
    destroyToken(state) {
      state.token = null
    },
  },
  actions: {
  },
  modules: {
  }
})
