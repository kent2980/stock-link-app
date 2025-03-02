import { Flex } from "@chakra-ui/react";
import { Outlet, createFileRoute, redirect } from "@tanstack/react-router";

import { isLoggedIn } from "@/hooks/useAuth";
import Header from "../components/Common/Header";
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
  return (
    <Flex direction="column" h="100vh">
      <Header />
      <Flex flex="1" direction="column" p={4} overflowY="auto">
        <Outlet />
      </Flex>
    </Flex>
  );
}

export default Layout;
