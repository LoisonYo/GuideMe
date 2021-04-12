<template>
	<div class="primary pt-15 pb-10 px-7" style="width: 100%; height: 100%;">
		<h1>Résultats</h1>

		<div class="d-flex flex-column align-center">
			<div v-for="(value, index) in activities" :key="index" style="width: 100%;">
				<card-activity class="mx-auto my-2" :activity="value"></card-activity>
			</div>

			<v-progress-circular v-intersect="infiniteScrolling"
				indeterminate
				v-show="loading"
				color="accent"
				class="mt-5">
			</v-progress-circular>
		</div>
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
	created() {
		this.fetchData();
	},
	methods: {
		async fetchData()
		{
			var values = this.$route.query['center'].replace(/\s/g, '').split('(')[1].split(')')[0].split(',');
			var latitude = parseFloat(values[0]);
			var longitude = parseFloat(values[1]);

			var intent = await this.$store.dispatch('fetchActivities', {
				longitude: longitude,
				latitude: latitude,
				radius: this.$route.query.radius,
			})

			this.activities = Object.values(intent.data).flat();
			this.loading = false;
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