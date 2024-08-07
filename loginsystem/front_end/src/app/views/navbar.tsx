
"use client";
import { Avatar, Dropdown, Navbar } from "flowbite-react";
import { useRouter } from "next/navigation";
export function NavbarComp() {
  const router = useRouter();
  const handleSignOut = async () => {
    await fetch('/api/signout', { method: 'POST' });
    document.cookie = 'auth_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    router.push('/signin');
  };
  return (
    <Navbar fluid rounded>
      <Navbar.Brand href="https://flowbite-react.com">
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite React</span>
      </Navbar.Brand>

      {false ? (<>   <div className="flex md:order-2">
        <Dropdown
          arrowIcon={false}
          inline
          label={
            <Avatar alt="User settings" rounded />
          }
        >
          <Dropdown.Header>
            <span className="block text-sm">Bonnie Green</span>
            <span className="block truncate text-sm font-medium">name@flowbite.com</span>
          </Dropdown.Header>

          <Dropdown.Item href="/" onClick={handleSignOut}>Sign out</Dropdown.Item>
        </Dropdown>
        <Navbar.Toggle />
      </div></>) : (<>  <div className="flex md:order-2">
        <Navbar.Collapse>  <Navbar.Link href="/signin">signin</Navbar.Link>    </Navbar.Collapse>
      </div></>)}



      <Navbar.Collapse>
        <Navbar.Link href="/" active>
          Home
        </Navbar.Link>
        <Navbar.Link href="/products">products</Navbar.Link>
        z
        <Navbar.Link href="/about">about</Navbar.Link>
      </Navbar.Collapse>
    </Navbar>
  );
}
