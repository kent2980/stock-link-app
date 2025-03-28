import { Box, Flex } from "@chakra-ui/react";
import { createFileRoute, Outlet, redirect } from "@tanstack/react-router";

import { isLoggedIn } from "@/hooks/useAuth";
import { HeaderStore } from "@/Store/HeaderStore";
import { useStore } from "@tanstack/react-store";
import Footer from "../components/Common/Footer";
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
  const { height } = useStore(HeaderStore, (state) => state);
  return (
    <Flex direction="column">
      <Header bg="linear-gradient(to right, #eef1f3, #fefefe)" />
      <Box
        mt={height}
        bg="linear-gradient(to right, #e9ebef, #eceff6)"
        h={"calc(100vh - " + height + "px)"}
        w={"100%"}
      >
        <Outlet />
      </Box>
      <Footer bg="linear-gradient(to right, #ffffff, #fefefe)" />
    </Flex>
  );
}

export default Layout;
