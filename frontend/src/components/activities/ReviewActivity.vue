<template>
	<v-card>
		<v-card-title>{{ author }}</v-card-title>
		<v-card-subtitle>{{ date }}</v-card-subtitle>
		<v-card-text>
			<p>{{ review }}</p>
		</v-card-text>
	</v-card>
</template>

<script>
export default {
	name: "ReviewActivity",
	data() {
		return {
			author: "Gōshō Aoyama",
			review: `Literally the best sushi in the region. In a very simple but pleasant atmosphere, you can eat the freshest sushi. 
						The service is always impeccable. It is the perfect lunch break.`,
			date: "01.04.21"
		}
	},
}
</script>

<style>

</style>