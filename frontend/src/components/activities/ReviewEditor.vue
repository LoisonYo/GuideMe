<template>
	<v-card v-if="canComment" class="d-flex justify-center transparent" style="margin-bottom: 30px; box-shadow: none">

        <v-btn v-if="!display_form" @click="toggleForm" text rounded color="accent" class="subtitle-1">
            <v-icon v-text="icon" class="mr-3" color="rgb(107,119,180)"></v-icon>
            Écrire une review
        </v-btn>

        <div v-if="display_form" style="width:100%">
            <h2 class="display-1 secondary--text mb-5">Review</h2>
            <v-form class="text-center transparent" style="width:100%">
                <StarRating v-model="review.note" :max="10" style="width:400px;" class="mx-auto"></StarRating>

				<v-textarea v-model="review.comment" label="Commentaire" required color="accent" auto-grow clearable></v-textarea>
                <div v-if="!updating" class="d-flex justify-space-between">
                    <v-btn @click="createReview" rounded color="accent" elevation="0" class="my-8">Envoyer</v-btn>
                    <v-btn @click="toggleForm" text rounded color="accent" elevation="0" class="my-8">Annuler</v-btn>
                </div>

                <div v-if="updating" class="d-flex justify-space-between">
                    <v-btn @click="editReview" rounded color="accent" elevation="0" class="my-8">Modifier</v-btn>
                    <v-btn @click="deleteReview" text rounded color="accent" elevation="0" class="my-8">Supprimer</v-btn>
                </div>
                
			</v-form>
        </div>
	</v-card>
</template>

<script>
import StarRating from '@/components/activities/StarRating.vue'

export default {
	name: "ReviewEditor",
    props: ['activity_id', 'current_review'],

    watch:
    {
        current_review: function() {
            if(this.current_review != undefined)
            {
                this.display_form = true;
                this.updating = true;
                this.review = this.current_review;
            }
        }
    },

    components:
    { 
		StarRating,
	},

    data()
    {
        return {
            display_form: false,
            icon: 'mdi-comment-edit-outline',
            updating: false,

            review:
            {
                note: 5,
                comment: "",
                activity_id: this.activity_id,
            },
        }
    },

    methods:
    {
        toggleForm()
        {
            this.display_form = !this.display_form;
        },

		async createReview()
		{
			try
			{
				await this.$store.dispatch('createRating', {
					'creator': this.$store.state.user.id,
					'note': this.review.note,
					'comment': this.review.comment,
					'activity': this.activity_id,
				});

				this.$router.go();
			}
			catch(error)
			{
				console.log(error)
			}
		},

        async editReview()
		{
			try
			{
				await this.$store.dispatch('updateRating', {
                    'id': this.review.id,
					'creator': this.$store.state.user.id,
					'note': this.review.note,
					'comment': this.review.comment,
					'activity': this.review.activity,
				});

				this.$router.go();
			}
			catch(error)
			{
				console.log(error)
			}
		},

        async deleteReview()
		{
			try
			{
				await this.$store.dispatch('deleteRating', {
                    'id': this.review.id,
				});

				this.$router.go();
			}
			catch(error)
			{
				console.log(error)
			}
		},
    },

    computed:
    {
        canComment()
        {
            return this.isAutheticated;
        },

        isAutheticated()
        {
            return this.$store.getters.loggedIn;
        },
    }
}
</script>

<style>

</style>