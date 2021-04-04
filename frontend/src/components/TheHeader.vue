<template>
	<nav>
		<v-app-bar absolute color="transparent" flat style="z-index: 10;">
			<v-app-bar-nav-icon class="mx-0" v-on:click="drawer = !drawer">
				<input type="checkbox" id="openmenu-input" v-model="drawer">
				<label id="hamburger-lbl" for="openmenu-input">
					<span v-for="i in 3" :key="i" 
					:style="{ background: colorNavIcon }"
					v-bind:class="[{ 'secondary': drawer }]"></span>
				</label>
			</v-app-bar-nav-icon>

			<v-spacer></v-spacer>

			<ButtonToggleTheme />
		</v-app-bar>

		<v-navigation-drawer fixed temporary :width="navWidth" class="pt-16" color="primary" v-model="drawer">
			<v-list nav dense> 
				<router-link v-for="(item, i) in items" :key="i" :to=" { name: item.route } " style="text-decoration: none;">
					<v-list-item link>
					
						<v-list-item-icon >
							<v-icon v-text="item.icon" class="ml-3" color="secondary"></v-icon>
						</v-list-item-icon>
						
						<v-list-item-content>
							<v-list-item-title v-text="item.text" class="secondary--text"></v-list-item-title>
						</v-list-item-content>
					
					</v-list-item>
				</router-link>
			</v-list>				
			
			<template v-slot:append>
				<v-divider class="mx-2"></v-divider>
				<div class="pa-2">
					<div v-if="loggedIn">
						<h4 class="body-1 text-center">{{user.name}}</h4>
						<h5 class="caption text-center mb-3">{{user.email}}</h5>
						<v-btn @click="logout" block color="primary lighten-2" class="caption">
							Se déconnecter
						</v-btn>
					</div>
					<div v-else>
						<router-link :to="{ name: 'Login' }">
							<v-btn elevation="0" block color="primary lighten-2" class="caption secondary--text" :class="{'primary darken-1 text--darken-4': !$vuetify.theme.dark}">
								Se connecter
							</v-btn>
						</router-link>
					</div>
				</div>
			</template>
		</v-navigation-drawer>
	</nav>
</template>

<script>
import ButtonToggleTheme from './ButtonToggleTheme.vue'
import colors from 'vuetify/lib/util/colors'

export default {
	name: "TheHeader",
	components: { 
		ButtonToggleTheme 
	},
	data() {
		return {
			user: {
				name: "Pingoo",
				email: "jean.neymar@gmail.com",
			},
			colorNavIcon: colors.grey.lighten4,
			drawer: false,
			items: [
				{ text: 'Accueil', icon: 'mdi-home', route: 'Home'},
				{ text: 'Rechercher', icon: 'mdi-magnify', route: 'Search'},
			],
		}
	},
	computed: {
		loggedIn() {
			return false;
		},
		navWidth () {
			switch (this.$vuetify.breakpoint.name) {
				case 'xs': return 220
				case 'sm': return 240
				case 'md': return 260
				case 'lg': return 280
				case 'xl': return 300
				default: return 0
			}
		},
	},
	methods: {
		logout() {
			// TODO
		},
	}
}
</script>

<style scoped lang="scss">

#hamburger-lbl {
	/* Display & Box Model */
	margin: 0 15px;
	border: 0;
	/* Other */
	cursor: pointer;
	outline: none;
	pointer-events: none;

	span {
		/* Display & Box Model */
		display: block;
		position: relative;
		width: 32px;
		height: 3px;
		margin: 7px 0;
		transform-origin: 50% 50%;
		transition: transform 0.5s cubic-bezier(0.77, 0.2, 0.05, 1),
			background 0.5s cubic-bezier(0.77, 0.2, 0.05, 1), opacity 0.5s ease;		
	}
}

#openmenu-input {
	/* Display & Box Model */
	display: none;

	&:checked ~ label span:first-child {
		transform: translate(0, 10px) rotate(45deg) scale(0.9, 1);
	}
	&:checked ~ label span:nth-child(2) {
		opacity: 0;
		transform: scale(0.2, 0.2);
	}
	&:checked ~ label span:last-child {
		transform: translate(0, -10px) rotate(-45deg) scale(0.9, 1);
	}
}

</style>