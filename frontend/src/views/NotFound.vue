<template>
	<v-sheet class="primary pt-15 d-flex flex-column align-center"  height="100%" width="100%">
		<img :src="img.src" :alt="img.alt" height="240px" class="mx-auto mb-3" style="display: block;"/>
		<div class="px-10 mb-15">
			<h3 class="subtitle-1 secondary--text text--darken-2">404</h3>
			<h2 class="display-1 secondary--text  mb-4">Je ne trouve rien ici...</h2>
			
			<p class="secondary--text mb-8">Désolé cette page n'a pas peut être trouvée.</p>

			<div style="width:100%; text-align: center;">
				<router-link :to="{ name: 'Home' }">
					<v-btn outlined rounded color="secondary">
						Retourner à l'accueil<v-icon >mdi-chevron-right</v-icon>
					</v-btn>
				</router-link>
			</div>
		</div>
	</v-sheet>
</template>

<script>
import pikachu from "@/assets/pikachu.png"

export default {
	name: "NotFound",
	data() {
		return {
			img: {
				src: pikachu,
				alt: "detective pikachu",
			},
		}
	}
}
</script>

<style>

</style>