import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";

import Home from "../views/Home.vue";
import Login from "../views/users/Login"
import Register from "../views/users/Register"
import MyActivities from "../views/activities/MyActivities"
import ActivityDetails from "../views/activities/ActivityDetails"
import ActivityCreate from "../views/activities/ActivityCreate"
import Search from "../views/activities/Search"
import SearchResults from "../views/activities/SearchResults"
import NotFound from "../views/NotFound"


Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		name: "Home",
		component: Home
	},

	{
		path: "/home",
		redirect: "/"
	},

	{
		path: "/login",
		name: "Login",
		component: Login,
		meta: {
			requiresVisitor: true,
		},
	},

	{
		path: "/register",
		name: "Register",
		component: Register,
		meta: {
			requiresVisitor: true,
		},
	},

	{
		path: "/search",
		name: "Search",
		component: Search
	},

	{
		path: "/search/results",
		name: "Results",
		component: SearchResults
	},

	{
		path: "/activity/create",
		name: "ActivityCreate",
		component: ActivityCreate,
		meta: {
			requiresAuth: true
		},
	},

	{
		path: "/activity/:id",
		name: "ActivityDetails",
		component: ActivityDetails,
		props: true
	},

	{
		path: "/myactivities",
		name: "MyActivities",
		component: MyActivities,
		props: true,
		meta: {
			requiresAuth: true
		},
	},
	// Comments: ctrl+k+c
	// Uncomments: ctrl+k+u
	// {
	// 	path: "/activity/add_rating",
	// 	name: "TODO",
	// 	component: TODO,
	// 	meta:	{ requiresAuth: true }
	// },
	// {
	// 	path: "/activity/edit",
	// 	name: "TODO",
	// 	component: TODO,
	// 	meta:	{ requiresAuth: true }
	// },
	{
		path: "/:catchAll(.*)",
		name: NotFound,
		component: NotFound
	}
	// { 
	// 	path: "/about",
	// 	name: "About",
	// 	// route level code-splitting
	// 	// this generates a separate chunk (about.[hash].js) for this route
	// 	// which is lazy-loaded when the route is visited.
	// 	component: () =>
	// 		import(/* webpackChunkName: "about" */ "../views/About.vue")
	// }
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes
});

// Global Before Guards 
router.beforeEach((to, from, next) => {
	if (to.matched.some(record => record.meta.requiresAuth))
	{
		if (!store.getters.loggedIn) 
		{
			next({name: 'Login'})
		}
		else 
			next()
	}
	else if(to.matched.some(record => record.meta.requiresVisitor))
	{
		!store.dispatch("logout");
		next()
	}
	else
	{
		next() 
	}
})

export default router;
