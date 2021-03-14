import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({
	theme: {
		themes: {
			light: {
				// Default colors in theme
				// primary: '#1976D2',
				// secondary: '#424242',
				// accent: '#82B1FF',
				// error: '#FF5252',
				// info: '#2196F3',
				// success: '#4CAF50',
				// warning: '#FFC107',
				background: colors.grey.lighten4,
			},
			dark: {
				background: colors.grey.darken4,
			},
		},
	},
});
