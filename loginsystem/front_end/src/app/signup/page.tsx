"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
import Link from "next/link"
import { Button } from "@/components/ui/button"
import 'react-phone-number-input/style.css'
import PhoneInput from 'react-phone-number-input'
import { useState } from "react"
import { Loader2 } from "lucide-react"

const fetcher = (url: string) => fetch(url).then((res) => res.json());
import {
    Form,
    FormControl,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from "@/components/ui/form"
import { useRouter } from "next/navigation"
import { Input } from "@/components/ui/input"
import { toast } from "@/components/ui/use-toast"

const FormSchema = z.object({
    username: z.string().min(2, { message: "Username must be at least 2 characters." }).default(""),
    email: z.string().email({ message: "Invalid email address." }).default(""),
    password: z.string().min(6, { message: "Password must be at least 6 characters." }).default(""),
    phone_number: z.string().min(10, { message: "Phone number must be at least 10 characters." }).default(""),
});

export default function InputForm() {
    const router = useRouter();
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<String|undefined>("");
    const form = useForm<z.infer<typeof FormSchema>>({
        resolver: zodResolver(FormSchema),
    })

    async function onSubmit(data: z.infer<typeof FormSchema>) {
        setLoading(true);
        const formData = new FormData()
        formData.append("username", data.username)
        formData.append("email", data.email)
        formData.append("password", data.password)
        formData.append("phone", data.phone_number)

        try {
            const registerResponse = await fetch(`http://localhost:8000/api/signup`, {
                method: "POST",
                body: formData
            })
            if (registerResponse.ok) {
                const data = await registerResponse.json()
                data.success
                router.replace("/")
            } else {
                const data = await registerResponse.json()
                console.log("data:",data.detail)
                setError(data.detail)
            }
        }
        catch (e) {
          setError("Some thing went wrong")
        } finally {
            setLoading(false);
        }
    }

    return (
        <>
         
            <div className="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
                <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                    <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign up for an account</h2>
                </div>

                <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                    <Form {...form}>
                        <form onSubmit={form.handleSubmit(onSubmit)} className="  space-y-6">
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
                                name="email"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>Email</FormLabel>
                                        <FormControl>
                                            <Input placeholder="Enter a Email" {...field} />
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

                            <FormField
                                control={form.control}
                                name="phone_number"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>Phone Number</FormLabel>
                                        <FormControl>
                                            <PhoneInput
                                                placeholder="Enter phone number"
                                                {...field} />
                                        </FormControl>

                                        <FormMessage />
                                    </FormItem>
                                )}
                            />

                            <div>
                                <FormMessage>{error}</FormMessage>
                                <Button type="submit" className="  w-full " disabled={loading}> 
                                {loading &&  <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
                              
                                Sign up</Button>
                            </div>


                        </form>
                    </Form>

                    <p className="mt-10 text-center text-sm text-gray-500">
                        Already have an account?
                        <Link href="/signin" className="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Sign in</Link>
                    </p>
                </div>
            </div>





        </>



    )
}