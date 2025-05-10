import CustomSpinner from "@/components/Spinner/CustomSpinner";
import LatestStockList from "@/components/StockList/LatestStockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

export const Route = createFileRoute("/_layout/stock/")({
  component: Timeline,
});

function Timeline() {
  return (
    <Box h="100vh">
      <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
        <Suspense fallback={<CustomSpinner />}>
          <LatestStockList />
        </Suspense>
      </ErrorBoundary>
    </Box>
  );
}
