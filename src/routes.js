import VueRouter from 'vue-router'


let routes = [
	{
		path: '/',
		name: 'home',
		component: require('./Home.vue').default
	},
	{
		path: '/:slug',
		name: 'single-article',
		component: require('./Article.vue').default
	}
]

export default new VueRouter ({
	mode: 'history',
	routes
});