<template>
	<div>
		<TheBackground/>
		
		<v-sheet height="100vh" color="transparent" 
			style="overflow: hidden;"
			class="grey--text text--lighten-4
			pt-14 pt-md-16 mt-n14 mt-md-n16 
			d-flex flex-column align-center justify-space-between">

			<div style="margin-top: 5vh; text-align: center;">
				<h1 style="font-size: 4rem;" class="font-weight-regular">Guide Me</h1>
				<p style="width: 250px;" class="title ma-auto">Recherche une activity dans une région</p>
			</div>	

			<router-link :to="{ name: 'Search' }" style="margin: 15vh 0;">
				<v-btn large outlined rounded color="grey lighten-4">Rechercher</v-btn>
			</router-link>
		</v-sheet>

		<v-sheet class="primary secondary--text pa-5
			d-flex flex-column align-center">
			<div class="">
			<h2 class="headline font-weight-regular mb-5" style="text-align: center;">Vous souhaitez ajouter une activité?</h2>
			
				<p style="text-align: center;">Connectez-vous et ajoutez une activité dans l'application.</p>
				<img :src="imgMap.src" :alt="imgMap.alt">
				<v-btn outlined rounded color="accent">Ajouter une activité</v-btn>
			</div>
			
<div>
			<h2 class="headline font-weight-regular" style="text-align: center;">A propos de Guide Me</h2>

			<p>Guide Me est une application qui vous permet de trouver des activités à faire dans une région.</p>
			<p>C'est une application communautaire, nous comptons donc sur vous pour la rendre géniale!</p>
</div>
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

img {
	width:100px;
}

p {
	margin:0;
}

</style>