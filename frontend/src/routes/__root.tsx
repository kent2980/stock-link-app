import { Box } from "@chakra-ui/react";
import { Outlet, createRootRouteWithContext } from "@tanstack/react-router";
import React, { Suspense } from "react";

import NotFound from "@/components/Common/NotFound";
import { QueryClient } from "@tanstack/react-query";

const loadDevtools = () =>
  Promise.all([
    import("@tanstack/router-devtools"),
    import("@tanstack/react-query-devtools"),
  ]).then(([routerDevtools, reactQueryDevtools]) => {
    return {
      default: () => (
        <>
          <Box display={{ base: "block", md: "block" }}>
            <routerDevtools.TanStackRouterDevtools />
            <reactQueryDevtools.ReactQueryDevtools />
          </Box>
        </>
      ),
    };
  });

const TanStackDevtools =
  process.env.NODE_ENV === "production" ? () => null : React.lazy(loadDevtools);

export const Route = createRootRouteWithContext<{
  queryClient: QueryClient;
}>()({
  component: () => (
    <>
      <Outlet />
      <Box display={{ base: "none", md: "block" }}>
        <Suspense>
          <TanStackDevtools />
        </Suspense>
      </Box>
    </>
  ),
  notFoundComponent: () => <NotFound />,
});
