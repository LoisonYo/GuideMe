<template>
	<v-card>
		<v-card-title>{{ rating.creator.username }}</v-card-title>
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
	props: {
		rating: {
			type: Object,
			required: true,
		}
	},
}
</script>

<style>

</style>