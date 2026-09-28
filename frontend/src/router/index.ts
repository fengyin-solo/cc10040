import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Pipeline = () => import('@/views/pipeline/index.vue')
const Regulator = () => import('@/views/regulator/index.vue')
const Valve = () => import('@/views/valve/index.vue')
const Cathode = () => import('@/views/cathode/index.vue')
const Leak = () => import('@/views/leak/index.vue')
const Route = () => import('@/views/route/index.vue')
const Rush = () => import('@/views/rush/index.vue')
const Meter = () => import('@/views/meter/index.vue')
const Safetycheck = () => import('@/views/safetycheck/index.vue')
const Pipeage = () => import('@/views/pipeage/index.vue')
const Thirdparty = () => import('@/views/thirdparty/index.vue')
const Shutoff = () => import('@/views/shutoff/index.vue')
const Hazard = () => import('@/views/hazard/index.vue')
const Team = () => import('@/views/team/index.vue')
const Appliance = () => import('@/views/appliance/index.vue')
const Pressure = () => import('@/views/pressure/index.vue')
const Account = () => import('@/views/account/index.vue')
const Emergency = () => import('@/views/emergency/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/pipeline', name: 'pipeline', component: Pipeline },
    { path: '/regulator', name: 'regulator', component: Regulator },
    { path: '/valve', name: 'valve', component: Valve },
    { path: '/cathode', name: 'cathode', component: Cathode },
    { path: '/leak', name: 'leak', component: Leak },
    { path: '/route', name: 'route', component: Route },
    { path: '/rush', name: 'rush', component: Rush },
    { path: '/meter', name: 'meter', component: Meter },
    { path: '/safetycheck', name: 'safetycheck', component: Safetycheck },
    { path: '/pipeage', name: 'pipeage', component: Pipeage },
    { path: '/thirdparty', name: 'thirdparty', component: Thirdparty },
    { path: '/shutoff', name: 'shutoff', component: Shutoff },
    { path: '/hazard', name: 'hazard', component: Hazard },
    { path: '/team', name: 'team', component: Team },
    { path: '/appliance', name: 'appliance', component: Appliance },
    { path: '/pressure', name: 'pressure', component: Pressure },
    { path: '/account', name: 'account', component: Account },
    { path: '/emergency', name: 'emergency', component: Emergency },
  ],
})

export default router
