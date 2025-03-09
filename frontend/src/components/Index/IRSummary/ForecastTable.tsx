import { SummaryService } from "@/client";
import { Box, Card, Flex, Heading, Table } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";

interface ForecastTableProps {
  head_item_key: string;
}

const ForecastTable = ({ head_item_key }: ForecastTableProps) => {
  const { data } = useSuspenseQuery({
    queryKey: ["Forecast", head_item_key],
    queryFn: async () => {
      return await SummaryService.getForecasts({
        headItemKey: head_item_key,
      });
    },
  });
  return (
    <Box>
      <Card.Root boxShadow="lg" borderRadius="xl" overflow="hidden">
        <Card.Body p={0}>
          <Flex p={4} justifyContent="space-between" alignItems="center">
            <Heading size="md">業績予想</Heading>
          </Flex>
          <Table.Root size="sm" fontSize={12}>
            <Table.Header fontSize={10}>
              <Table.Row>
                <Table.ColumnHeader
                  w="33%"
                  textAlign={{ base: "center", md: "left" }}
                >
                  科目
                </Table.ColumnHeader>
                <Table.ColumnHeader w="33%" textAlign="center">
                  予想値
                </Table.ColumnHeader>
              </Table.Row>
            </Table.Header>
            <Table.Body>
              {data.data.map((item) =>
                item.forecast?.data?.map((result, key) => (
                  <Table.Row key={key}>
                    <Table.Cell
                      fontSize={10}
                      textAlign={{ base: "center", md: "left" }}
                    >
                      {result.label} ({result.curValue?.display_scale})
                    </Table.Cell>
                    <Table.Cell fontSize={10} textAlign="center">
                      {result.curValue?.value}
                    </Table.Cell>
                  </Table.Row>
                ))
              )}
            </Table.Body>
          </Table.Root>
        </Card.Body>
      </Card.Root>
    </Box>
  );
};

export default ForecastTable;
