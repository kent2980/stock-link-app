import CustomSpinner from "@/components/Spinner/CustomSpinner";
import Industry33StockList from "@/components/StockList/Industry33StockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute, useParams } from "@tanstack/react-router";
import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

export const Route = createFileRoute(
  "/_layout/timeline/industry33/$industry_33"
)({
  component: Timeline,
});

function Timeline() {
  const { industry_33 } = useParams({
    from: "/_layout/timeline/industry33/$industry_33",
  });

  return (
    <Box>
      <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
        <Suspense fallback={<CustomSpinner />}>
          <Industry33StockList industry_33_code={Number(industry_33)} />
        </Suspense>
      </ErrorBoundary>
    </Box>
  );
}
