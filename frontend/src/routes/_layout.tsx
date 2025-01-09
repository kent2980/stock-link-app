import { Box, Flex, Spinner } from "@chakra-ui/react";
import { Outlet, createFileRoute, redirect } from "@tanstack/react-router";

import { useEffect, useRef, useState } from "react";
import Header from "../components/Common/Header";
import Sidebar from "../components/Common/Sidebar";
import UserMenu from "../components/Common/UserMenu";
import useAuth, { isLoggedIn } from "../hooks/useAuth";

export const Route = createFileRoute("/_layout")({
  component: Layout,
  beforeLoad: async () => {
    if (!isLoggedIn()) {
      throw redirect({
        to: "/login",
      });
    }
  },
});

function Layout() {
  const { isLoading } = useAuth();
  const headerRef = useRef<HTMLDivElement>(null);
  const sidebarRef = useRef<HTMLDivElement>(null);

  const [headerHeight, setHeaderHeight] = useState(0);
  const [sidebarWidth, setSidebarWidth] = useState(0);

  useEffect(() => {
    if (headerRef.current) {
      setHeaderHeight(headerRef.current.offsetHeight);
      console.log(headerRef.current.offsetHeight);
    }
    if (sidebarRef.current) {
      setSidebarWidth(sidebarRef.current.offsetWidth);
      console.log(sidebarRef.current.offsetWidth);
    }
  }, []);

  return (
    <Flex maxW="large" h="auto" position="relative">
      <Header ref={headerRef} />
      <Sidebar marginTop={`${headerHeight}px`} ref={sidebarRef} />
      {isLoading ? (
        <Flex
          justify="center"
          align="center"
          height="100vh"
          width="100vw"
          mt={`${headerHeight}px`}
          ml={{ base: 0, md: `${sidebarWidth}px` }}
        >
          <Spinner size="xl" color="ui.main" />
        </Flex>
      ) : (
        <Box
          mt={`${headerHeight}px`}
          ml={{ base: 0, md: `${sidebarWidth}px` }}
          width="100vw"
        >
          <Outlet />
        </Box>
      )}
      <UserMenu />
    </Flex>
  );
}
