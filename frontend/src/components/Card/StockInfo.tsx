import { DisclosureItem } from "@/client";
import { Box, Table } from "@chakra-ui/react";
import React from "react";

interface StockInfoProps {
  item: DisclosureItem | null;
}

const StockInfo: React.FC<StockInfoProps> = ({ item }) => {
  if (item == null) {
    return <Box>No data available</Box>;
  }

  const ope = item.operating_result;
  return (
    <Box maxW="100%" overflowX="hidden" p={4}>
      {/* 経営成績テーブル */}
      <Table.Root size="sm">
        <Table.Header>
          <Table.Row>
            <Table.ColumnHeader py={0}>期間</Table.ColumnHeader>
            {ope?.data?.map((data, index) => (
              <Table.ColumnHeader
                key={index}
                maxW={"80px"}
                fontSize={"10px"}
                py={0}
              >
                {data.label}
              </Table.ColumnHeader>
            ))}
          </Table.Row>
        </Table.Header>
        <Table.Body>
          <Table.Row>
            <Table.Cell py={0}>{ope?.period?.fiscalYear}</Table.Cell>
            {ope?.data?.map((data, index) => (
              <Table.Cell key={index} py={0}>
                {data.result?.curValue?.value}
              </Table.Cell>
            ))}
          </Table.Row>
          <Table.Row>
            <Table.Cell py={0}>{ope?.period?.fiscalYear}</Table.Cell>
            {ope?.data?.map((data, index) => (
              <Table.Cell key={index} py={0}>
                {data.result?.preValue?.value}
              </Table.Cell>
            ))}
          </Table.Row>
        </Table.Body>
      </Table.Root>
    </Box>
  );
};

export default StockInfo;
