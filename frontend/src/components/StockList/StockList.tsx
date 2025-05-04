import { DocumentListPublics } from "@/client";
import { Box, BoxProps, Center, List } from "@chakra-ui/react";
import { useWindowVirtualizer } from "@tanstack/react-virtual";
import React from "react";
import StockListItem from "./StockListItem";

interface StockListProps extends BoxProps {
  data: DocumentListPublics;
}

export const StockList: React.FC<StockListProps> = ({ data, ...props }) => {
  if (!data || data.count === 0) {
    return (
      <Box minH="100vh">
        <Center mt={10}>データが見つかりません。</Center>
      </Box>
    );
  }

  const listRef = React.useRef<HTMLDivElement | null>(null);

  const virtualizer = useWindowVirtualizer({
    count: data.count,
    estimateSize: () => 400,
    overscan: 5,
    scrollMargin: listRef.current?.offsetTop ?? 0,
  });

  return (
    <>
      <Box
        ref={listRef}
        className="List"
        {...props}
        m={{ base: 0, md: 4 }}
        width={{ base: "100%", md: "1024px" }}
      >
        <Box
          height={virtualizer.getTotalSize()}
          width="100%"
          position="relative"
          borderTop="solid 1px"
          borderLeft="solid 1px"
          borderRight="solid 1px"
          borderColor="gray.200"
          borderRadius={{ base: "0px", md: "lg" }}
        >
          {virtualizer.getVirtualItems().map((virtualRow) => {
            const item = data.data[virtualRow.index];
            return (
              <List.Root
                key={virtualRow.key}
                data-index={virtualRow.index}
                ref={virtualizer.measureElement}
                className={
                  virtualRow.index % 2 ? "ListItemOdd" : "ListItemEven"
                }
                position="absolute"
                top={0}
                left={0}
                width="100%"
                transform={`translateY(${virtualRow.start - virtualizer.options.scrollMargin}px)`}
                listStyle={"none"}
              >
                <StockListItem item={item} />
              </List.Root>
            );
          })}
        </Box>
      </Box>
    </>
  );
};

export default StockList;
