import DisclosurePage from "@/Pages/disclosure/Disclosure";
import { Container } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/")({
  component: Index,
});

function Index() {
  return (
    <Container id="main-container">
      <DisclosurePage />
    </Container>
  );
}
