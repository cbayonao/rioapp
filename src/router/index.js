import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Bdua from '../views/Bdua.vue'
import Sisben from '../views/Sisben.vue'
import Entintrio from '../views/Entintrio.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/bdua',
    name: 'Bdua',
    component: Bdua
  },
  {
    path: '/sisben',
    name: 'Sisben',
    component: Sisben
  },
  {
    path: '/entintrionegro',
    name: 'Entintrio',
    component: Entintrio
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
