<template>
	<base-container-login v-bind:link="{ name: 'Créer un compte', route: 'Register'}">
		<v-form @submit.prevent="login" v-model="valid" class="mt-5">	
			<v-text-field v-model="name" label="Nom" required 
				:rules="nameRules"
				color="accent">
			</v-text-field>
			
			<v-text-field v-model="password" label="Mot de passe" type="password" required 
				:rules="passwordRules"
				color="accent">
			</v-text-field>

			<p v-show="display_error" class="warning--text body-2 my-3">L'adresse mail et/ou le mot de passe sont incorrects !</p>
			
			<v-btn :disabled="!valid" type="submit"
				rounded color="accent" elevation="0" class="my-7">
				Se connecter
			</v-btn>
		</v-form>
	</base-container-login>
</template>

<script>
import BaseContainerLogin from '@/components/users/BaseContainerLogin.vue';

export default {
	name: "Login",
	components: {
		BaseContainerLogin,
	},
	data() {
		return {
			valid: false,
			name: "",
			nameRules: [
				v => !!v || "Nom requis",
			],
			password: "",
			passwordRules: [
				v => !!v || "Mot de passe requis",
			],
			display_error: false,
		}
	},
	methods: {
		login()
		{
			this.$store.dispatch("login", {
				username: this.name,
				password: this.password,
			})
			.then(() => {
				//TODO Redirection
				console.log(this.$store.state.user);
				//this.$router.push({name:"Home"})
			})
			.catch(error => {
				console.log(Object.values(error.response.data).flat());
			})
		}
	}
}
</script>

<style>

</style>