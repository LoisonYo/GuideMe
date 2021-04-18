<template>
	<v-card color="primary lighten-2" elevation="0" class="secondary--text my-5" :class="{'primary darken-1 text--darken-4': !$vuetify.theme.dark}">
		<div class="d-flex justify-space-between" style="width: 100%;">
			<div>
				<v-card-title v-if="creator" class="headline accent--text">{{ creator.username }}</v-card-title>
				<v-card-subtitle>{{ review.date }}</v-card-subtitle>
			</div>

			<div class="px-5 my-auto" style="text-align: center;">
				<h3 class="accent--text font-weight-medium" style="font-size: 1.6rem;">{{ review.note }}</h3>
				<p class="ma-n2 body-2 secondary--text text--darken-2">sur 10</p>
			</div>
		</div>

		<v-card-text class="pt-0 pb-2" style="text-align: justify;">
			<p>{{ review.comment }}</p>
		</v-card-text>
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