import { Box, Flex, Grid, GridItem } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import React from "react";
import { SummaryService } from "../../client";

interface HeaderProps {
  head_item_key: string;
}

const Header: React.FC<HeaderProps> = ({ head_item_key }) => {
  const { data, isPending, isError } = useQuery({
    queryKey: ["SummaryNonNumeric", head_item_key],
    queryFn: () => {
      return SummaryService.getSummaryNonNumericItemsHeadItemKey({
        headItemKey: head_item_key,
      });
    },
    gcTime: 1000 * 60 * 60 * 24,
    staleTime: 1000 * 60 * 60 * 24,
  });

  if (isPending) {
    return <Box>Loading...</Box>;
  }

  if (isError) {
    return <Box>Error</Box>;
  }

  return (
    <Grid
      bg="ui.main"
      color="ui.light"
      templateColumns="repeat(3, 1fr)"
      templateRows="repeat(2, auto)"
      gap={4}
      py={6}
      px={4}
    >
      <GridItem colSpan={3}>
        <Flex gap={4}>
          <Box
            bg="ui.light"
            color="ui.main"
            borderRadius="md"
            w={14}
            h={8}
            textAlign="center"
            alignContent="center"
            fontSize={18}
            fontWeight={600}
          >
            {data.securities_code?.value}
          </Box>
          <Box alignContent="center" fontSize={15} fontWeight={800}>
            {data.company_name?.value}
          </Box>
        </Flex>
      </GridItem>
      <GridItem colSpan={3}>
        <Flex gap={4}>
          <Box alignContent="center" fontSize={12} fontWeight={600}>
            {data.document_name?.value}
          </Box>
        </Flex>
      </GridItem>
    </Grid>
  );
};

export default Header;
