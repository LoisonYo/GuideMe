<template>
	<div style="width:100%; height: 100%;">
		<v-img :src="img.src" :alt="img.alt"
			width="100%"
			height="300"
			style="position: fixed; top: 0; left: 0; z-index: -1;"
		/>

		<v-sheet color="primary" class="pa-8 rounded-t-xl" style="margin-top: 280px; height: calc(100% - 280px);" >
			<div class="d-flex justify-space-between align-end mb-5">
				<h2 class="display-2 secondary--text">{{ title }}</h2>
				<div style="text-align: center;">
					<h3 class="accent--text font-weight-medium" style="font-size: 2rem;">{{ note }}</h3>
					<p class="ma-n2 body-2 secondary--text text--darken-2">sur 10</p>
				</div>
			</div>
			<p class="secondary--text">{{ description }} <br><br> {{ id }}</p>

			<div class="d-flex my-10">
				<IconCategoryActivity v-for="category in categories" :key="category" :name="category" :icon="getIcon(category)" class="mr-3"/>	
			</div>
			
			<div style="width:100%; text-align: center;">
				<a :href="link">
					<v-btn rounded color="accent" elevation="0">
						<v-icon left>mdi-link-variant</v-icon>
						Site officiel
					</v-btn>
				</a>
			</div>
			<v-divider class="my-10 "></v-divider>		
			<ReviewActivity />
		</v-sheet>
		
	</div>
</template>

<script>
import IconCategoryActivity from '@/components/activities/IconCategoryActivity.vue'
import ReviewActivity from '@/components/activities/ReviewActivity.vue'
import sushi from "@/assets/background/banner.png";

export default {
	components: { 
		IconCategoryActivity,
		ReviewActivity 
	},
	name: "ActivityDetails",
	props: ['id'],
	async beforeMount() {
		// TODO request API with id
	},
	data() {
		return {
			img: {
				src: sushi,
				alt: "sushi",
			},
			title: "Jugemu",
			note: 7.3,
			description: `Japanese temaki rolls are awesome, especially at Jugemu in Soho, where they’re made to order for punters sitting at the counter. 
								Each little package is packed with super-fresh ingredients and handed over the instant it’s ready, the nori wrapping still crisp. 
								Alternatively, bag a table for full platters of sushi and sashimi.`,
			categories: ["restaurant", "delivery"],
			link: "https://www.sushizen.shop",
		}
	},
	methods: {
		getIcon(category) {
			switch (category) {
				case "restaurant": return "mdi-silverware-fork-knife";
				case "delivery": return "mdi-moped";
				default: return null;
			}
		}
	}
}
</script>

<style>

</style>