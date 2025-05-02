import StockList from "@/components/StockList/StockList";
import { Box, Spinner, Text, VStack } from "@chakra-ui/react";
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
        <Suspense
          fallback={
            <VStack colorPalette="teal">
              <Spinner color="colorPalette.600" />
              <Text color="colorPalette.600">Loading...</Text>
            </VStack>
          }
        >
          <StockList />
        </Suspense>
      </ErrorBoundary>
    </Box>
  );
}
