<template>
	<v-card elevation="0"
	max-width="400px" 
	color="primary lighten-2" 
	class="ma-5 d-flex justify-space-between" 
	:class="{'primary darken-1 text--darken-4': !$vuetify.theme.dark}">
		<div>
			<div>
				<router-link :to="{ name: 'ActivityDetails', params: { id: activity.id }}" class="secondary--text">{{ activity.name }}</router-link>
				<v-card-subtitle>{{activity.note}}</v-card-subtitle>
			</div>
			<v-btn @click="updateActivity">Modifier</v-btn>
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
		async deleteActivity()
		{
			if (confirm("Voulez-vous vraiment supprimer cette activitée ?"))
			{
				try
				{
					await this.$store.dispatch("deleteActivity", {
						id: this.activity.id,
					});

					this.$parent.fetchUserActivities();
				}
				catch(error)
				{
					//Rien
				}
			}
		},

		updateActivity()
		{
			this.$router.push({name: 'ActivityEdit', params: { id: this.activity.id }})
		},
	}
}
</script>

<style>

</style>