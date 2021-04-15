<template>
	<v-card>
		<v-card-title>{{ creator.username }}</v-card-title>
		<v-card-subtitle>{{ rating.date }}</v-card-subtitle>
		<label>{{ rating.note }}</label>
		<v-card-text>
			<p>{{ rating.comment }}</p>
		</v-card-text>
	</v-card>
</template>

<script>
export default {
	name: "ReviewActivity",
	props: ['id'],

	data()
	{
		return {
			rating: null,
			creator: null,
		}
	},

	mounted()
	{
		this.fetchRating()
	},

	methods:
	{
		fetchRating()
		{
			console.log()
			this.$store.dispatch('fetchRating', {
				id: this.id,
			})
			.then(rating => {
				this.rating = rating.data
				this.fetchCreator()
			})
		},

		fetchCreator()
		{
			this.$store.dispatch('fetchUser', {
				id: this.rating.creator,
			})
			.then((creator) => {
				this.creator = creator.data
			})
		}
	}
}
</script>

<style>

</style>