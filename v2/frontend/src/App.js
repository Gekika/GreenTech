// // // // // import logo from './logo.svg';
// // // // // import './App.css';

// // // // // function App() {
// // // // //   return (
// // // // //     <div className="App">
// // // // //       <header className="App-header">
// // // // //         <img src={logo} className="App-logo" alt="logo" />
// // // // //         <p>
// // // // //           Edit <code>src/App.js</code> and save to reload.
// // // // //         </p>
// // // // //         <a
// // // // //           className="App-link"
// // // // //           href="https://reactjs.org"
// // // // //           target="_blank"
// // // // //           rel="noopener noreferrer"
// // // // //         >
// // // // //           Learn React
// // // // //         </a>
// // // // //       </header>
// // // // //     </div>
// // // // //   );
// // // // // }

// // // // // export default App;



// // // // import React from "react";
// // // // import InventoryList from "./InventoryList"; // Import the InventoryList component

// // // // function App() {
// // // //   return (
// // // //     <div className="App">
// // // //       <header>
// // // //         <h1>Welcome to GreenTech Inventory System</h1>
// // // //       </header>
// // // //       <main>
// // // //         <InventoryList /> {/* Add the component here */}
// // // //       </main>
// // // //     </div>
// // // //   );
// // // // }

// // // // export default App;


// // // import React from "react";
// // // import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// // // import Navbar from "./components/Navbar";
// // // import Home from "./pages/Home";
// // // import Inventory from "./pages/Inventory";
// // // import Reports from "./pages/Reports";

// // // function App() {
// // //   return (
// // //     <Router>
// // //       <Navbar /> {/* Add Navbar to every page */}
// // //       <div className="container mx-auto">
// // //         <Routes>
// // //           <Route path="/" element={<Home />} />
// // //           <Route path="/inventory" element={<Inventory />} />
// // //           <Route path="/reports" element={<Reports />} />
// // //         </Routes>
// // //       </div>
// // //     </Router>
// // //   );
// // // }

// // // export default App;


// // const App = () => <h1>React Frontend is Working!</h1>;
// // export default App;


// import React, { useState, useEffect } from "react";

// const App = () => {
//   const [data, setData] = useState(null);
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     fetch("http://127.0.0.1:8000/inventory/homepage-data/")
//       .then((response) => response.json())
//       .then((data) => {
//         setData(data);
//         setLoading(false);
//       })
//       .catch((error) => {
//         console.error("Error fetching data:", error);
//         setLoading(false);
//       });
//   }, []);

//   if (loading) return <p>Loading...</p>;

//   if (!data) return <p>No data available.</p>;

//   return (
//     <div>
//       <h1>GreenTech Inventory Data</h1>
//       <ul>
//         {data.labels.map((label, index) => (
//           <li key={index}>
//             {label}: {data.datasets[0].data[index]}
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default App;
import React, { useState, useEffect } from "react";
import { Bar } from "react-chartjs-2";

const App = () => {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/inventory/homepage-data/")
      .then((response) => response.json())
      .then((data) => {
        const barData = {
          labels: data.labels,
          datasets: data.datasets.map((dataset) => ({
            ...dataset,
            borderWidth: 1,
          })),
        };
        setChartData(barData);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  if (!chartData) return <p>Loading...</p>;

  return (
    <div>
      <h1>GreenTech Inventory Chart</h1>
      <Bar data={chartData} />
    </div>
  );
};

export default App;
