import React from 'react';
import Fade from "react-reveal/Fade";
import yahoo from "../Assets/Yahoo.svg";
import mw from "../Assets/mw.svg";
import inv from "../Assets/inv.svg";

function Companies() {
  return (
    <div className="h-full from-[#1f3217] to-[rgb(25,53,40)] bg-gradient-to-r lg:px-28 px-4">
      <Fade bottom cascade>
        <p className="text-white font-semibold text-center pt-4 whitespace-nowrap">
          Powered By
        </p>
        <div className="lg:flex justify-evenly pt-4 grid grid-cols-2 md:grid-cols-3 gap-10">
          <img
            src={yahoo}
            alt="Yahoo"
            className="w-40 h-20 object-contain"
          />
          <img
            src={mw}
            alt="Market Watch"
            className="w-40 h-20 object-contain"
          />
          <img
            src={inv}
            alt="Investing.com"
            className="w-40 h-20 object-contain"
          />
        </div>
      </Fade>
    </div>
  );
}

export default Companies;
