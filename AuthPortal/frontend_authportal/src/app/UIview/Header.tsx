import React from "react";
import Link from "next/link";

export default function Header() {
  return (
    <div>
       <nav className="bg-gray-800 p-4">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex justify-between items-center">
          
          <Link href="/"className="text-white text-lg font-bold">Logo 
          </Link>
 
          <ul className="flex space-x-4">
            <li>
              <Link href="/signin"  className="text-white hover:text-gray-300">Sign In 
              </Link>
            </li>
            <li>
              <Link href="/signup " className="text-white hover:text-gray-300">Sign Up 
              </Link>
            </li>
            <li>
              <Link href="/heropage" 
                className="text-white hover:text-gray-300">products 
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    </div>
  );
}
