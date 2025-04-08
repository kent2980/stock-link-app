import { Box, Flex } from "@chakra-ui/react";
import { createFileRoute, Outlet, redirect } from "@tanstack/react-router";

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

const HEADER_HEIGHT = "110px";
const FOOTER_HEIGHT = "60px";

function Layout() {
  return (
    <Flex direction="column">
      <Box w={"100%"} pb={FOOTER_HEIGHT}>
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
