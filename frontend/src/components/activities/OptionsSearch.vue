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
			<v-sheet color="primary" class="d-flex align-center pb-3 pb-md-5 pt-14 pt-md-16 px-6">
				<h3 class="secondary--text mr-3 subtitle-1">Rayon</h3>

				<v-slider v-if="toggle"
					v-model="radius"
					:max="max"
					:min="min"
					hide-details
					color="accent"
					track-color="secondary"
					height="38px"
					class="mt-0 pt-0">
				</v-slider>

				<v-text-field v-else
					v-model="radius"
					type="number"
					hide-details
					single-line
					solo flat dense
					suffix="km"
					color="primary"
					background-color="secondary" 
					class="mt-0 pt-0 body-1 primary--text">
				</v-text-field>
			</v-sheet>		

			<router-link :to="{ name: 'Results' }" class="mt-2" style="display:flex; justify-content: center; width: 100%;">
				<v-btn rounded color="accent" elevation="0">Rechercher</v-btn>
			</router-link>	
		</v-sheet>
	</div>
</template>

<script>
import { gsap } from 'gsap';

export default {
	name: "OptionsSearch",
	data () {
		return {
			radius: 0,
			tweenedNumber: 0,
			min: 100,
			max: 5e3,
			toggle: true,
		}
	},
	computed: {
		animatedNumber: function() {
			return this.tweenedNumber.toFixed(0);
		}
	},
	mounted() {
		gsap.to(this.$data, { duration: 1.2, radius: 2.5e3 });
	},
	watch: {
		radius: function () {
			this.$emit('value', this.radius);
		},
	},
}
</script>

<style scoped>
>>>.v-text-field__slot input{
	color: var(--v-primary-base) !important;
}

/* Chrome, Safari, Edge, Opera */
>>>input::-webkit-outer-spin-button,
>>>input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
>>>input[type=number] {
  -moz-appearance: textfield;
}
</style>