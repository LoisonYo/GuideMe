<template>
  <div style="height:100%; width:100%;" class="pt-14 pt-md-16">
		<TheBackground />
		
		<h1 class="text-center
			grey--text text--lighten-4 font-weight-regular"
			style="font-size: 2.4rem;">
			Guide Me
		</h1>

		<v-card color="primary" 
			max-width="400px"
			style="width: calc(100% - 104px);" 
			class="mt-4 mb-16 mx-auto pa-12 rounded-xl text-center">

			<slot></slot>	

			<v-row align="center" v-if="link != null">
				<v-divider class="mr-5"></v-divider>
					or
				<v-divider class="ml-5"></v-divider>
			</v-row>

			<div class="mt-7 mb-5" v-if="link != null">
				<router-link :to="{ name: link.route }" class="accent--text">
					{{link.name}}
				</router-link>
			</div>
		</v-card>
	</div>
</template>

<script>
import TheBackground from '@/components/TheBackground.vue'
export default {
	name: "BaseContainerLogin",
	components: { TheBackground },
	props: {
		link: {
			type: Object,
			default: null,
		},
	},
}
</script>

<style>

</style>