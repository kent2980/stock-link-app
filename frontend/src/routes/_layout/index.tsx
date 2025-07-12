import StockGallery from "@/components/Card/StockGallery";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";

export const Route = createFileRoute("/_layout/")({
  component: Index,
});

function Index() {
  return (
    <Box id="main-content" h="100%">
      <Box h="30%"></Box>
      <Box h="70%">
        <Suspense fallback={<Box>Loading...</Box>}>
          <StockGallery />
        </Suspense>
      </Box>
    </Box>
  );
}
