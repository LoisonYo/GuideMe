<template>

	<!-- See: https://stackoverflow.com/questions/62005958/vuetify-toggle-between-light-and-dark-theme-with-vuex  -->
	<div>
		<v-tooltip v-if="$vuetify.theme.dark" bottom>
			<template v-slot:activator="{ on }">

				<v-btn v-on="on" @click="toggleTheme" color="primary" small fab elevation="0">
					<v-icon color="secondary">{{ dark.icon }}</v-icon>
				</v-btn>

			</template>
			<span>{{ dark.tooltip }}</span>
		</v-tooltip>

		<v-tooltip v-else bottom>
			<template v-slot:activator="{ on }">

				<v-btn v-on="on" @click="toggleTheme" color="primary" small fab elevation="0">
					<v-icon color="secondary">{{ light.icon }}</v-icon>
				</v-btn>

			</template>
			<span>{{ light.tooltip }}</span>
		</v-tooltip>
	</div>
</template>

<script>

export default {
	name: "ButtonToggleTheme",
	data() {
		return {
			light: {
				icon: "mdi-white-balance-sunny",
				tooltip: "Dark Mode Off",
			},
			dark: {
				icon: "mdi-moon-waxing-crescent",
				tooltip: "Dark Mode On",
			},
		}
	},
	methods: {
		toggleTheme() {
			this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
		}
	},
}
</script>

<style>

</style>