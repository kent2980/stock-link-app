import {
  Box,
  BoxProps,
  Heading,
  LinkBox,
  LinkOverlay,
  Stack,
  Text,
} from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import { Link as RouterLink } from "@tanstack/react-router";
import React from "react";
import { XbrlViewService } from "../../client";

interface StockSummaryProps extends BoxProps {
  code: string;
}

const StockSummary: React.FC<StockSummaryProps> = ({ code, ...props }) => {
  const { data: items, status } = useQuery({
    queryKey: ["heads", code, 50],
    queryFn: () =>
      XbrlViewService.readHeadItems({
        code: "",
        limit: 50,
      }),
    enabled: !!code,
  });

  if (status === "error") {
    return <Box>Error</Box>;
  }

  if (status === "pending") {
    return <Box>Loading...</Box>;
  }

  return (
    <Box {...props} w="full" p={0} bg="gray.100">
      <Stack spacing={0}>
        {items.data.map((item) => (
          <LinkBox key={item.xbrl_id}>
            <Stack
              direction={"column"}
              spacing={2}
              color={"gray.600"}
              borderWidth="1px"
              p={5}
              bg="white"
              boxShadow="0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08)"
            >
              <Box as={"p"}>
                <Text as={"span"} fontSize="sm" mx={2}>
                  {item.reporting_date}
                </Text>
                <Text as={"span"} fontSize="sm" mx={2}>
                  {item.current_period}
                </Text>
                <Text as={"span"} fontSize="sm" mx={2}>
                  {item.company_name}
                </Text>
              </Box>
              <Heading size="xs" color="gray.700">
                <LinkOverlay
                  as={RouterLink}
                  to={`/summary/${item.xbrl_id}`}
                  replace
                >
                  {item.document_name}
                </LinkOverlay>
              </Heading>
            </Stack>
          </LinkBox>
        ))}
      </Stack>
    </Box>
  );
};

export default StockSummary;
