import StockList from "@/components/StockList/StockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute, useParams } from "@tanstack/react-router";
import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

export const Route = createFileRoute("/_layout/index/industry/$industry_17")({
  component: Index,
});

function Index() {
  const { industry_17 } = useParams({
    from: "/_layout/index/industry/$industry_17",
  });
  console.log("industry_17", industry_17);
  return (
    <Box overflow="hidden">
      {/* デスクトップ */}
      {/* モバイル */}
      <Box display={{ base: "block", md: "none" }}>
        <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
          <Suspense fallback={<div>Loading...</div>}>
            <StockList industry_17_code={Number(industry_17)} />
          </Suspense>
        </ErrorBoundary>
      </Box>
    </Box>
  );
}
