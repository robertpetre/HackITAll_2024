import React, { useEffect, useState } from "react";

const NewsDashboard = () => {
    const [data, setData] = useState([]);
    const [expandedCards, setExpandedCards] = useState({}); // Track which cards are expanded

    // Fetch data from the backend
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch("http://localhost:5000/api/");
                if (!response.ok) {
                    throw new Error("Failed to fetch data");
                }
                const result = await response.json();
                setData(result);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };

        fetchData();
    }, []);

    const toggleCard = (index) => {
        setExpandedCards((prev) => ({
            ...prev,
            [index]: !prev[index],
        }));
    };

    const getSentimentClass = (mean) => {
        if (mean <= 0) {
            return "bg-red-500"; // Negative sentiment
        } else if (mean > 0 && mean <= 0.7) {
            return "bg-yellow-500"; // Neutral sentiment
        } else {
            return "bg-green-500"; // Positive sentiment
        }
    };

    return (
        <div className="min-h-screen bg-gray-100 flex flex-col items-center p-4">
            <h1 className="text-2xl md:text-4xl font-bold text-gray-800 mb-6">
                News Sentiment Dashboard
            </h1>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 w-full max-w-7xl">
                {data.map((item, index) => (
                    <div
                        key={index}
                        className={`bg-white p-4 shadow-md rounded-md border border-gray-300 transition-all duration-300 ${expandedCards[index] ? "h-auto" : "h-20 overflow-hidden"
                            }`}
                    >
                        {/* Clickable Header to Toggle */}
                        <div
                            className="cursor-pointer flex justify-between items-center"
                            onClick={() => toggleCard(index)}
                        >
                            <span className="text-lg font-semibold text-gray-700">
                                {item.tag}
                            </span>
                            <span
                                className={`w-4 h-4 rounded-full ${getSentimentClass(item.mean)}`}
                                title={`Mean Sentiment: ${item.mean}`}
                            ></span>
                        </div>

                        {/* News List (Only shown when card is expanded) */}
                        {expandedCards[index] && (
                            <div>
                                <ul className="mt-4 space-y-2">
                                    {item.news.map((newsItem, i) => (
                                        <li key={i} className="flex items-center space-x-2">
                                            <a href={newsItem[2]} className="flex-1 underline">
                                                {newsItem[3]} {/* Summary */}
                                            </a>
                                            <span
                                                className={`w-3 h-3 rounded-full ${getSentimentClass(newsItem[1] === "true" ? 1 : (newsItem[1] === "false" ? -1 : 0.5))}`}
                                                title={`Sentiment: ${newsItem[1]}`}
                                            ></span>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        )}
                    </div>
                ))}
            </div>
            <div className="w-full mt-4">
                <iframe
                    src="https://caa0fa6b2f74871573.gradio.live"
                    height="800"
                    className="w-full border rounded-md shadow-md"
                    title="Gradio Interface"
                ></iframe>
            </div>
        </div>
    );
};

export default NewsDashboard;
