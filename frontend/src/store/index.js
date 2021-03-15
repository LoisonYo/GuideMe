import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios'

Vue.use(Vuex);
axios.defaults.baseURL = "http://localhost:8000";

export default new Vuex.Store({
	state:
	{
		activities: [],
	},

	mutations:
	{
		
	},

	actions: {},
	modules: {},
});
