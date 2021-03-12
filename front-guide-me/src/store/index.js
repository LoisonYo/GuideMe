import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios'

Vue.use(Vuex);
axios.defaults.baseURL = ""; // Link to backend

export default new Vuex.Store({
	state: {},
	mutations: {},
	actions: {},
	modules: {}
});
