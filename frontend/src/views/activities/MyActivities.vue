<template>
	<div class="primary pt-15 pb-10 px-7" style="width: 100%; height: 100%;">
		<h1>Résultats</h1>

		<div class="d-flex flex-column align-center">
			<div v-for="(value, index) in activities" :key="index" style="width: 100%;">
				<card-edit-activity class="mx-auto my-2" :activity="value"></card-edit-activity>
			</div>
		</div>
	</div>
</template>

<script>
//import axios from "axios";
import CardEditActivity from '../../components/activities/CardEditActivity.vue';

export default {
  components: { CardEditActivity },
	name: 'SearchResults',
	data() {
		return {
			activities: [],
		}
	},
	computed: {
		url() {
			// TODO request API with $route.query.radius, $route.query.center.lat, $route.query.center.lng  
			return "https://jsonplaceholder.typicode.com/posts?_page=" + this.page;
		}
	},
	mounted()
	{
		this.fetchUserActivities()
	},

	methods:
    {
		async fetchUserActivities()
		{
			try
			{
				var response = await this.$store.dispatch('fetchUserActivities')
				this.activities = response.data.activities;
			}
			catch(error)
			{
				//Rien
			}
            
		},
	}
}
</script>

<style>

</style>