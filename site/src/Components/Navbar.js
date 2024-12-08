import { MenuIcon, XIcon } from "@heroicons/react/outline";
import React, { useState } from "react";

import { Disclosure } from "@headlessui/react";
import { HashLink } from "react-router-hash-link";

const navigation = [
  { name: "Home", href: "/", current: true },
  { name: "Dashboard", href: "/dashboard", current: false },
];

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

export default function Navbar({ className }) {
  const [navs, setNavs] = useState(navigation);

  const handleActive = (nav) => {
    navs.forEach((e) => (e.current = e.name === nav.name));
    setNavs([...navs]);
  };

  return (
    <Disclosure as="nav" className={`bg-transparent ${className}`}>
      {({ open }) => (
        <>
          <div className="w-full h-fit">
            <div className="relative flex items-center justify-between h-16">
              <div className="flex-shrink-0 flex items-center pl-4 lg:pl-8">
                <h1 className="font-bold text-white">DailyInsights</h1>
              </div>

              <div className="hidden sm:block">
                <div className="flex justify-center space-x-4">
                  {navs.map((item) => (
                    <HashLink
                      onClick={() => handleActive(item)}
                      smooth
                      key={item.name}
                      to={item.href}
                      className={classNames(
                        item.current
                          ? "text-transparent bg-clip-text bg-gradient-to-br from-[#64f185] to-[#4af063] md:text-xs lg:text-base"
                          : "text-gray-300",
                        "px-3 py-2 rounded-md text-sm font-medium md:text-xs lg:text-base hover:text-white hover:scale-110 ease-in duration-200"
                      )}
                      aria-current={item.current ? "page" : undefined}
                    >
                      {item.name}
                    </HashLink>
                  ))}
                </div>
              </div>

              <div className="inset-y-0 right-0 flex items-center sm:hidden">
                <Disclosure.Button className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
                  <span className="sr-only">Open main menu</span>
                  {open ? (
                    <XIcon className="block h-6 w-6" aria-hidden="true" />
                  ) : (
                    <MenuIcon className="block h-6 w-6" aria-hidden="true" />
                  )}
                </Disclosure.Button>
              </div>

              <div className="hidden sm:flex items-center pr-4 lg:pr-8">
                <button className="text-white border rounded px-7 py-2 md:px-5 hover:text-white c-btn relative tracking-wider overflow-hidden">
                  <span className="absolute inset-0 bg-gradient-to-br from-[#64f185] to-[#4af063]"></span>
                  <span className="absolute inset-0 flex justify-center items-center">
                    Contact Us
                  </span>
                  Contact Us
                </button>
              </div>
            </div>
          </div>

          <Disclosure.Panel className="sm:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1">
              {navs.map((item) => (
                <Disclosure.Button
                  key={item.name}
                  as="a"
                  href={item.href}
                  onClick={() => handleActive(item)}
                  className={classNames(
                    item.current
                      ? "bg-transparent text-white"
                      : "text-gray-300 hover:bg-gray-700 hover:text-white",
                    "block px-3 py-2 rounded-md text-base font-medium"
                  )}
                  aria-current={item.current ? "page" : undefined}
                >
                  {item.name}
                </Disclosure.Button>
              ))}
            </div>
          </Disclosure.Panel>
        </>
      )}
    </Disclosure>
  );
}
