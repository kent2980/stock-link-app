import StockList from "@/components/StockList/StockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";

export const Route = createFileRoute("/_layout/")({
  component: Index,
});

function Index() {
  return (
    <Box>
      <Suspense fallback={<div>Loading...</div>}>
        <StockList />
      </Suspense>
    </Box>
  );
}
