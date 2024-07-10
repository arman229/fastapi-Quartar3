'use client'

import Image from "next/image"
export const ImagesGallery=()=>{
    return(

        <>
         <section className="flex items-center justify-center h-screen bg-cover bg-center" style={{ backgroundImage: "url('https://i.pinimg.com/736x/58/bd/4f/58bd4fc9ebfccc1f2de419529bbf1a12.jpg')" }}>
      <div className="text-center  px-4">
        <h1 className="text-5xl font-bold mb-4">Welcome to Our Website</h1>
        <p className="text-xl mb-8">Your journey starts here. Discover amazing content and experiences.</p>
        <button className="bg-pink-500 hover:bg-pink-700 text-white font-bold py-2 px-4 rounded">
          Get Started
        </button>
      </div>
    </section>

        </>
    )
}