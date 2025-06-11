import DisclosurePage from "@/Pages/disclosure/Disclosure";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";

export const Route = createFileRoute("/_layout/disclosure/")({
  component: Index,
});

function Index() {
  return (
    <Box px={{ base: 0, md: 4 }}>
      <Suspense fallback={<div>Loading...</div>}>
        <DisclosurePage />
      </Suspense>
    </Box>
  );
}
