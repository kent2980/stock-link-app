import MiniDisclosure from "@/Pages/disclosure/MiniDisclosure";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";

export const Route = createFileRoute("/_layout/")({
  component: Index,
});

function Index() {
  return (
    <Box id="main-content">
      <Suspense fallback={<div>Loading...</div>}>
        <MiniDisclosure />
      </Suspense>
    </Box>
  );
}
