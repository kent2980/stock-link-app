import {
  Box,
  Flex,
  Grid,
  GridItem,
  HStack,
  Link,
  Text,
} from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import dayjs from "dayjs";
import React from "react";
import { edif, edjp, SummaryService } from "../../client";

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

  function isEdData(data: any): data is edjp | edif {
    return data.type === "edjp" || data.type === "edif";
  }

  return (
    <Grid
      color="ui.main"
      bg="ui.light"
      templateColumns="repeat(10, 1fr)"
      templateRows="repeat(4, auto)"
      gap={2}
      py={3}
      px={3}
      m={2}
      mt="70px"
      border="1px solid #e2e8f0"
    >
      <GridItem colSpan={10}>
        <Flex gap={6}>
          <Box
            bg="ui.light"
            color="ui.main"
            borderRadius="md"
            border="1px solid #e2e8f0"
            boxShadow="1px 1px 0.8px #959ba4"
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
      <GridItem colSpan={10}>
        <Flex gap={4}>
          <Box alignContent="center" fontSize={12} fontWeight={600}>
            {data.document_name?.value}
          </Box>
        </Flex>
      </GridItem>
      <GridItem colSpan={10}>
        <Flex gap={4}>
          <Text
            bg="ui.light"
            color="ui.main"
            fontSize={12}
            fontWeight={600}
            px={2}
          >
            {dayjs(data.fiscal_year_end?.value).format("YYYY年M月期")}
          </Text>
          {isEdData(data) && (
            <HStack bg="ui.light" color="ui.main" px={2}>
              <Text alignContent="center" fontSize={12} fontWeight={600}>
                会計期間:
              </Text>
              <Text alignContent="center" fontSize={12} fontWeight={600}>
                {data?.type_of_current_period_dei?.value}
              </Text>
            </HStack>
          )}
        </Flex>
      </GridItem>
      <GridItem colSpan={10}>
        <Flex>
          {isEdData(data) && (
            <Text>
              <Link href={data.URL?.value ?? ""}>{data.URL?.value}</Link>
            </Text>
          )}
        </Flex>
      </GridItem>
    </Grid>
  );
};

export default Header;
