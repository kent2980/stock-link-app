import { Box } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useStore } from "@tanstack/react-store";
import React from "react";
import { XbrlDefService } from "../../client";
import { StockIndexStore } from "../../Store/StockIndexStore";

const Summary: React.FC = () => {
  const { head_item_key } = useStore(StockIndexStore, (state) => state);
  const { data } = useSuspenseQuery({
    queryKey: ["Summary", head_item_key],
    queryFn: async () => {
      return await XbrlDefService.readMenuLabels({
        headItemKey: head_item_key,
      });
    },
    staleTime: 1000 * 60 * 60 * 24 * 30, // 30 days
    gcTime: 1000 * 60 * 60 * 24 * 30, // 30 days
  });
  return (
    <Box>
      {data.data.map((item, index) => {
        return (
          <Box key={index}>
            {index + 1}. {item.label}
          </Box>
        );
      })}
    </Box>
  );
};

export default Summary;
