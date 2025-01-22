<template>
    <div id="app">
      <h1>ERP Frontend</h1>
      <router-view /> <!-- This will render the active route component -->
    </div>
  </template>
  
  <script>
  export default {
    name: 'App',
  };
  </script>
  
  <style>
  /* Add global styles here */
  body {
    font-family: Arial, sans-serif;
  }
  </style>
  