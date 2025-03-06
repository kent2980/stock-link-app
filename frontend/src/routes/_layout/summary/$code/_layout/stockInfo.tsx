import { Box, Skeleton, VStack } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";
import WikiInfoErrorBound from "../../-compomnents/ErrorBoundary/WikiInfoErrorBound";
import FinancialPosition from "../../-compomnents/StockInfo/FinancialPosition";
import OperatingResult from "../../-compomnents/StockInfo/OperatingResult";
import WikiInfo from "../../-compomnents/StockInfo/WikiInfo";
export const Route = createFileRoute(
  "/_layout/summary/$code/_layout/stockInfo"
)({
  component: StockInfo,
});

function StockInfo() {
  const { code } = Route.useParams();
  return (
    <>
      <Box p={4} w="100%" minH={120} boxShadow="md" borderRadius="md">
        <WikiInfoErrorBound>
          <Suspense
            fallback={
              <VStack gap={4}>
                {Array.from({ length: 3 }).map((_, index) => (
                  <Skeleton key={index} height="20px" w="100%" />
                ))}
              </VStack>
            }
          >
            <WikiInfo code={code} />
          </Suspense>
        </WikiInfoErrorBound>
      </Box>
      <Suspense fallback={<div>Loading...</div>}>
        <OperatingResult code={code} />
      </Suspense>
      <Suspense fallback={<div>Loading...</div>}>
        <FinancialPosition code={code} />
      </Suspense>
    </>
  );
}
