import { WikiService } from "@/client";
import { Box, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";

interface StockWikiProps {
  code: string;
}

const StockWiki: React.FC<StockWikiProps> = ({ code }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["stock", code],
    queryFn: async () => {
      return await WikiService.getStockWikiItem({
        code: code,
      });
    },
    retry: 0,
  });

  return (
    <Box>
      <Text>{data.description}</Text>
    </Box>
  );
};

export default StockWiki;
