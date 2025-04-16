import StockList from "@/components/StockListItem/StockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute, useParams } from "@tanstack/react-router";
import { Suspense } from "react";

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
        <Suspense fallback={<div>Loading...</div>}>
          <StockList industry_17_code={Number(industry_17)} />
        </Suspense>
      </Box>
    </Box>
  );
}
