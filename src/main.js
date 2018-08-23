import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './routes.js'
import vueHeadful from 'vue-simple-headful'

Vue.use(vueHeadful)
Vue.use(VueRouter)

new Vue({
  el: '#app',
  render: h => h(App),
  router
})