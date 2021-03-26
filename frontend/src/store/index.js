import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios'

Vue.use(Vuex);
axios.defaults.baseURL = "http://localhost:8000/api";

export default new Vuex.Store({
	state:
	{
		activities: [],
	},

	mutations:
	{
		
	},

	actions: {
		register(context, data)
		{
			return new Promise((resolve, reject) => {
				axios.post("/users", {
					name: data.name,
					email: data.email,
					password: data.password,
					password_confirmation: data.password_confirmation,
				})
				.then(response => {
					console.log(response)
					//resolve(response)
				})
				.catch(error => {
					reject(error)
				})
			})
		},
	},
	modules: {},
});
