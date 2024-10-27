import { Outlet, createRootRoute } from "@tanstack/react-router";
import React, { Suspense } from "react";

import { Box } from "@chakra-ui/react";
import NotFound from "../components/Common/NotFound";

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

export const Route = createRootRoute({
  component: () => (
    <>
      <Outlet />
      <Suspense>
        <TanStackDevtools />
      </Suspense>
    </>
  ),
  notFoundComponent: () => <NotFound />,
});
