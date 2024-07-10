import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
export async function middleware(request: NextRequest) {

  const protected_routes = ['/products', '/about']

  if (protected_routes.some((route: string) => request.nextUrl.pathname.startsWith(route))) {
    const authToken = request.cookies.get('auth_token')?.value;
    console.log('Auth token:', authToken);
    if (!authToken) {
      console.log('No auth token found, redirecting to signin');
      return NextResponse.rewrite(new URL('/signin', request.url));
    }
    else {
      try {
        const checkApifun = await validation_authToken(authToken);
        if (!checkApifun.valid) {
          console.log('Token invalid, redirecting to signin');
          return NextResponse.rewrite(new URL('/signin', request.url));
        }
        else {
          return NextResponse.next();
        }
      } catch (error) {

      }

    }

  }

}
export const config = {
  matcher: '/:path*',
};

const validation_authToken = async (auth_token: string) => {
  const token_in_form_data = new FormData()
  token_in_form_data.append('token', auth_token)
  const validationTokenRes = await fetch('http://localhost:8000/api/validate_token', { method: 'POST', body: token_in_form_data })

  if (validationTokenRes.status !== 200) {
    throw new Error('Token is not valid')
  }

  return await validationTokenRes.json()

}