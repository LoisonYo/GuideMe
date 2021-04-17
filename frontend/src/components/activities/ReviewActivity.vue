<template>
	<v-card style="margin-bottom: 10px; background-color: rgb(61,69,89)">
		<v-card-title v-if="creator" style="color: rgb(107,119,180)">{{ creator.username }}</v-card-title>
		<v-card-subtitle>{{ review.date }}</v-card-subtitle>
		<div class="d-flex" style="min-height: 60px;">
			<div style="text-align: center; width: 100px; margin-right: 30px; padding-left: 20px; padding-bottom: 40px; padding-top: 20px;">
				<h3 class="accent--text font-weight-medium" style="font-size: 1.6rem;">{{ review.note }}</h3>
				<p class="ma-n2 body-2 secondary--text text--darken-2">sur 10</p>
			</div>
			<v-card-text style="padding: 0px; padding-right: 20px; text-align: justify">
				<p>{{ review.comment }}</p>
			</v-card-text>
		</div>
	</v-card>
</template>

<script>
export default {
	name: "ReviewActivity",
	props: ['review'],

	data()
	{
		return {
			creator: null,
		}
	},

	mounted()
	{
		this.fetchCreator()
	},

	methods:
	{
		async fetchCreator()
		{
			try
			{
				var response = await this.$store.dispatch('fetchUser', {
					id: this.review.creator,
				});

				this.creator = response.data;
			}
			catch(error)
			{
				console.log(error)
			}
		}
	}
}
</script>

<style>

</style>