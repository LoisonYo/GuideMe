<template>
	<div style="width:100%; height: 100%;">
		
		<v-img :src="img" alt="image uploaded" 
			height="300" width="100%"
			class="grey"
			style="position: fixed; top: 0; left: 0; z-index: -1;"
		/>

		<div style="width:100%; height: 280px;" class="d-flex justify-center align-center">
			<v-btn icon x-large color="primary" @click="$refs.inputUpload.click()">
				<v-icon>mdi-camera</v-icon>
			</v-btn>
			<v-btn icon x-large color="primary" class="ml-4" v-if="img != ''" @click="resetFiles">
				<v-icon>mdi-close</v-icon>
			</v-btn>
			<input type="file" style="display:none" accept="image/*" ref="inputUpload" @input="uploadFiles">
		</div>

		<v-sheet color="primary" class="pa-8 rounded-t-xl" style="height: calc(100% - 280px);">
			<v-sheet max-width="600px" class="transparent mx-auto">
			<h2 class="text-center mb-8 headline secondary--text">
				Ajouter une activité
			</h2>

			<v-form @submit.prevent="createActivity" v-model="valid" class="text-center">
				<v-text-field v-model="name" label="Nom" 
					:rules="nameRules" required 
					color="accent" clearable>
				</v-text-field>

				<v-textarea v-model="description" label="Description"
					:rules="descriptionRules" required 				
					color="accent" auto-grow clearable>
				</v-textarea>

				<v-autocomplete v-model="values" item-value="url" item-text="name" :items="tags" label="Catégories"
					chips deletable-chips multiple
					color="accent" item-color="accent">
				</v-autocomplete>

				<v-text-field v-model="link" label="Lien (facultatif)" 
					prepend-inner-icon="mdi-link-variant"
					hint="www.example.com/page" persistent-hint 
					color="accent">
				</v-text-field>

				<ul class="warning--text body-2 mb-0 mt-8">
					<li v-for="(value, index) in errors" :key="index">{{ index }} : {{ value }}</li>
				</ul>
			
				<v-btn :disabled="!valid" type="submit"
					rounded color="accent" elevation="0" class="my-8">
					Enregistrer
				</v-btn>
			</v-form>
			</v-sheet>
		</v-sheet>
	</div>
</template>

<script>
export default {
	name: "ActivityCreate",
	data() {
		return {
			img: "",
			name: "",
			nameRules: [
				v => !!v || "Nom requis",
			],
			description: "",
			descriptionRules: [
				v => !!v || "Description requise",
			],
			tags: [],
			values: [],
			link: "",
			valid: false,
			errors: [],
			file: null,
		}
	},

	mounted()
	{
		this.fetchTags();
	},

	methods: {
		fetchTags()
		{
			this.$store.dispatch("fetchTags")
			.then((tags) => {
				this.tags = Object.values(tags.data).flat();
			})
		},

		createActivity()
		{
			this.$store.dispatch("createActivity", {
				creator: this.$store.state.user.url,
				name: this.name,
				description: this.description,
				longitude: this.longitude,
				latitude: this.latitude,
				website: this.link,
				tags: this.values,
				image: this.file,
			})
			.then(() => {
				
			})
			.catch(errors => {
				this.errors = errors.response.data;
			})
		},

		resetFiles()
		{
			this.$refs.inputUpload.value = '';
			this.img = "";
		},
		uploadFiles(e) {
			if (e.target.files && e.target.files[0]) {
				this.file = e.target.files[0];
				this.img= URL.createObjectURL(this.file);
			}
		},
	}
}
</script>

<style>

</style>