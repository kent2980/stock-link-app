import { DocumentListPublic } from "@/client";
import { Box, Card, Flex, VStack } from "@chakra-ui/react";
import React from "react";
import DataDisplay from "./DataDisplay";
import Footer from "./Footer";
import Header from "./Header";
import ProgressBar from "./ProgressBar";

interface StockListItemProps {
  item: DocumentListPublic;
}

const StockListItem: React.FC<StockListItemProps> = ({ item }) => {
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
            <Header
              company_name={item.company_name}
              securities_code={item.securities_code}
            />
          </Card.Header>
          <Card.Body>
            <VStack gap={5} align="stretch">
              <ProgressBar value={40} />
              <DataDisplay />
              <DataDisplay />
            </VStack>
          </Card.Body>
          <Card.Footer>
            <Footer />
          </Card.Footer>
        </Card.Root>
      </Flex>
    </Box>
  );
};

export default StockListItem;
