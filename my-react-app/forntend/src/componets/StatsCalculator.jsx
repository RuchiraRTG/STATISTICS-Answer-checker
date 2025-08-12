import React, { useState } from "react";
import axios from "axios";
import "../styles/StatsCalculator.css";

export default function StatsCalculator() {
  const [numbers, setNumbers] = useState("");
  const [results, setResults] = useState(null);

  const handleCalculate = async () => {
    let arr = numbers
      .split(",")
      .map((n) => parseFloat(n.trim()))
      .filter((n) => !isNaN(n));

    if (arr.length === 0) {
      alert("Please enter valid numbers separated by commas.");
      return;
    }

    try {
      const res = await axios.post("http://127.0.0.1:8000/calculate", {
        numbers: arr
      });
      setResults(res.data);
    } catch (error) {
      console.error(error);
      alert("Error connecting to backend.");
    }
  };

  return (
    <div className="stats-container">
      <h1>📊 Statistics Calculator</h1>
      <textarea
        placeholder="Enter numbers separated by commas (e.g., 5, 2, 9, 1)"
        value={numbers}
        onChange={(e) => setNumbers(e.target.value)}
      ></textarea>
      <button onClick={handleCalculate}>Calculate</button>

      {results && (
        <div className="results">
          <h2>Results</h2>
          <ul>
            <li><strong>Length:</strong> {results.length}</li>
            <li><strong>Before Sorting:</strong> {results.before.join(", ")}</li>
            <li><strong>After Insertion Sort:</strong> {results.after.join(", ")}</li>
            <li><strong>Max:</strong> {results.max}</li>
            <li><strong>Min:</strong> {results.min}</li>
            <li><strong>Range:</strong> {results.range}</li>
            <li><strong>Most Frequent:</strong> {results.mostFrequent}</li>
            <li><strong>Median:</strong> {results.median}</li>
            <li><strong>Q1:</strong> {results.Q1}</li>
            <li><strong>Q3:</strong> {results.Q3}</li>
            <li><strong>IQR:</strong> {results.IQR}</li>
            <li><strong>Upper Fence:</strong> {results.upperFence}</li>
            <li><strong>Lower Fence:</strong> {results.lowerFence}</li>
          </ul>
        </div>
      )}
    </div>
  );
}
