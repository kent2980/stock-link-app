import StockList from "@/components/StockListItem/StockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense, useEffect } from "react";
import { ErrorBoundary } from "react-error-boundary";
import { HeaderAddressItem, HeaderStore } from "../../Store/HeaderStore";

export const Route = createFileRoute("/_layout/")({
  component: Index,
});

function Index() {
  const items: HeaderAddressItem[] = [
    {
      label: "Top",
      href: "/",
    },
  ];
  useEffect(() => {
    HeaderStore.setState((state) => {
      return {
        ...state,
        HeaderAddressItems: items,
      };
    });
  }, []);

  return (
    <Box overflow="hidden">
      {/* デスクトップ */}
      {/* モバイル */}
      <Box display={{ base: "block", md: "none" }}>
        <Suspense fallback={<div>Loading...</div>}>
          <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
            <StockList />
          </ErrorBoundary>
        </Suspense>
      </Box>
    </Box>
  );
}
