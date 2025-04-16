import StockList from "@/components/StockListItem/StockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute, useParams } from "@tanstack/react-router";
import { Suspense } from "react";

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
        <Suspense fallback={<div>Loading...</div>}>
          <StockList dateStr={dateStr} />
        </Suspense>
        {dateStr}
      </Box>
    </Box>
  );
}
