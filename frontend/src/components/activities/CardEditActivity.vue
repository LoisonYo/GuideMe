<template>
	<v-card elevation="0"
		class="rounded-lg"
		color="primary lighten-1"
		:class="{'primary darken-2 text--darken-4': !$vuetify.theme.dark}"
		style="width:100%;">

		<CardActivity class="ma-0" :activity="activity"></CardActivity>

		<div class="d-flex justify-space-around py-3">
			<v-btn @click="updateActivity" elevation="0" color="accent">Modifier</v-btn>
			<v-btn @click="deleteActivity" elevation="0" color="error">Supprimer</v-btn>
		</div>
	</v-card>
</template>

<script>
import CardActivity from '../../components/activities/CardActivity.vue';

export default {
	components:
	{
		CardActivity
	},

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