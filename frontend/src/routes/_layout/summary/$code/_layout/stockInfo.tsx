import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";
import LatestUpdates from "../../-compomnents/StockInfo/LatestUpdates";
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
      <Suspense fallback={<div>Loading...</div>}>
        <WikiInfo code={code} />
      </Suspense>
      <Suspense fallback={<div>Loading...</div>}>
        <LatestUpdates code={code} />
      </Suspense>
    </>
  );
}
