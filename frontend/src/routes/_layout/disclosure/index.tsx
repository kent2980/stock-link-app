import DisclosurePage from "@/Pages/disclosure/Disclosure";
import { Container } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";

export const Route = createFileRoute("/_layout/disclosure/")({
  component: Index,
});

function Index() {
  return (
    <Container>
      <Suspense fallback={<div>Loading...</div>}>
        <DisclosurePage />
      </Suspense>
    </Container>
  );
}
