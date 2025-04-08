import IndexHeader from "@/components/Common/IndexHeader";
import StockList from "@/components/StockListItem/StockList";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense, useEffect } from "react";
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

  const HEADER_HEIGHT = "120px";

  return (
    <Box overflow="hidden">
      <IndexHeader h={HEADER_HEIGHT} />
      <Suspense fallback={<div>Loading...</div>}>
        <StockList pt={HEADER_HEIGHT} />
      </Suspense>
    </Box>
  );
}
