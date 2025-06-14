import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/disclosure/page/$key")({
  component: DisclosurePage,
});

function DisclosurePage() {
  const { key } = Route.useParams();
  return <Box>{key}</Box>;
}
