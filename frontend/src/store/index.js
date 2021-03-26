import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios'

Vue.use(Vuex);
axios.defaults.baseURL = "http://localhost:8000/api/";

export default new Vuex.Store({
	state:
	{
		activities: [],
	},

	mutations:
	{
		
	},

	actions: {
		async register(context, data)
		{
			return axios.post("users/", {
				username: data.name,
				email: data.email,
				password: data.password,
			})
		},
	},
	modules: {},
});
