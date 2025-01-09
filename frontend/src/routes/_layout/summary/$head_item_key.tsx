import { Box } from "@chakra-ui/react";
import { createFileRoute, Outlet } from "@tanstack/react-router";
import Header from "../../../components/Summary/Header";

export const Route = createFileRoute("/_layout/summary/$head_item_key")({
  component: () => <Summary />,
});

function Summary() {
  const { head_item_key } = Route.useParams();

  return (
    <Box color="ui.main">
      <Header head_item_key={head_item_key} />
      <Outlet />
    </Box>
  );
}
