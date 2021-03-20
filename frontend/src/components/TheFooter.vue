<template>
	<v-footer class="accent
		grey--text text--lighten-4
		d-flex flex-column align-center py-5">
		<p class="body-2">
			{{ new Date().getFullYear() }} — Guide Me
		</p>
		<p class="body-2">
			Tous droits réservés
		</p>
	</v-footer>
</template>

<script>
export default {
	name: "TheFooter",
}
</script>

<style scoped>
p {
	margin: 0;
}
</style>