<template>
	<v-card elevation="0"
	max-width="400px" 
	color="primary lighten-2"
	:class="{'primary darken-1 text--darken-4': !$vuetify.theme.dark}">
		<router-link :to="{ name: 'ActivityDetails', params: { id: activity.id }}" class="secondary--text d-flex justify-space-between">
			<div style="margin: auto 0px;">
				<v-card-title
					class="headline"
					v-text="activity.name">
				</v-card-title>
				<v-card-subtitle :style="color">{{activity.note}}</v-card-subtitle>
			</div>
			
			<v-img
				:src="activity.image"
				class="ma-0"
				style="object-fit: contain"
				max-width="120px"
				height="120px"
			>
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