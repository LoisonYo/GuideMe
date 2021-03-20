<template>
	<div style="height:100%; width:100%;">
		<TheBackground/>
		
		<h1 class="display-2 text-center mt-5
			grey--text text--lighten-4 font-weight-regular">
			Guide Me
		</h1>

		<v-card color="primary" 
			max-width="400px"
			style="width: calc(100% - 104px);" 
			class="mt-7 mb-16 mx-auto pa-12 rounded-xl text-center">

			<v-form @submit.prevent="login" ref="form" class="mt-5">
				<v-text-field v-model="name" label="Nom" required 
					color="accent">
				</v-text-field>
				
				<v-text-field v-model="password" label="Mot de passe" type="password" required 
					color="accent">
				</v-text-field>

				<p v-show="display_error" class="warning--text body-2 my-3">L'adresse mail et/ou le mot de passe sont incorrects !</p>
				
				<v-btn :disabled="!valid" type="submit"
					rounded color="accent" elevation="0" class="my-7">
					Se connecter
				</v-btn>
			</v-form>

			<v-row align="center">
				<v-divider class="mr-5"></v-divider>
					or
				<v-divider class="ml-5"></v-divider>
			</v-row>

			<div class="mt-7 mb-5">
				<router-link :to="{ name: 'Register' }" class="accent--text">
					Créer un compte
				</router-link>
			</div>
		</v-card>
	</div>
</template>

<script>
import TheBackground from '@/components/TheBackground.vue';

export default {
	name: "Login",
	components: {
		TheBackground,
	},
	data() {
		return {
			name: "",
			password: "",
			display_error: false,
		}
	},
	computed: {
		valid () {
			return (
				this.name && this.password
			)
		},
  },
	methods: {
		login() {
			
		}
	}
}
</script>

<style>

</style>