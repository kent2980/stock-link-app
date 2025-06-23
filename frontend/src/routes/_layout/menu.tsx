import MainMenu from "@/Pages/MainMenu";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/menu")({
  component: Menu,
});

function Menu() {
  return (
    <Box>
      <MainMenu />
    </Box>
  );
}
