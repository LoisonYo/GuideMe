<template>
	<v-sheet color="primary">
		<div>
		<h2>Error 404</h2>

		<img :src="img.src" :alt="img.alt" style="width: 100%;"/>
		</div>
	</v-sheet>
</template>

<script>
import aa from "@/assets/pikachu.png"

export default {
	name: "NotFound",
	data() {
		return {
			img: {
				src: aa,
				alt: "sushi",
			},
		}
	}
}
</script>

<style>

</style>