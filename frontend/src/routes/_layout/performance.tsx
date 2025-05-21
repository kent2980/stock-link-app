import PerformancePage from "@/Pages/performance/page";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/performance")({
  component: Performance,
});

function Performance() {
  return (
    <Box>
      <PerformancePage />
    </Box>
  );
}
