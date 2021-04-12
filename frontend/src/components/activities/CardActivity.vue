<template>
	<v-card elevation="0"
	max-width="400px" 
	color="primary lighten-2" 
	class="ma-5 d-flex justify-space-between" 
	:class="{'primary darken-1 text--darken-4': !$vuetify.theme.dark}">
		<div>
			<router-link :to="{ name: 'ActivityDetails', params: { id: title }}" class="secondary--text">link</router-link>
			<v-card-title
				class="headline"
				v-text="activity.name">
			</v-card-title>
			<v-card-subtitle>{{item.note}}</v-card-subtitle>
		</div>
		
		<v-img
			:src="item.img"
			class="ma-0"
			style="height:100px;"
			max-width="100"
		>
		</v-img>
	</v-card>
</template>

<script>
import sushi from "@/assets/activity/tennis.jpg";

export default {
	name: "CardActivity",
	props: {
		activity: {
			type: Object,
			required: true,
		}
	},
	data() {
		return {
			item: {
				note: 7.3,
				img: sushi,
			},
		}
	},
}
</script>

<style>

</style>