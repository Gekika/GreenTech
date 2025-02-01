

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
