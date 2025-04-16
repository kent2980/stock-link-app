import { Box, Flex } from "@chakra-ui/react";
import { createFileRoute, Outlet, redirect } from "@tanstack/react-router";

import Header from "@/components/Common/Header";
import ChildSidebar from "@/components/Desktop/ChildSidebar";
import Sidebar from "@/components/Desktop/Sidebar";
import { isLoggedIn } from "@/hooks/useAuth";
import Footer from "../components/Common/Footer";

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
      <Header h={{ base: HEADER_HEIGHT, md: "60px" }} />
      <Sidebar pt="60px" />
      <ChildSidebar pt="60px" />
      <Box pb={{ base: 0, md: FOOTER_HEIGHT }} pt={HEADER_HEIGHT}>
        <Outlet />
      </Box>
      <Footer
        bg="linear-gradient(to right, #ffffff, #fefefe)"
        h={FOOTER_HEIGHT}
      />
    </Flex>
  );
}

export default Layout;
