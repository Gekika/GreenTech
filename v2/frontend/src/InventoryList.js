import React, { useEffect, useState } from "react"; // Import React hooks
import API from "./api"; // Import the API object created in api.js

const InventoryList = () => {
  const [products, setProducts] = useState([]); // State to store the products
  const [loading, setLoading] = useState(true); // State to handle loading
  const [error, setError] = useState(null); // State to handle errors

  // Fetch data when the component loads
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await API.get("/inventory/products/"); // Fetch from the backend
        setProducts(response.data); // Store the data in the products state
      } catch (err) {
        setError("Failed to fetch products. Please try again."); // Handle errors
      } finally {
        setLoading(false); // Stop loading spinner
      }
    };

    fetchProducts(); // Call the fetch function
  }, []); // Empty dependency array ensures it runs only once when the component mounts

  // Show loading spinner
  if (loading) return <div>Loading products...</div>;

  // Show error message if there's an error
  if (error) return <div>Error: {error}</div>;

  // Display products in a list
  return (
    <div>
      <h1>Inventory</h1>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            <strong>{product.name}</strong> - Stock: {product.stock_quantity}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default InventoryList; // Export the component
