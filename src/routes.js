import VueRouter from 'vue-router';

let routes = [
	{
		path: '/',
		component: require('./Home.vue').default
	}
]

export default new VueRouter ({
	routes
});