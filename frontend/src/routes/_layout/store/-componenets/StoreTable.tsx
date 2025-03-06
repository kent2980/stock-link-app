import { DocumentListPublic, IxService } from "@/client";
import {
  PaginationItems,
  PaginationNextTrigger,
  PaginationPrevTrigger,
  PaginationRoot,
} from "@/components/ui/pagination";
import { Box, HStack, Table, VStack } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { useEffect, useState } from "react";

interface StoreTableProps {}

export const StoreTable: React.FC<StoreTableProps> = () => {
  const [page, setPage] = useState(1);

  const limit = 50;
  const { data } = useSuspenseQuery({
    queryKey: ["storeTable", limit, page],
    queryFn: async () => {
      return IxService.getDocumentList({
        limit: limit,
        page: page,
      });
    },
  });

  const { count } = data;

  useEffect(() => {
    console.log("page", page);
  }, [page]);

  return (
    <VStack gap={4}>
      <Box>
        <PaginationRoot
          count={count}
          pageSize={limit}
          defaultPage={1}
          page={page}
          onPageChange={(e) => setPage(e.page)}
        >
          <HStack>
            <PaginationPrevTrigger />
            <PaginationItems />
            <PaginationNextTrigger />
          </HStack>
        </PaginationRoot>
      </Box>
      <Table.Root size="sm" variant="outline">
        <Table.Header>
          <Table.Row bg="bg.subtle">
            <Table.ColumnHeader>コード</Table.ColumnHeader>
            <Table.ColumnHeader>企業名</Table.ColumnHeader>
            <Table.ColumnHeader>提出書類名</Table.ColumnHeader>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {data?.data.map((item: DocumentListPublic) => (
            <Table.Row key={item.id}>
              <Table.Cell>{item.securities_code}</Table.Cell>
              <Table.Cell>{item.company_name}</Table.Cell>
              <Table.Cell>{item.document_name}</Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table.Root>
    </VStack>
  );
};

export default StoreTable;
