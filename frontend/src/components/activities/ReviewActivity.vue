<template>
	<v-card>
		<v-card-title v-if="creator">{{ creator.username }}</v-card-title>
		<v-card-subtitle>{{ review.date }}</v-card-subtitle>
		<label>{{ review.note }}</label>
		<v-card-text>
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