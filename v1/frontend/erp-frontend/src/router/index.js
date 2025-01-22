import { createRouter, createWebHistory } from 'vue-router';
import InventoryView from '../views/InventoryView.vue';

const routes = [
  { path: '/', component: InventoryView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
