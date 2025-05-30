import { DocumentListPublic } from "@/client";
import { Box, BoxProps, Center, List } from "@chakra-ui/react";
import { useVirtualizer } from "@tanstack/react-virtual";
import React from "react";
import StockListItem from "./StockListItem";

interface StockListProps extends BoxProps {
  data: DocumentListPublic[];
  count: number;
}

export const StockList: React.FC<StockListProps> = ({
  data,
  count,
  ...props
}) => {
  if (!data || count === 0) {
    return (
      <Box minH="100vh">
        <Center mt={10}>データが見つかりません。</Center>
      </Box>
    );
  }

  const parentRef = React.useRef<HTMLDivElement>(null);

  const virtualizer = useVirtualizer({
    count: count,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 1300,
    overscan: 3,
    gap: 2,
  });

  return (
    <>
      <Box
        ref={parentRef}
        className="List"
        {...props}
        m={{ base: 0, md: 4 }}
        width={{ base: "100%", md: "1024px" }}
        overflowY="auto" // ← 追加
        maxHeight="100vh" // ← 必要に応じて追加（高さ制限）
      >
        <List.Root
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
            const item = data[virtualRow.index];
            return (
              <List.Item
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
                scrollSnapAlign="start"
              >
                <StockListItem
                  item={item}
                  itemIndex={virtualRow.index}
                  itemCount={count}
                />
              </List.Item>
            );
          })}
        </List.Root>
      </Box>
    </>
  );
};

export default StockList;
