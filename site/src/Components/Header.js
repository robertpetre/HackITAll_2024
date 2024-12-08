import React from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "./Navbar";
import Fade from "react-reveal/Fade";
import icon from "../Assets/icon.png";

function Header() {
  const navigate = useNavigate();

  const handleNavigation = () => {
    navigate("/dashboard");
  };

  return (
    <div className="from-[#1d2620] to-[#475547] bg-gradient-to-b w-full h-full relative">
      {/* Navbar */}
      <Navbar className="z-50 top-0 left-0 w-full px-10 lg:px-28" />

      {/* Content */}
      <div className="grid place-items-center h-full px-10 lg:px-28">
        <div className="lg:flex items-center justify-center">
          {/* Text Section */}
          <Fade left cascade>
            <div className="lg:w-[800px] container text-center lg:text-left">
              <h1 className="font-[1000] xl:text-[4.2rem] lg:text-[3rem] md:text-[3.2rem] text-3xl lg:w-[79%] text-white xl:leading-[5rem] md:leading-[4rem]">
                Stay Updated on{" "}
                <span className="text-transparent bg-clip-text bg-gradient-to-br from-[#64f185] to-[#4af063]">
                  Market Trends
                </span>
              </h1>

              <div className="xl:flex justify-start mt-7">
                <div>
                  <button
                    onClick={handleNavigation}
                    className="rounded px-7 py-3 bg-[#3ed461] text-white relative group hover:text-white overflow-hidden c-btn tracking-wider"
                  >
                    <span className="absolute inset-0 bg-[#5ae66f]"></span>
                    <span className="absolute inset-0 flex justify-center items-center">
                      Try Now!
                    </span>
                    Try Now!
                  </button>
                </div>
                <p className="xl:w-[50%] lg:w-[70%] md:w-[80%] text-[14px] text-gray-400 lg:leading-6 xl:pl-5 xl:pt-0 pt-4 pb-4">
                  Stay ahead of the market with real-time news, categorized by stock and sentiment. Get an easy-to-understand view of how major financial stories are impacting the stock market, powered by AI sentiment analysis.
                </p>
              </div>
            </div>
          </Fade>

          <div className="flex justify-center items-center">
            <Fade right cascade>
              <div>
                <img
                  src={icon}
                  className="w-[800px] lg:w-[700px] md:w-[600px] xl:w-[500px] h-auto"
                  alt="Chart"
                />
              </div>
            </Fade>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Header;
