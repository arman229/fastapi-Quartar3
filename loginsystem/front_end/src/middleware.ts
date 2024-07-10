 

import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export async function middleware(request: NextRequest) {
  if (request.nextUrl.pathname.startsWith('/products')) {
    const authToken = request.cookies.get('auth_token')?.value;
    if (!authToken) {
      return NextResponse.rewrite(new URL('/signin', request.url));
    } 
    else {
      try {
        const validationResponse = await validateauthtoken(authToken);
        if (!validationResponse.valid) {
          return NextResponse.rewrite(new URL('/signin', request.url));
        }
      } 
      catch (error) {
        console.error('Error validating token:', error); 
      }
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: '/:path*',
};


const validateauthtoken = async (auth_token: string) => {
  const token_in_form_data = new FormData()
  token_in_form_data.append("token", auth_token)

  const validationTokenresponse = await fetch("http://localhost:8000/api/validation_token", { method: 'POST', body: token_in_form_data })
  if (validationTokenresponse.status! == 200) {
    throw new Error("token is not valid")
  }
  return await validationTokenresponse.json()
}