import { Box, Flex, Spinner } from "@chakra-ui/react";
import { Outlet, createFileRoute, redirect } from "@tanstack/react-router";

import Header from "../components/Common/Header";
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

  return (
    <Box>
      <Header />
      {isLoading ? (
        <Flex justify="center" align="center" height="100vh" width="full">
          <Spinner size="xl" color="ui.main" />
        </Flex>
      ) : (
        <Outlet />
      )}
    </Box>
  );
}
