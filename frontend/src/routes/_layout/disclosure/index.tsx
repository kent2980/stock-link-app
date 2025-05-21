import DisclosurePage from "@/Page/disclosure/Disclosure";
import { Container } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/disclosure/")({
  component: Index,
});

function Index() {
  return (
    <Container>
      <DisclosurePage />
    </Container>
  );
}
