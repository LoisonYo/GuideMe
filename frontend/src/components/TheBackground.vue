<template>
  <img :src="img.src" :alt="img.alt">
</template>

<script>
import road from "@/assets/background/road.jpeg";

export default {
	name: "TheBackground",
	data() {
		return {
			img: {
				src: road,
				alt: "road",
			},
		}
	},	
}
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
	filter: brightness(80%);
}

</style>