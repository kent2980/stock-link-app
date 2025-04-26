import { Box, Flex } from "@chakra-ui/react";
import { createFileRoute, Outlet, redirect } from "@tanstack/react-router";

import Header from "@/components/Common/Header";
import { isLoggedIn } from "@/hooks/useAuth";

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

const HEADER_HEIGHT = "40px";
const FOOTER_HEIGHT = "50px";

function Layout() {
  return (
    <Flex direction="column">
      <Header />
      <Box w="100%" mx="auto">
        <Outlet />
      </Box>
    </Flex>
  );
}

export default Layout;
