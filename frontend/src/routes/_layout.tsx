import { Box, Flex } from "@chakra-ui/react";
import { createFileRoute, Outlet, redirect } from "@tanstack/react-router";

import Footer from "@/components/Common/Footer";
import Header from "@/components/Common/Header";
import AppSidebar from "@/components/Common/Sidebar";
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

const HEADER_HEIGHT = 20;
const FOOTER_HEIGHT = "60px";

function Layout() {
  return (
    <Flex direction="column">
      <Header headerHeight={HEADER_HEIGHT} />
      <Box
        w="100%"
        mx="auto"
        mt={HEADER_HEIGHT}
        mb={{ base: FOOTER_HEIGHT, md: 0 }}
      >
        <AppSidebar />
        <Box ml={{ base: 0, md: "60" }} bg="gray.50">
          <Outlet />
        </Box>
      </Box>
      <Footer h={FOOTER_HEIGHT} />
    </Flex>
  );
}

export default Layout;
