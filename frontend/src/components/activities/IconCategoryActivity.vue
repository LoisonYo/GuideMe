<template>
	<div style="text-align: center;">
		<span class="secondary pa-3 rounded-lg">
			<v-icon color="primary">{{ icon }}</v-icon>
		</span>
		<h5 class="caption mt-2 secondary--text">{{ name }}</h5>
	</div>
	
</template>

<script>
export default {
	name: "IconCategoryActivity",
	props: {
		name: {
			type: String,
			required: true
		},
		icon: {
			type: String,
			required: true
		}
	}
}
</script>

<style>

</style>