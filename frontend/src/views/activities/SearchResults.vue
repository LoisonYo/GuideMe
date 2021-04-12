<template>
	<div class="primary pt-15 pb-10 px-7" style="width: 100%; height: 100%;">
		<h1>Résultats</h1>
		<p> {{ $route.query }}</p>

		<div class="d-flex flex-column align-center">
			<div v-for="(title, index) in titles" :key="index" style="width: 100%;">
				<card-activity class="mx-auto my-2" :activity="title"></card-activity>
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
		async fetchData() {
			const response = await axios.get(this.url);
			this.titles = response.data;
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