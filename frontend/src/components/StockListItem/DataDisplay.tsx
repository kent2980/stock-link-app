import { Box, HStack, Text, VStack } from "@chakra-ui/react";
import React from "react";

interface DataItem {
  name: string;
  currentValue: number;
  previousValue: number;
  changeRate: number;
}

interface DataDisplayProps {
  title?: string;
  data?: DataItem[];
}

const DataDisplay: React.FC<DataDisplayProps> = ({
  title = "経営成績",
  data = [
    {
      name: "売上高",
      currentValue: 6700000000,
      previousValue: 6400000000,
      changeRate: 4.7,
    },
    {
      name: "純利益",
      currentValue: 60000000000,
      previousValue: 36000000000,
      changeRate: 66.7,
    },
    {
      name: "営業利益",
      currentValue: 30000000000,
      previousValue: 27000000000,
      changeRate: 11.1,
    },
    {
      name: "経常利益",
      currentValue: 40000000000,
      previousValue: 35000000000,
      changeRate: 14.3,
    },
  ],
}) => {
  // データ数に応じたフォントサイズの調整
  const fontSize = `${(10 / data.length) * 5}px`;
  const valueFontSize = `${(10 / data.length) * 7}px`;

  return (
    <Box>
      <Text
        color="gray.600"
        fontSize="16px"
        fontWeight="semibold"
        mb={4}
        textAlign="left"
      >
        {title}
      </Text>
      <HStack gap={8} justify="space-between">
        {data.map((item, index) => (
          <VStack key={index} gap={1} align="center">
            <Text fontSize={fontSize} color="gray.500">
              {item.name}
            </Text>
            <Text fontWeight="bold" fontSize={valueFontSize}>
              {(item.currentValue / 1_000_000_000).toFixed(1)}億円
              <Text as="span" fontSize={fontSize} color="gray.500" ml={2}>
                ({item.changeRate >= 0 ? "+" : ""}
                {item.changeRate.toFixed(1)}%)
              </Text>
            </Text>
            {/* 前年の数値 */}
            <Text fontSize={fontSize} color="gray.400">
              {(item.previousValue / 1_000_000_000).toFixed(1)}億円
              <br />
              <Text
                as="span"
                ml={1}
                color={item.changeRate >= 0 ? "green.600" : "red.600"}
              >
                ({item.changeRate >= 0 ? "+" : ""}
                {item.changeRate.toFixed(1)}%)
              </Text>
            </Text>
          </VStack>
        ))}
      </HStack>
    </Box>
  );
};

export default DataDisplay;
