import StockList from "@/components/StockList/StockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute, useParams } from "@tanstack/react-router";
import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

export const Route = createFileRoute("/_layout/index/industry33/$industry_33")({
  component: Index,
});

function Index() {
  const { industry_33 } = useParams({
    from: "/_layout/index/industry33/$industry_33",
  });

  return (
    <Box overflow="hidden">
      {/* デスクトップ */}
      {/* モバイル */}
      <Box display={{ base: "block", md: "none" }}>
        <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
          <Suspense fallback={<div>Loading...</div>}>
            <StockList industry_33_code={Number(industry_33)} />
          </Suspense>
        </ErrorBoundary>
      </Box>
    </Box>
  );
}
