import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./Components/Header";
import Companies from "./Components/Companies";
import NewsSentiment from "./Components/NewsSentiment";
import "./app.css";

function App() {
  return (
    <Router>
      <Routes>
        {/* Home Route */}
        <Route
          path="/"
          element={
            <div className="h-screen flex flex-col">
              <div className="lg:h-4/5 h-full">
                <Header />
              </div>
              <div className="lg:h-1/5 h-fit">
                <Companies />
              </div>
            </div>
          }
        />
        {/* Dashboard Route */}
        <Route path="/dashboard" element={<NewsSentiment />} />
      </Routes>
    </Router>
  );
}

export default App;
