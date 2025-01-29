import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-green-600 text-white p-4">
      <div className="container mx-auto flex justify-between">
        <h1 className="text-xl font-bold">GreenTech Inventory</h1>
        <ul className="flex space-x-4">
          <li>
            <Link to="/" className="hover:underline">Home</Link>
          </li>
          <li>
            <Link to="/inventory" className="hover:underline">Inventory</Link>
          </li>
          <li>
            <Link to="/reports" className="hover:underline">Reports</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
