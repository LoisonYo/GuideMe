<template>
	<div>
		<h1>Ah</h1>
		<div v-for="activity in activities" :key="activity" >
			<router-link :to="{ name: 'ActivityDetails', params: { id: activity }}">{{ activity }}</router-link>
		</div>
		
	</div>
</template>

<script>
export default {
	data() {
		return {
			activities: ["Tennis", "Musée"],
		}
	},
}
</script>

<style>

</style>