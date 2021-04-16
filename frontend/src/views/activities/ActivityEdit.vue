<template>
	<div v-if="activity" style="width:100%; height: 100%;">
		
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
				Modifier une activité
			</h2>

			<v-form @submit.prevent="updateActivity" v-model="valid" class="text-center">
				<v-text-field v-model="activity.name" label="Nom" 
					:rules="nameRules" required 
					color="accent" clearable>
				</v-text-field>

				<v-textarea v-model="activity.description" label="Description"
					:rules="descriptionRules" required 				
					color="accent" auto-grow clearable>
				</v-textarea>

				<v-autocomplete v-model="activity.types" item-value="id" item-text="name" :items="tags" label="Catégories"
					chips deletable-chips multiple
					color="accent" item-color="accent">
				</v-autocomplete>

				<v-text-field v-model="activity.website" label="Lien (facultatif)" 
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
	name: "ActivityEdit",
	props: ['id'],
	data() {
		return {
			img: '',
			activity: null,
			nameRules: [ v => !!v || "Nom requis" ],
			descriptionRules: [ v => !!v || "Description requise" ],
			tags: [],
			valid: false,
			errors: [],
			file: null,
		}
	},

	mounted()
	{
		this.fetchTags();
		this.fetchActivity();
	},

	methods: {
		fetchActivity()
		{
			this.$store.dispatch('fetchActivity', {
				id: this.id,
			})
			.then(activity => {
				this.activity = activity.data;
				this.fetchImage()
			})
		},

		fetchTags()
		{
			this.$store.dispatch("fetchTags")
			.then(tags => {
				this.tags = tags.data;
			})
		},

		async fetchImage()
		{
			const name = this.activity.image.split('/').pop();
			const response = await fetch(this.activity.image);
			const blob = await response.blob();
			this.file = new File([blob], name, {type: blob.type});
			this.img = URL.createObjectURL(this.file);
		},

		updateActivity()
		{
			this.$store.dispatch("updateActivity", {
				creator: this.$store.state.user.id,
				id: this.activity.id,
				name: this.activity.name,
				description: this.activity.description,
				longitude: this.activity.longitude,
				latitude: this.activity.latitude,
				tags: this.activity.types,
				website: this.activity.link,
				image: this.file,
			})
			.then(result => {
				this.$router.push({name: 'ActivityDetails', params: { id: result.data.id }})
			});
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