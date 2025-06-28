import Industries from "@/Pages/Industries";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";

export const Route = createFileRoute("/_layout/industries/")({
  component: Index,
});

function Index() {
  return (
    <Box>
      <Suspense fallback={<div>Loading...</div>}>
        <Industries />
      </Suspense>
    </Box>
  );
}
