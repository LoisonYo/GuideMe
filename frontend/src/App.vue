<template>
	<v-app>
		<TheHeader />
		<v-main>
			<v-container fluid fill-height class="pa-0">
				<router-view></router-view>
			</v-container>
		</v-main>
		<TheFooter />
  </v-app>
</template>

<script>
import TheFooter from './components/TheFooter.vue';
import TheHeader from './components/TheHeader.vue';

export default {
	name: 'App',
	components: {
		TheHeader,
		TheFooter,
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
