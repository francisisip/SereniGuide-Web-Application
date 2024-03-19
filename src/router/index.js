import {createRouter, createWebHistory} from 'vue-router'

import Input from '../views/Input.vue'
import Results from '../views/Results.vue'

const routes = [
    {
        path: '/input',
        name: 'Input',
        component: Input
    },
    {
        path: '/results',
        name:'Results',
        component: Results
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router