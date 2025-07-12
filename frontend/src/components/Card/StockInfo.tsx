import { DisclosureItem } from "@/client";
import { Box, Table } from "@chakra-ui/react";
import React from "react";
import { DarkMode, useColorModeValue } from "../ui/color-mode";

interface StockInfoProps {
  item: DisclosureItem | null;
}

const StockInfo: React.FC<StockInfoProps> = ({ item }) => {
  const bg = useColorModeValue("#272429", "white");
  const borderColor = useColorModeValue("gray.600", "gray.400");
  if (item == null) {
    return <Box>No data available</Box>;
  }

  const ope = item.operating_result;
  return (
    <Box maxW="100%" overflowX="hidden" p={4}>
      {/* 経営成績テーブル */}
      <DarkMode>
        <Table.Root size="sm" boxShadow="sm">
          <Table.Header>
            <Table.Row bg={bg}>
              <Table.ColumnHeader
                py={0}
                borderBottom="1px solid"
                borderColor={borderColor}
              >
                期間
              </Table.ColumnHeader>
              {ope?.data?.map((data, index) => (
                <Table.ColumnHeader
                  key={index}
                  maxW={"80px"}
                  fontSize={"10px"}
                  py={0}
                  borderBottom="1px solid"
                  borderColor={borderColor}
                >
                  {data.label}
                </Table.ColumnHeader>
              ))}
            </Table.Row>
          </Table.Header>
          <Table.Body>
            <Table.Row bg={bg}>
              <Table.Cell
                py={0}
                borderBottom="1px solid"
                borderColor={borderColor}
              >
                {ope?.period?.fiscalYear}
              </Table.Cell>
              {ope?.data?.map((data, index) => (
                <Table.Cell
                  key={index}
                  py={0}
                  borderBottom="1px solid"
                  borderColor={borderColor}
                >
                  {data.result?.curValue?.value}
                </Table.Cell>
              ))}
            </Table.Row>
            <Table.Row bg={bg}>
              <Table.Cell py={0}>{ope?.period?.fiscalYear}</Table.Cell>
              {ope?.data?.map((data, index) => (
                <Table.Cell key={index} py={0}>
                  {data.result?.preValue?.value}
                </Table.Cell>
              ))}
            </Table.Row>
          </Table.Body>
        </Table.Root>
      </DarkMode>
    </Box>
  );
};

export default StockInfo;
