<template>
	<div class="primary pt-15 pb-10 px-7" style="width: 100%; height: 100%;">
		<v-sheet max-width="600px" class="transparent mx-auto">

			<h2 class="display-1 secondary--text my-5">Résultats</h2>

			<div class="d-flex flex-column align-center mt-5">
				<div v-for="(value, index) in activities" :key="index" style="width: 100%;">
					<card-activity class="mx-auto my-5" :activity="value"></card-activity>
					<card-activity class="mx-auto my-5" :activity="value"></card-activity>
					<card-activity class="mx-auto my-5" :activity="value"></card-activity>
				</div>

				<v-progress-circular v-intersect="infiniteScrolling"
					indeterminate
					v-show="loading"
					color="accent"
					class="mt-5">
				</v-progress-circular>
			</div>
		</v-sheet>
	</div>
</template>

<script>
import axios from "axios";
import CardActivity from '../../components/activities/CardActivity.vue';

export default {
  components: { CardActivity },
	name: 'SearchResults',
	data() {
		return {
			activities: [],
			titles: [],
			page: 1,
			loading: true,
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
		this.fetchData();
	},
	methods: {
		async fetchData()
		{
			var latitude;
			var longitude;

			if(typeof this.$route.query.center == 'string')
			{
				var values = this.$route.query.center.replace(/\s/g, '').split('(')[1].split(')')[0].split(',');
				latitude = parseFloat(values[0]);
				longitude = parseFloat(values[1]);
			}
			else
			{
				latitude = this.$route.query.center.lat;
				longitude = this.$route.query.center.lng;
			}

			try
			{
				var response = await this.$store.dispatch('fetchActivities', {
					latitude: latitude,
					longitude: longitude,
					radius: this.$route.query.radius,
				});

				this.activities = response.data.activities;
				this.loading = false;
			}
			catch(error)
			{
				//Rien
			}
		},
		
		infiniteScrolling() {
			setTimeout(() => {
				this.page++;
				axios
					.get(this.url)
					.then(response => {
						if (response.data.length > 1) 
							response.data.forEach(item => this.titles.push(item));
						else
							this.loading = false;
					})
					.catch(err => {
						console.log(err);
					});
			}, 500);
		}
	}
}
</script>

<style>

</style>