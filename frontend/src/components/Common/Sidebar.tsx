import { Box, BoxProps, VStack } from "@chakra-ui/react";
import React, { Suspense } from "react";
import SummaryList from "../Sidebar/SummaryList";

interface SidebarProps extends BoxProps {
  links: { name: string; icon: React.ElementType; href: string }[];
}

const Sidebar: React.FC<SidebarProps> = ({ links, ...rest }) => {
  return (
    <Box
      bg="gray.50"
      pos="fixed"
      h="full"
      {...rest}
      shadow="md"
      display={{ base: "none", md: "block" }}
    >
      <VStack gap={4} mt={4} align="stretch">
        <Suspense fallback={<Box p={4}>Loading...</Box>}>
          <SummaryList />
        </Suspense>
      </VStack>
    </Box>
  );
};

export default Sidebar;
