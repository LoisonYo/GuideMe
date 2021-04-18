<template>
	<v-card elevation="0" 
		height="100px"
		class="rounded-lg"
		color="primary lighten-2"
		:class="{'primary darken-1 text--darken-4': !$vuetify.theme.dark}"
		style="width:100%;">

		<router-link :to="{ name: 'ActivityDetails', params: { id: activity.id }}" class="secondary--text d-flex justify-space-between" style="height:100%; width: 100%">
			<div class="my-auto mx-3 text-truncate" style="width: 100%;" >
				<v-card-title class="headlines"
					style="width: 100%;"
					v-text="activity.name">
				</v-card-title>

				<v-card-subtitle class="title" 
					:style="color"
					v-text="activity.note">
				</v-card-subtitle>
			</div>

			<v-img
				:src="activity.image"
				class="ma-0 rounded-r-lg"
				max-width="150"
				style="width: 150px;">
			</v-img>

		</router-link>
	</v-card>
</template>

<script>
export default {
	name: "CardActivity",
	props: {
		activity: {
			type: Object,
			required: true,
		}
	},

	computed:
	{
		color()
		{
			var tmp = 255 / 10;
			var green = tmp * this.activity.note;
			var red = 255 - green;

			return {
				color: 'rgb(' + red + ',' + green + ',0)'
			}
		}
	}
}
</script>

<style>

</style>