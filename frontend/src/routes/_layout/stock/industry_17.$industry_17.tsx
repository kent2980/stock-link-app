import CustomSpinner from "@/components/Spinner/CustomSpinner";
import Industry17StockList from "@/components/StockList/Industry17StockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute, useParams } from "@tanstack/react-router";
import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

export const Route = createFileRoute("/_layout/stock/industry_17/$industry_17")(
  {
    component: Timeline,
  }
);

function Timeline() {
  const { industry_17 } = useParams({
    from: "/_layout/stock/industry_17/$industry_17",
  });

  return (
    <Box>
      <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
        <Suspense fallback={<CustomSpinner />}>
          <Industry17StockList industry_17_code={Number(industry_17)} />
        </Suspense>
      </ErrorBoundary>
    </Box>
  );
}
