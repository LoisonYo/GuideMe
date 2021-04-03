<template>
	<div>
		<!-- Switch between slider and text-field -->
		<v-switch v-model="toggle"
			color="accent"
			hide-details
			class="ma-0 pa-0 mr-15 mt-4 mt-md-5"
			style="position: fixed; top:0; right: 0; z-index: 200;">
		</v-switch>

		<v-sheet width="100%" color="transparent" style="position: fixed; top:0; z-index: 1;">
			<v-sheet color="primary" class="d-flex align-center pb-3 pb-md-5 pt-13 pt-md-15 px-5">
				<h3 class="secondary--text mr-4 subtitle-1">Rayon :</h3>

				<v-slider v-if="toggle"
					v-model="radius"
					:max="max"
					:min="min"
					hide-details
					color="accent"
					track-color="secondary"
					class="mt-0 pt-0">
				</v-slider>

				<v-text-field v-else
					v-model="radius"
					type="number"
					hide-details
					single-line
					suffix="km"
					color="accent"
					class="mt-0 pt-0">
				</v-text-field>
			</v-sheet>		

			<router-link :to="{ name: 'Results' }" class="mt-2" style="display:flex; justify-content: center; width: 100%;">
				<v-btn rounded color="accent" elevation="0">Rechercher</v-btn>
			</router-link>	
		</v-sheet>

		
	</div>
</template>

<script>
export default {
	name: "OptionsSearch",
	data () {
		return {
			radius: 2.5e3,
			min: 100,
			max: 5e3,
			toggle: true,
		}
	},
	watch: {
		radius: function () {
			this.$emit('value', this.radius);
		}
	},
}
</script>

<style>
/* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type=number] {
  -moz-appearance: textfield;
}
</style>