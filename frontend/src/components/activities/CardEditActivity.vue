<template>
	<v-card elevation="0"
	max-width="400px"
	color="primary lighten-2" 
	:class="{'primary darken-1 text--darken-4': !$vuetify.theme.dark}">
		<div>
			<CardActivity class="ma-0" :activity="activity"></CardActivity>

			<div class="d-flex justify-space-around" style="padding: 10px 0px">
				<v-btn @click="updateActivity" style="background-color: transparent; box-shadow: none;">Modifier</v-btn>
				<v-btn @click="deleteActivity" style="background-color: transparent; box-shadow: none;">Supprimer</v-btn>
			</div>
			
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