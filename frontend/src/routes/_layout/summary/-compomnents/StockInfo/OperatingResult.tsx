import { Box, Heading, Table } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";
import { SummaryService } from "../../../../../client";

interface OperatingResultProps {
  code: string;
}

const OperatingResult: React.FC<OperatingResultProps> = ({ code }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["OperatingResult", code],
    queryFn: async () => {
      return SummaryService.getOperatingResults({ code });
    },
  });
  return (
    <Box p={5} shadow="md" w="100%">
      <Heading fontSize="md">経営成績</Heading>
      {/* デスクトップ */}
      <Table.Root display={{ base: "none", md: "table" }}>
        <Table.Header>
          <Table.Row>
            {data.labels.map((item, key) => (
              <Table.ColumnHeader key={key} colSpan={2}>
                {item.label}
              </Table.ColumnHeader>
            ))}
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {data.data.map(
            (item, key) =>
              item.result?.is_active && (
                <Table.Row key={key}>
                  {item.result.data?.map((metric) => (
                    <>
                      <Table.Cell>{metric.value?.value}</Table.Cell>
                      <Table.Cell>{metric.change?.value}%</Table.Cell>
                    </>
                  ))}
                </Table.Row>
              )
          )}
        </Table.Body>
      </Table.Root>
      {/* モバイル */}
      <Table.Root display={{ base: "table", md: "none" }}>
        <Table.Header>
          <Table.Row>
            <Table.ColumnHeader>項目</Table.ColumnHeader>
            <Table.ColumnHeader>実績</Table.ColumnHeader>
            <Table.ColumnHeader>前年比</Table.ColumnHeader>
          </Table.Row>
        </Table.Header>
        {data.data.map(
          (item) =>
            item.result?.is_active &&
            item.result.data?.map((metric, key) => (
              <>
                <Table.Row key={key}>
                  <Table.ColumnHeader>{metric.label}</Table.ColumnHeader>
                  <Table.Cell>{metric.value?.value}</Table.Cell>
                  <Table.Cell>{metric.change?.value}%</Table.Cell>
                </Table.Row>
              </>
            ))
        )}
      </Table.Root>
    </Box>
  );
};

export default OperatingResult;
