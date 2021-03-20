import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

// Default colors in theme
// {
// 	primary: '#1976D2',
// 	secondary: '#424242',
// 	accent: '#82B1FF',
// 	error: '#FF5252',
// 	info: '#2196F3',
// 	success: '#4CAF50',
// 	warning: '#FFC107',
//  }

export default new Vuetify({
	theme: {
		themes: {
			light: {
				primary: colors.blue.lighten3,
				secondary: colors.orange.darken4,
				accent: colors.green.base,
				background: colors.grey.lighten4,
			},
			dark: {
				primary: colors.purple.darken4,
				secondary: colors.green.lighten1,
				background: colors.grey.darken4,
			},
		},
	},
});
