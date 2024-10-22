import {
  Badge,
  Box,
  Heading,
  LinkBox,
  LinkOverlay,
  Stack,
  Text,
} from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import { createFileRoute, Link as RouterLink } from "@tanstack/react-router";
import { XbrlViewService } from "../../client";

export const Route = createFileRoute("/_layout/navigate")({
  component: Navigate,
});

function Navigate() {
  const { data: items, status } = useQuery({
    queryKey: ["navigate", 5000],
    queryFn: () =>
      XbrlViewService.readNewStockRecord({
        limit: 5000,
      }),
  });

  if (status === "error") {
    return <Box>Error</Box>;
  }

  if (status === "pending") {
    return <Box>Loading...</Box>;
  }

  if (!items) {
    return <Box>No data</Box>;
  }

  return (
    <Box w="full" p={0} bg="gray.100">
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
              </Box>
              <Stack direction={"row"} spacing={4}>
                <Stack direction="row" alignItems="center" spacing={4}>
                  <Badge
                    fontSize="14px"
                    colorScheme="pink"
                    px={2}
                    py="1px"
                    borderRadius="md"
                    variant="outline"
                  >
                    {item.securities_code}
                  </Badge>
                  <Heading size="xs" color="gray.700">
                    <LinkOverlay
                      as={RouterLink}
                      to={`/summary/${item.xbrl_id}`}
                    >
                      {item.company_name}
                    </LinkOverlay>
                  </Heading>
                </Stack>
              </Stack>
              <Text as={"span"} fontSize="sm" mx={2}>
                {item.document_name}
              </Text>
            </Stack>
          </LinkBox>
        ))}
      </Stack>
    </Box>
  );
}
