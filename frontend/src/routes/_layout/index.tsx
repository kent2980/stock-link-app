import MainDataView from "@/components/Index/MainDataView";
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
      <Suspense fallback={<div>Loading...</div>}>
        <MainDataView />
      </Suspense>
    </>
  );
}
