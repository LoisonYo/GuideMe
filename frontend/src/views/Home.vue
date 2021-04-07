<template>
	<div style="width:100%;">
		<TheBackground/>
		
		<v-sheet height="100vh" color="transparent" 
			style="overflow: hidden;"
			class="grey--text text--lighten-4
			pt-14 pt-md-16 
			d-flex flex-column align-center justify-space-between">

			<div style="margin-top: 5vh; text-align: center;">
				<h1 style="font-size: 4rem;" class="font-weight-regular">Guide Me</h1>
				<p style="width: 250px;" class="title ma-auto">Recherche une activity dans une région</p>
			</div>	

			<router-link :to="{ name: 'Search' }" style="margin: 15vh 0;">
				<v-btn large outlined rounded color="grey lighten-4">Rechercher</v-btn>
			</router-link>
		</v-sheet>

		<v-sheet class="primary secondary--text pa-10 rounded-t-xl
			d-flex flex-column align-center">

			<h2 style="font-size: 2rem;" class="font-weight-regular my-4 text-center">
				Vous souhaitez ajouter une activité?
			</h2>
			<p class="text-center">Connectez-vous et ajoutez une activité dans l'application.</p>
			<img :src="imgMap.src" :alt="imgMap.alt" width="130px" class="my-7">

			<router-link :to="{ name: 'ActivityCreate' }" class="mt-3">
				<v-btn rounded color="accent" elevation="0">Ajouter une activité</v-btn>
			</router-link>

			<div style="width: 100%;" class="mb-5 mt-12">
				<v-divider class="secondary"></v-divider>
			</div>

			<h2 style="font-size: 2rem;" class="font-weight-regular my-4 text-center">
				A propos de Guide Me
			</h2>

			<p class="text-center mb-2">Guide Me est une application qui vous permet de trouver des activités à faire dans une région.</p>
			<p class="text-center mb-10">C'est une application communautaire, nous comptons donc sur vous pour la rendre géniale!</p>

		</v-sheet>	
	</div>
</template>

<script>
// @ is an alias to /src
import TheBackground from '@/components/TheBackground.vue';
import map from "@/assets/map.png"

export default {
	name: "Home",
	components: {
		TheBackground,
	},
	data() {
		return {
			imgMap: {
				src: map,
				alt: "map icon",
			}
		}
	},
};
</script>

<style scoped>

p {
	margin:0;
}

</style>