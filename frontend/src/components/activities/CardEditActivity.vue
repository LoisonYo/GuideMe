<template>
	<v-card elevation="0"
	max-width="400px" 
	color="primary lighten-2" 
	class="ma-5 d-flex justify-space-between" 
	:class="{'primary darken-1 text--darken-4': !$vuetify.theme.dark}">
		<div>
		<div>
			<v-card-title
				class="headline"
				v-text="activity.name">
			</v-card-title>
			<v-card-subtitle>{{activity.note}}</v-card-subtitle>
		</div>		
			<v-btn>Modifier</v-btn>
			<v-btn @click="deleteActivity">Supprimer</v-btn>
		</div>
	</v-card>
</template>

<script>
export default {
	name: "CardEditActivity",
	props: {
		activity: {
			type: Object,
			required: true,
		}
	},

	methods:
	{
		deleteActivity()
		{
			this.$store.dispatch("deleteActivity", {
				id: this.activity.id,
			})
			.then(() => {
				this.$parent.fetchUserActivities()
			});
		}
	}
}
</script>

<style>

</style>