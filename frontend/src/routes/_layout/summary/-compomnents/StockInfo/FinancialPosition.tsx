import { SummaryService } from "@/client";
import { Box, Heading, Table } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";

interface FinancialPositionProps {
  code: string;
}

const FinancialPosition: React.FC<FinancialPositionProps> = ({ code }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["FinancialPosition", code],
    queryFn: () => {
      return SummaryService.getFinancialPosition({ code });
    },
  });
  return (
    <Box p={5} shadow="md" w="100%">
      <Heading fontSize="md">財政状況</Heading>
      <Table.Root>
        <Table.Header>
          <Table.Row>
            {data.labels.map((item, key) => (
              <Table.ColumnHeader key={key}>{item.label}</Table.ColumnHeader>
            ))}
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {data.data.map((items, key) => (
            <Table.Row key={key}>
              {items.result?.is_active &&
                items.result.data?.map((item, key) => (
                  <Table.Cell key={key}>{item.value?.value}</Table.Cell>
                ))}
            </Table.Row>
          ))}
        </Table.Body>
      </Table.Root>
    </Box>
  );
};

export default FinancialPosition;
