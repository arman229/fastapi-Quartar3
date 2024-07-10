 

// import { parseCookies, setCookie, destroyCookie } from 'nookies';

// const TOKEN_NAME = 'authToken';

// export const setAuthToken = (token:any) => {
//   setCookie(null, TOKEN_NAME, token, {
//     maxAge: 30 * 24 * 60 * 60, // 30 days expiry
//     path: '/',
//     secure: process.env.NODE_ENV === 'production',
//     sameSite: 'strict',
//     httpOnly: true,
//   });
// };

// export const getAuthToken = () => {
//   const cookies = parseCookies();
//   return cookies[TOKEN_NAME] || null;
// };

// export const removeAuthToken = () => {
//   destroyCookie(null, TOKEN_NAME);
// };
