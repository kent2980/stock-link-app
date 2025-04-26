import StockList from "@/components/StockList/StockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute, useParams } from "@tanstack/react-router";
import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

export const Route = createFileRoute("/_layout/index/date/$dateStr")({
  component: Index,
});

function Index() {
  const { dateStr } = useParams({ from: "/_layout/index/date/$dateStr" });
  return (
    <Box overflow="hidden">
      {/* デスクトップ */}
      {/* モバイル */}
      <Box display={{ base: "block", md: "none" }}>
        <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
          <Suspense fallback={<div>Loading...</div>}>
            <StockList dateStr={dateStr} />
          </Suspense>
        </ErrorBoundary>
        {dateStr}
      </Box>
    </Box>
  );
}
