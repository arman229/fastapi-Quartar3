"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
import Link from "next/link"
import { Button } from "@/components/ui/button"
import 'react-phone-number-input/style.css'
import { useState } from "react"
import { useRouter } from "next/navigation"
import { Loader2 } from "lucide-react"
import Cookies from 'js-cookie';
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"

const FormSchema = z.object({
  username: z.string({ required_error: "Provide username" }),
  password: z.string({ required_error: "Provide password" }),
});

export default function Signin() {
  const [error, setError] = useState<String | undefined>("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();
  const form = useForm<z.infer<typeof FormSchema>>({
    resolver: zodResolver(FormSchema),
  })

  async function onSubmit(data: z.infer<typeof FormSchema>) {
    setLoading(true);
    const formData = new FormData()
    formData.append("username", data.username)
    formData.append("password", data.password)

    try {
      const registerResponse = await fetch(`http://localhost:8000/api/signin`, {
        method: "POST",
        body: formData
      })
      if (registerResponse.ok) {
        const data = await registerResponse.json()
        Cookies.set('auth_token', data.access_token);
        router.replace("/")
      } else {
        const data = await registerResponse.json()
        console.log("data:", data.detail)
        setError(data.detail)
      }
    }
    catch (e: any) {
      setError("Some thing went wrong:" + e.message)
    } finally {
      setLoading(false);
    }
  }

  return (

    <>
      <div className="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in for an account</h2>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <Form {...form}>
            <form className="  space-y-6">
              <FormField
                control={form.control}
                name="username"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Username</FormLabel>
                    <FormControl>
                      <Input placeholder="Enter a username" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />



              <FormField
                control={form.control}
                name="password"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Password</FormLabel>
                    <FormControl>
                      <Input placeholder="Enter a password" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <Button onClick={form.handleSubmit(onSubmit)} className="  w-full " disabled={loading}>
                {loading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}Sign in</Button>
              <FormMessage className="text-center">{error}</FormMessage>


            </form>
          </Form>

          <p className="mt-10 text-center text-sm text-gray-500">
            Not a member?
            <Link href="/signup" className="font-semibold leading-6 text-indigo-600 hover:text-indigo-500"> Sign up</Link>
          </p>
        </div>
      </div>






    </>



  )
}