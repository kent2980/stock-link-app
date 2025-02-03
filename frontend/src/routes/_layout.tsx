import { Box, Flex, Spinner } from "@chakra-ui/react";
import { Outlet, createFileRoute, redirect } from "@tanstack/react-router";

import { useStore } from "@tanstack/react-store";
import Header from "../components/Common/Header";
import useAuth, { isLoggedIn } from "../hooks/useAuth";
import { HeaderStore } from "../Store/HeaderStore";

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
  const { height } = useStore(HeaderStore, (state) => state);
  return (
    <Flex maxW="large" h="auto" position="relative">
      <Header />
      {isLoading ? (
        <Flex
          justify="center"
          align="center"
          height="100vh"
          width="100vw"
          mt={height}
          ml={{ base: 0, md: 0 }}
        >
          <Spinner size="xl" color="ui.main" />
        </Flex>
      ) : (
        <Box mt={height} ml={{ base: 0, md: 0 }} width="100vw">
          <Outlet />
        </Box>
      )}
      {/* <UserMenu /> */}
    </Flex>
  );
}
