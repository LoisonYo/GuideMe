<template>

	<!-- See: https://stackoverflow.com/questions/62005958/vuetify-toggle-between-light-and-dark-theme-with-vuex  -->
	<div>
		<v-tooltip v-if="$vuetify.theme.dark" bottom>
			<template v-slot:activator="{ on }">

				<v-btn v-on="on" @click="toggleTheme" :color="dark.color" small fab elevation="0">
					<v-icon :color="dark.iconColor">{{ dark.icon }}</v-icon>
				</v-btn>

			</template>
			<span>{{ dark.tooltip }}</span>
		</v-tooltip>

		<v-tooltip v-else bottom>
			<template v-slot:activator="{ on }">

				<v-btn v-on="on" @click="toggleTheme" :color="light.color" small fab elevation="0">
					<v-icon :color="light.iconColor">{{ light.icon }}</v-icon>
				</v-btn>

			</template>
			<span>{{ light.tooltip }}</span>
		</v-tooltip>
	</div>
</template>

<script>
import colors from 'vuetify/lib/util/colors'

export default {
	name: "ButtonToggleTheme",
	data() {
		return {
			light: {
				color: colors.grey.lighten4,
				icon: "mdi-white-balance-sunny",
				iconColor: colors.grey.darken4,
				tooltip: "Dark Mode Off",
			},
			dark: {
				color: colors.grey.darken4,
				icon: "mdi-moon-waxing-crescent",
				iconColor: colors.grey.lighten4,
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