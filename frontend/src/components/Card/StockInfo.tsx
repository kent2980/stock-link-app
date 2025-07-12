import { DisclosureItem } from "@/client";
import { Box } from "@chakra-ui/react";
import React from "react";

interface StockInfoProps {
  item: DisclosureItem | null;
}

const StockInfo: React.FC<StockInfoProps> = ({ item }) => {
  return (
    <Box>
      {item?.company}
      <Box>{item?.summary}</Box>
    </Box>
  );
};

export default StockInfo;
