import { Box, BoxProps, VStack } from "@chakra-ui/react";
import { Suspense } from "react";
import StockList from "../StockListItem/StockList";

const ChildSidebar: React.FC<BoxProps> = (props) => {
  return (
    <Box
      display={{
        base: "none",
        md: "block",
      }}
      as="nav"
      h="100vh"
      w={"300px"}
      bg="gray.700"
      p={1}
      position="fixed"
      top="0"
      left="80px"
      {...props}
    >
      <VStack align="start" gap="4">
        <Suspense fallback={<div>Loading...</div>}>
          <StockList />
        </Suspense>
      </VStack>
    </Box>
  );
};

export default ChildSidebar;
