import { DashboardInfo } from "@/components/Home/dashboard-info";
import DisclosurePage from "@/Pages/disclosure/Disclosure";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/")({
  component: Index,
});

function Index() {
  return (
    <Box id="main-content">
      <DashboardInfo />
      <DisclosurePage />
    </Box>
  );
}
