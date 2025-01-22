<template>
    <div class="product-item">
      <h3>{{ product.name }}</h3>
      <p>Category: {{ product.category }}</p>
      <p>Stock: {{ product.stock }}</p>
      <p>Price: {{ product.price }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      product: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  .product-item {
    border: 1px solid #ccc;
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 4px;
  }
  </style>
  