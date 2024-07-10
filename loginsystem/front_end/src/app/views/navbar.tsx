
"use client";

import { Avatar, Dropdown, Navbar } from "flowbite-react";

export function NavbarComp() {
  return (
    <Navbar fluid rounded>
      <Navbar.Brand href="https://flowbite-react.com"> 
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite React</span>
      </Navbar.Brand>
      <div className="flex md:order-2">
        <Dropdown
          arrowIcon={false}
          inline
          label={
            <Avatar alt="User settings"  rounded />
          }
        >
          <Dropdown.Header>
            <span className="block text-sm">Bonnie Green</span>
            <span className="block truncate text-sm font-medium">name@flowbite.com</span>
          </Dropdown.Header>
          <Dropdown.Item href="/signup">Sign up</Dropdown.Item>
          <Dropdown.Item href="/signin">Sign in</Dropdown.Item>
          <Dropdown.Item href="/">Sign out</Dropdown.Item>
        </Dropdown>
        <Navbar.Toggle />
      </div>
      <Navbar.Collapse>
        <Navbar.Link href="/" active>
          Home
        </Navbar.Link>
        <Navbar.Link href="/products">products</Navbar.Link> 
         </Navbar.Collapse>
    </Navbar>
  );
}
