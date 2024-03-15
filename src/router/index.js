import {createRouter, createWebHistory} from 'vue-router'

import Home from '../views/Input.vue'

const routes = [
    {
    path: '/input',
    name: 'Input',
    component: Home
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router