import MainDataView from "@/components/Index/MainDataView";
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

  return (
    <>
      <Box></Box>
      <Suspense fallback={<div>Loading...</div>}>
        <MainDataView />
      </Suspense>
    </>
  );
}
