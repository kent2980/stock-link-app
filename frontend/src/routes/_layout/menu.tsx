import Industries from "@/Pages/Industries";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";

export const Route = createFileRoute("/_layout/menu")({
  component: Menu,
});

function Menu() {
  return (
    <Box>
      <Suspense fallback={<div>Loading...</div>}>
        <Industries />
      </Suspense>
    </Box>
  );
}
