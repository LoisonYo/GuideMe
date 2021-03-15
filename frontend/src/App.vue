<template>
	<v-app>
		<TheHeader/>
		<v-main>
			<v-container fluid class="pa-0">
				<router-view></router-view>
			</v-container>
		</v-main>
  </v-app>
</template>

<script>
import TheHeader from './components/TheHeader.vue';

export default {
	name: 'App',
	components:
	{
		TheHeader,
	},
	data: () => ({
		//
	}),
};
</script>

<style scoped>
#app {
	background-color: transparent;
}
</style>
