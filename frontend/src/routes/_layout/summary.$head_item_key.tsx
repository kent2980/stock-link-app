import { Container, Divider, SimpleGrid } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import Contents from "../../components/Summary/Contents";
import Header from "../../components/Summary/Header";

export const Route = createFileRoute("/_layout/summary/$head_item_key")({
  component: () => <Summary />,
});

function Summary() {
  const { head_item_key } = Route.useParams();

  return (
    <Container maxW={"5xl"} py={4}>
      <SimpleGrid row={2} spacing={10}>
        <Header head_item_key={head_item_key} />
        <Divider />
        <Contents head_item_key={head_item_key} />
      </SimpleGrid>
    </Container>
  );
}
