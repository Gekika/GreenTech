<template>
    <div>
      <h1>Product Inventory</h1>
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">{{ error }}</div>
      <div v-else>
        <ProductItem v-for="product in products" :key="product.id" :product="product" />
      </div>
    </div>
  </template>
  
  <script>
  import axiosClient from '../api/axiosClient';
  import ProductItem from './ProductItem.vue';
  
  export default {
    components: {
      ProductItem,
    },
    data() {
      return {
        products: [],
        loading: true,
        error: null,
      };
    },
    async created() {
      try {
        const response = await axiosClient.get('/inventory/products/'); // Endpoint to fetch products
        this.products = response.data;
      } catch (err) {
        this.error = 'Failed to load products.';
      } finally {
        this.loading = false;
      }
    },
  };
  </script>
  
  <style>
  /* Add your styles here */
  </style>
  