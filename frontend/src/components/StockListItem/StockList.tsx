import { IxService } from "@/client";
import { Box, BoxProps, List } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useVirtualizer } from "@tanstack/react-virtual";
import React, { useRef } from "react";
import StockListItem from "./StockListItem";

interface StockListProps extends BoxProps {}

export const StockList: React.FC<StockListProps> = (props) => {
  const { data } = useSuspenseQuery({
    queryKey: ["store"],
    queryFn: async () => {
      return await IxService.getDocumentList({
        reportTypes: ["edjp", "edif", "edus"],
      });
    },
  });
  const parentRef = useRef<Element | null>(null);

  const rowVirtualizer = useVirtualizer({
    count: data.count,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 1000,
    overscan: 10,
  });

  return (
    <Box
      ref={parentRef}
      w="100%"
      overflow="auto"
      height="100vh"
      {...props}
      my={2}
    >
      <List.Root
        height={rowVirtualizer.getTotalSize()}
        w="100%"
        position="relative"
        fontSize={{ base: 12, md: 16 }}
        alignItems="center"
      >
        {rowVirtualizer.getVirtualItems().map((virtualRow) => {
          const item = data.data[virtualRow.index];
          return (
            <List.Item
              key={virtualRow.index}
              data-index={virtualRow.index}
              ref={rowVirtualizer.measureElement}
              position="absolute"
              transform={`translateY(${virtualRow.start}px)`}
              listStyleType="none"
              w={{ base: "100%", md: "720px" }}
              borderBottom="1px solid"
              borderColor="gray.200"
              py={4}
            >
              <StockListItem item={item} />
            </List.Item>
          );
        })}
      </List.Root>
    </Box>
  );
};

export default StockList;
