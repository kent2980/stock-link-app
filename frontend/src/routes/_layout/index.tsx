import Header from "@/components/StockListItem/Header";
import { Box, Card, Flex } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { useEffect } from "react";
import { HeaderAddressItem, HeaderStore } from "../../Store/HeaderStore";

export const Route = createFileRoute("/_layout/")({
  component: Index,
});

function Index() {
  const items: HeaderAddressItem[] = [
    {
      label: "Top",
      href: "/",
    },
  ];
  useEffect(() => {
    HeaderStore.setState((state) => {
      return {
        ...state,
        HeaderAddressItems: items,
      };
    });
  }, []);

  return (
    <Box>
      <Flex
        dir="row"
        justify="center"
        m={{ base: "0 auto", md: "0 auto" }}
        p={{ base: 2, md: 4 }}
      >
        <Card.Root w={{ base: "100%", md: "1024px" }} bg="white" shadow="md">
          <Card.Header borderBottom={"1px solid #eaeaea"}>
            <Header />
          </Card.Header>
          <Card.Body>
            <p>This is the content of the card.</p>
          </Card.Body>
          <Card.Footer>
            <p>This is the footer of the card.</p>
          </Card.Footer>
        </Card.Root>
      </Flex>
    </Box>
  );
}
