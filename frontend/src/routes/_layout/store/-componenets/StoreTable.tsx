import { IxService } from "@/client";
import { Box, Checkbox, Flex, Table, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useVirtualizer } from "@tanstack/react-virtual";
import React, { Suspense, useRef } from "react";
import BusinessPerformance from "./BusinessPerformance";

interface StoreTableProps {}

export const StoreTable: React.FC<StoreTableProps> = () => {
  const { data } = useSuspenseQuery({
    queryKey: ["store"],
    queryFn: async () => {
      return await IxService.getDocumentList();
    },
  });
  const parentRef = useRef<HTMLDivElement>(null);

  const rowVirtualizer = useVirtualizer({
    count: data.count,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 80,
    overscan: 5,
  });

  return (
    <>
      <Box ref={parentRef} w="100%">
        <Box height={`${rowVirtualizer.getTotalSize()}px`} w="100%">
          <Table.Root size="sm" variant="outline" showColumnBorder>
            <Table.Header>
              <Table.Row>
                <Table.ColumnHeader textAlign="center">
                  <Checkbox.Root colorPalette="blackAlpha" variant="subtle">
                    <Checkbox.HiddenInput />
                    <Checkbox.Control>
                      <Checkbox.Indicator />
                    </Checkbox.Control>
                  </Checkbox.Root>
                </Table.ColumnHeader>
                <Table.ColumnHeader>コード</Table.ColumnHeader>
                <Table.ColumnHeader>銘柄名</Table.ColumnHeader>
                <Table.ColumnHeader>業績(前年同期比)</Table.ColumnHeader>
              </Table.Row>
            </Table.Header>
            <Table.Body>
              {rowVirtualizer.getVirtualItems().map((virtualRow) => {
                const item = data.data[virtualRow.index];
                return (
                  <Table.Row
                    key={virtualRow.index}
                    height={`${virtualRow.size}px`}
                  >
                    <Table.Cell textAlign="center">
                      <Checkbox.Root colorPalette="blackAlpha" variant="subtle">
                        <Checkbox.HiddenInput />
                        <Checkbox.Control>
                          <Checkbox.Indicator />
                        </Checkbox.Control>
                      </Checkbox.Root>
                    </Table.Cell>
                    <Table.Cell>{item.securities_code}</Table.Cell>
                    <Table.Cell>{item.company_name}</Table.Cell>
                    {item.report_type.startsWith("ed") ? (
                      <Table.Cell>
                        <Flex direction="column" gap={2}>
                          <Flex direction="column" gap={0}>
                            <Text fontSize={10}>経営成績</Text>
                            <Suspense fallback={<Box>Loading...</Box>}>
                              <BusinessPerformance
                                head_item_key={item.head_item_key}
                              />
                            </Suspense>
                          </Flex>
                          <Flex direction="column" gap={0}>
                            <Text fontSize={10}>業績予想</Text>
                            <Suspense fallback={<Box>Loading...</Box>}>
                              <BusinessPerformance
                                head_item_key={item.head_item_key}
                              />
                            </Suspense>
                          </Flex>
                        </Flex>
                      </Table.Cell>
                    ) : (
                      <Table.Cell></Table.Cell>
                    )}
                  </Table.Row>
                );
              })}
            </Table.Body>
          </Table.Root>
        </Box>
      </Box>
    </>
  );
};

export default StoreTable;
