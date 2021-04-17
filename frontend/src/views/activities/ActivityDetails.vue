<template>
	<div v-if="activity" style="width:100%; height: 100%;">
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
			<p class="secondary--text" style="text-align: justify">{{ activity.description }}</p>

			<div class="d-flex my-10">
				<IconCategoryActivity v-for="(category, index) in tags" :key="index" :name="category.name" :icon="category.icon" class="mr-3"/>	
			</div>

			<div v-if="activity.website" style="width:100%; text-align: center;">
				<a :href="activity.website">
					<v-btn rounded color="accent" elevation="0">
						<v-icon left>mdi-link-variant</v-icon>
						Site officiel
					</v-btn>
				</a>
			</div>

			<PositionViewer v-model="activity" style="margin: 50px 10px"></PositionViewer>
			
			<v-divider class="my-10 "></v-divider>
			<ReviewEditor :activity_id="activity.id" :current_review="current_review"></ReviewEditor>		
			<ReviewActivity v-for="(review, index) in reviews" :key="index" :review="review"></ReviewActivity>
		</v-sheet>
	</div>
</template>

<script>
import IconCategoryActivity from '@/components/activities/IconCategoryActivity.vue'
import ReviewActivity from '@/components/activities/ReviewActivity.vue'
import ReviewEditor from '@/components/activities/ReviewEditor.vue'
import PositionViewer from '@/components/activities/PositionViewer.vue'

export default {
	components: { 
		IconCategoryActivity,
		ReviewActivity,
		ReviewEditor,
		PositionViewer,
	},
	name: "ActivityDetails",
	props: ['id'],

	data() {
		return {
			activity: Object(),
			tags: [],
			reviews: [],

			current_review: undefined,
		}
	},

	mounted()
	{
		this.fetchActivity();
	},

	methods:
	{
		async fetchActivity()
		{
			try
			{
				var response = await this.$store.dispatch('fetchActivity', {
					id: this.id,
				});

				this.activity = response.data;
				this.fetchTags()
				this.fetchReviews()
			}
			catch(error)
			{
				this.$router.replace({name:"Search"})
			}
		},

		async fetchTags()
		{
			try
			{
				var response = await this.$store.dispatch('fetchActivityTags', {
					id: this.activity.id,
				});

				this.tags = response.data.types;
			}
			catch(error)
			{
				console.log(error)
			}
		},

		async fetchReviews()
		{
			try
			{
				var response = await this.$store.dispatch('fetchActivityRatings', {
					id: this.activity.id,
				});

				this.reviews = response.data.ratings;

				if(this.$store.getters.loggedIn)
				{
					this.reviews.forEach(element => {
						if(element.creator == this.$store.state.user.id)
							this.current_review = element;
					});
				}
				
			}
			catch(error)
			{
				console.log(error)
			}
		},
	}
}
</script>

<style>

</style>