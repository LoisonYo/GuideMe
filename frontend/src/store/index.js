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
			return new Promise((resolve, reject) => {
				axios.post("users/", {
					username: data.name,
					email: data.email,
					password: data.password,
				})
				.catch(error => {
					reject(error)
				})
			})
		},
	},
	modules: {},
});
