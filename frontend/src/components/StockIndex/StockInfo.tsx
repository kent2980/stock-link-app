import { Badge, Box, Heading, HStack, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";
import { JpxService } from "../../client";

interface StockInfoProps {
  code: string;
}

const StockInfo: React.FC<StockInfoProps> = ({ code }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["StockInfoFromCode", code],
    queryFn: async () => {
      return await JpxService.readJpxStockInfoItem({
        code: code,
      });
    },
    staleTime: 1000 * 60 * 60 * 24 * 30, // 30 days
    gcTime: 1000 * 60 * 60 * 24 * 30, // 30 days
  });

  return (
    <Box borderBottom={"1px"} borderColor={"gray.200"}>
      <HStack spacing={8} p={4}>
        <Badge colorScheme="green" fontSize="1em" px={2}>
          {data.code}
        </Badge>
        <Heading size="md">{data.name}</Heading>
        <Text fontSize="sm">
          {data.market_or_type.replace("(内国株式)", "")}
        </Text>
        <Text fontSize="sm">{data.industry_33_name}</Text>
      </HStack>
    </Box>
  );
};

export default StockInfo;
