import Image from "next/image";

import Link from "next/link";

export default function Home() {
  return (
    <div className="flex justify-center items-center h-[100vh] gap-2">
      <button className="p-3 bg-blue-400 rounded-lg">
        <Link href="/signup"> Sign Up</Link>
      </button>

      <button className="p-3 bg-blue-400 rounded-lg">
        <Link href="/signin"> Sign In</Link>
      </button>
    </div>
  );
}
