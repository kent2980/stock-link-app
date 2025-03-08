import { SummaryService } from "@/client";
import {
  Badge,
  Box,
  Card,
  Flex,
  FormatNumber,
  Heading,
  Table,
} from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";

interface OperatingResultProps {
  head_item_key: string;
}

function OperatingResult({ head_item_key }: OperatingResultProps) {
  const { data } = useSuspenseQuery({
    queryKey: ["IRSummary", head_item_key],
    queryFn: async () => {
      return await SummaryService.getOperatingResults({
        headItemKey: head_item_key,
      });
    },
  });

  const badgeWidth = 16;
  return (
    <Box>
      <Card.Root boxShadow="lg" borderRadius="xl" overflow="hidden">
        <Card.Body p={0}>
          <Flex p={4} justifyContent="space-between" alignItems="center">
            <Heading size="md">経営成績</Heading>
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
                  今期
                </Table.ColumnHeader>
                <Table.ColumnHeader w="33%" textAlign="center">
                  昨年同期
                </Table.ColumnHeader>
              </Table.Row>
            </Table.Header>
            <Table.Body>
              {data.data.map((item) =>
                item.result?.data?.map((result, key) => (
                  <Table.Row key={key}>
                    <Table.Cell
                      fontSize={10}
                      textAlign={{ base: "center", md: "left" }}
                    >
                      {result.label} ({result.curValue?.display_scale})
                    </Table.Cell>
                    <Table.Cell>
                      <Flex gap={2} alignItems="center" justifyContent="center">
                        <Box w="40%" textAlign="right">
                          <FormatNumber value={result.curValue?.value ?? 0} />
                        </Box>
                        <Flex
                          w="60%"
                          alignItems="center"
                          justifyContent="center"
                        >
                          {result.curChange?.value ? (
                            <Badge
                              w={badgeWidth}
                              colorPalette={
                                (result.curChange?.value ?? 0) > 0
                                  ? "green"
                                  : "red"
                              }
                              justifyContent="center"
                            >
                              {result.curChange?.value
                                .toString()
                                .replace("-", "▲ ") ?? ""}
                              %
                            </Badge>
                          ) : (
                            <Badge
                              w={badgeWidth}
                              colorPalette="blue"
                              justifyContent="center"
                            >
                              -
                            </Badge>
                          )}
                        </Flex>
                      </Flex>
                    </Table.Cell>
                    <Table.Cell>
                      <Flex gap={2} alignItems="center" justifyContent="center">
                        <Box w="40%" textAlign="right">
                          <FormatNumber value={result.preValue?.value ?? 0} />
                        </Box>
                        <Flex
                          w="60%"
                          alignItems="center"
                          justifyContent="center"
                        >
                          {result?.preChange?.value ? (
                            <Badge
                              w={badgeWidth}
                              colorPalette={
                                (result.preChange?.value ?? 0) > 0
                                  ? "green"
                                  : "red"
                              }
                              justifyContent="center"
                            >
                              {result.preChange?.value
                                .toString()
                                .replace("-", "▲ ") ?? ""}
                              %
                            </Badge>
                          ) : (
                            <Badge
                              w={badgeWidth}
                              colorPalette="blue"
                              justifyContent="center"
                            >
                              -
                            </Badge>
                          )}
                        </Flex>
                      </Flex>
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
}

export default OperatingResult;
