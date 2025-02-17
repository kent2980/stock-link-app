import { VStack } from "@chakra-ui/react";
import { createFileRoute, Outlet } from "@tanstack/react-router";
import SummaryHeader from "../-compomnents/SummaryHeader";

export const Route = createFileRoute("/_layout/summary/$code/_layout")({
  component: _Layout,
});

function _Layout() {
  const { code } = Route.useParams();
  return (
    <>
      <VStack spacing={10} align="flex-start" ml={{ base: 4, md: 14 }}>
        <SummaryHeader code={code} />
        <Outlet />
      </VStack>
    </>
  );
}
