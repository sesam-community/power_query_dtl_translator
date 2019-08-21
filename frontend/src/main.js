import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import Speed from './components/Speed'

Vue.config.productionTip = false
Vue.use(VueRouter)

const routes = [
  { path: '/token', component: Speed },
  { path: '/get_statistics', component: Speed }
]

const router = new VueRouter({
  routes,
  mode : 'history'
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
});