import StockList from "@/components/StockList/StockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

export const Route = createFileRoute("/_layout/")({
  component: Index,
});

function Index() {
  return (
    <Box>
      <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
        <Suspense fallback={<div>Loading...</div>}>
          <StockList />
        </Suspense>
      </ErrorBoundary>
    </Box>
  );
}
