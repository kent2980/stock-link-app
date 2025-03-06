import { Flex } from "@chakra-ui/react";
import { createFileRoute, Outlet, redirect } from "@tanstack/react-router";

import Sidebar from "@/components/Common/Sidebar";
import { isLoggedIn } from "@/hooks/useAuth";
import { HeaderStore } from "@/Store/HeaderStore";
import { useStore } from "@tanstack/react-store";
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
      <Header />
      <Flex
        flex="1"
        overflow="hidden"
        mt={height}
        position="relative"
        flexDirection="row"
      >
        <Sidebar minW="25vw" />
        <Flex
          flex="1"
          direction="column"
          p={{ base: 0, md: 4 }}
          overflowY="auto"
          bg="ui.light"
          maxW={{ base: "100%", md: "720px" }}
          h={`calc(100vh - ${height}px)`}
        >
          <Outlet />
        </Flex>
      </Flex>
    </Flex>
  );
}

export default Layout;
