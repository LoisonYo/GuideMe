<template>
	<div style="width:100%; height: 100%;">
		<v-img :src="activity.image"
			width="100%"
			height="300"
			style="position: fixed; top: 0; left: 0; z-index: -1;"
		/>

		<v-sheet color="primary" class="pa-8 rounded-t-xl" style="margin-top: 280px; height: calc(100% - 280px);" >
			<div class="d-flex justify-space-between align-end mb-5">
				<h2 class="display-2 secondary--text">{{ activity.name }}</h2>
				<div style="text-align: center;">
					<h3 class="accent--text font-weight-medium" style="font-size: 2rem;">{{ activity.note }}</h3>
					<p class="ma-n2 body-2 secondary--text text--darken-2">sur 10</p>
				</div>
			</div>
			<p class="secondary--text">{{ activity.description }} <br><br> {{ activity.id }}</p>

			<div class="d-flex my-10">
				<IconCategoryActivity v-for="category in activity.types" :key="category" :name="category.name" :icon="category.icon" class="mr-3"/>	
			</div>
			
			<div style="width:100%; text-align: center;">
				<a :href="activity.website">
					<v-btn rounded color="accent" elevation="0">
						<v-icon left>mdi-link-variant</v-icon>
						Site officiel
					</v-btn>
				</a>
			</div>
			<v-divider class="my-10 "></v-divider>		
			<ReviewActivity v-for="rating in activity.ratings" :key="rating" :rating="rating"></ReviewActivity>
		</v-sheet>
		
	</div>
</template>

<script>
import IconCategoryActivity from '@/components/activities/IconCategoryActivity.vue'
import ReviewActivity from '@/components/activities/ReviewActivity.vue'

export default {
	components: { 
		IconCategoryActivity,
		ReviewActivity 
	},
	name: "ActivityDetails",
	props: ['id'],

	data() {
		return {
			activity: null,
			note: 7.3,
		}
	},

	mounted()
	{
		this.fetchActivity();
	},

	methods:
	{
		fetchActivity()
		{
			this.$store.dispatch('fetchActivity', {
				id: this.$route.params.id,
			})
			.then((activity) => {
				this.activity = activity.data;
				console.log(this.activity)
			})
		},
	}
}
</script>

<style>

</style>