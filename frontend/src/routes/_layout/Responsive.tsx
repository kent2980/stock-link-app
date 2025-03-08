import ResponsiveTable from "@/components/Index/IRSummary/ResponsiveTable";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/Responsive")({
  component: Responsive,
});

function Responsive() {
  return (
    <div>
      <ResponsiveTable />
    </div>
  );
}
