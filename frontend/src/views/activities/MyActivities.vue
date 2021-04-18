<template>
	<div class="primary pt-15 pb-10 px-7" style="width: 100%; height: 100%;">
		<v-sheet max-width="600px" class="transparent mx-auto">

			<h2 class="display-1 secondary--text my-5">Mes activités</h2>
			
			<div class="d-flex flex-column align-center mt-5">
				<div v-for="(value, index) in activities" :key="index" style="width: 100%;">
					<card-edit-activity class="mx-auto my-5" :activity="value"></card-edit-activity>
					<card-edit-activity class="mx-auto my-5" :activity="value"></card-edit-activity>
					<card-edit-activity class="mx-auto my-5" :activity="value"></card-edit-activity>
				</div>
			</div>
		</v-sheet>
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