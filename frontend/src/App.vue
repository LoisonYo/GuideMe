<template>
	<v-app>
		<TheHeader/>
		<v-main>
			<v-container fluid fill-height class="pa-0">
				<router-view></router-view>
			</v-container>
		</v-main>
  </v-app>
</template>

<script>
import TheHeader from './components/TheHeader.vue';

export default {
	name: 'App',
	components: {
		TheHeader,
	},
	data: () => ({
		//
	}),
};
</script>

<style>
#app {
	background-color: transparent;
}

a {
	text-decoration: none;
}
</style>
