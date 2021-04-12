<template>
  <base-container-login v-bind:link="{ name: 'Se connecter', route: 'Login'}">
		<v-form @submit.prevent="register" v-model="valid" class="mt-5">	
			<v-text-field v-model="name" label="Nom" required 
				:rules="nameRules"
				color="accent">
			</v-text-field>

			<v-text-field v-model="email" label="E-mail" required
				:rules="emailRules"
				color="accent">
			</v-text-field>
			
			<v-text-field v-model="password" label="Mot de passe" type="password" required
				:rules="passwordRules"
				color="accent">
			</v-text-field>

			<v-text-field v-model="confirmPassword" label="Confirmer mot de passe" type="password" required 
				:rules="passwordRules.concat(passwordConfirmationRule)"
				color="accent">
			</v-text-field>

			<ul class="warning--text body-2 my-3">
				<li v-for="(value, index) in errors" :key="index">{{ value }}</li>
			</ul>
			
			<v-btn :disabled="!valid" type="submit"
				rounded color="accent" elevation="0" class="my-7">
				S'inscrire
			</v-btn>
		</v-form>
	</base-container-login>
</template>

<script>
import BaseContainerLogin from '@/components/users/BaseContainerLogin.vue';

export default {
	name: "Register",
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
			email: "",
			emailRules: [
				v => !!v || "E-mail requis",
				v => /.+@.+\..+/.test(v) || "L'e-mail doit être valide",
			],
			password: "",
			passwordRules: [
				v => !!v || "Mot de passe requis",
			],
			confirmPassword: "",
			confirmRules: [

			],
			display_error: false,
			errors: []
		}
	},
	computed: {
		passwordConfirmationRule() {
			return this.password === this.confirmPassword || "Password must match";
		}
	},
	methods: {
		register()
		{
			this.$store.dispatch("register", {
				name: this.name,
				email: this.email,
				password: this.password,
				password_confirmation: this.confirmPassword,
			})
			.then(() => {
				this.$router.push({name:"Login"})
			})
			.catch(error => {
				this.errors = Object.values(error.response.data).flat();
			})
		},
	}
}
</script>

<style>

</style>