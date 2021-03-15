<template>
	<div>
		<img :src="img.src" :alt="img.alt">
		
		<v-sheet height="100vh" color="transparent" class="pt-14 pt-md-16 mt-n14 mt-md-n16 grey--text text--lighten-4" >
			<h1 class="display-3 font-weight-regular">Guide Me</h1>
			<p>Recherche une activity dans une région</p>
			<router-link :to="{ name: 'Search' }" style="text-decoration: none;">
				<v-btn outlined rounded color="grey lighten-4">Rechercher</v-btn>
			</router-link>
		</v-sheet>

		<v-sheet class="primary secondary--text ">
			<h2>Vous souhaitez ajouter une activité?</h2>
			<p>Connectez-vous et ajoutez une activité dans l'application.</p>
			<v-btn outlined rounded color="accent">Ajouter une activité</v-btn>

			<h2>A propos de Guide Me</h2>
			<p>Guide Me est une application qui vous permet de trouver des activités à faire dans une région.</p>

			<p>C'est une application communautaire, nous comptons donc sur vous pour la rendre géniale!</p>

		</v-sheet>	
	</div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from "@/components/HelloWorld.vue";
import road from "@/assets/background/road.jpeg";

export default {
	name: "Home",
	components: {
		
	},
	data() {
		return {

			img: {
				src: road,
				alt: "road",
			}
		}
	},
	computed: {
		
	},
};
</script>

<style scoped>

img {
	position: fixed;
	top: 0;
	left: 0;
	z-index: -1;
	width: 100%;
	height: 100vh;
	object-fit: cover;
}

p {
	margin:0;
}
#yo {
	display: flex;
	flex-direction: column;
	align-items: center;
	
}

</style>