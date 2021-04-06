<template>
	<div style="width:100%;">
		
		<v-img :src="img" alt="image uploaded" 
			height="350"
			width="100%"
			class="grey"
			style="position: fixed; top: 0; left: 0; z-index: -1;"
		/>

		<div style="width:100%; height: 280px;" class="d-flex justify-center align-center">
			<v-btn icon x-large color="primary" @click="$refs.inputUpload.click()">
				<v-icon>mdi-camera</v-icon>
			</v-btn>
			<input type="file" style="display:none" accept="image/*" ref="inputUpload" @input="uploadFiles">
		</div>

		<v-sheet color="primary" class="pa-8 rounded-t-xl">
			<h2 class="text-center mb-8 headline secondary--text">
				Ajouter une activité
			</h2>
			<v-form @submit.prevent="login" v-model="valid" class="">
				<v-text-field v-model="name" label="Nom" required 
					color="accent" clearable>
				</v-text-field>

				<v-textarea
					label="Description"
					color="accent"
					auto-grow
					clearable>
				</v-textarea>

				<v-autocomplete
					v-model="values"
					:items="items"
					chips
					deletable-chips
					multiple
					label="Catégories"
					color="accent"
					item-color="accent">
				</v-autocomplete>

				<v-text-field v-model="name" label="Lien" prepend-inner-icon="mdi-link-variant" hint="Facultatif"
					persistent-hint required 
					color="accent" >
				</v-text-field>

				<p v-show="display_error" class="warning--text body-2 my-3">L'adresse mail et/ou le mot de passe sont incorrects !</p>
			
				<v-btn :disabled="!valid" type="submit"
					rounded color="accent" elevation="0" class="my-7">
					Enregistrer
				</v-btn>
			</v-form>
		</v-sheet>
	</div>
</template>

<script>
export default {
	name: "ActivityCreate",
	data() {
		return {
			valid: false,
			items: ['restaurant', 'sport', 'group', 'culture'],
			name: "",
			img: "",
			display_error: false,
		}
	},
	methods: {
		uploadFiles(e) {
			const file = e.target.files[0];
			this.img= URL.createObjectURL(file);
		},
	}
}
</script>

<style>

</style>