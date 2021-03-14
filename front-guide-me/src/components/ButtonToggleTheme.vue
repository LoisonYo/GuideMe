<template>

	<!-- See: https://stackoverflow.com/questions/62005958/vuetify-toggle-between-light-and-dark-theme-with-vuex  -->
	<div>
		<v-tooltip v-if="$vuetify.theme.dark" bottom>
			<template v-slot:activator="{ on }">
				<v-btn v-on="on" @click="toggleTheme" :color="colorDark" small fab elevation="0">
					<v-icon :color="colorLight">
						mdi-moon-waxing-crescent
					</v-icon>
				</v-btn>
			</template>
			<span>Dark Mode On</span>
		</v-tooltip>
		<v-tooltip v-else bottom>
			<template v-slot:activator="{ on }">
				<v-btn v-on="on" @click="toggleTheme" :color="colorLight" small fab elevation="0">
					<v-icon :color="colorDark">mdi-white-balance-sunny</v-icon>
				</v-btn>
			</template>
			<span>Dark Mode Off</span>
		</v-tooltip>
	</div>
</template>

<script>
import colors from 'vuetify/lib/util/colors'

export default {
	name: "ButtonToggleTheme",
	props: {
		colorLight: {
			type: String,
			default: colors.grey.lighten4,
		},
		colorDark: {
			type: String,
			default: colors.grey.darken4,
		},
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