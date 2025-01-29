import React from "react";
import InventoryList from "../InventoryList";

const Inventory = () => {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Inventory</h1>
      <InventoryList />
    </div>
  );
};

export default Inventory;
