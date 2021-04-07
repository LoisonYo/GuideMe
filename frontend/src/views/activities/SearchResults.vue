<template>
	<div>
		<h1>Search</h1>
		<div v-for="activity in activities" :key="activity" style="z-index:10;">
			<router-link :to="{ name: 'ActivityDetails', params: { id: activity }}">{{ activity }}</router-link>
		</div>
	</div>
</template>

<script>
export default {
	name: 'SearchResults',
	data() {
		return {
			radius: 4000,
			activities: ["Tennis", "Musée"],
		}
	}
}
</script>

<style>

</style>