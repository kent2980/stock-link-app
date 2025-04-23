import { IxService } from "@/client";
import { Box, BoxProps, List } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useVirtualizer } from "@tanstack/react-virtual";
import React, { useRef } from "react";
import StockListItem from "./StockListItem";

interface StockListProps extends BoxProps {
  dateStr?: string | null;
  industry_17_code?: number | null;
}

export const StockList: React.FC<StockListProps> = ({
  dateStr = null,
  industry_17_code = null,
  ...props
}) => {
  const { data } = useSuspenseQuery({
    queryKey: ["store", dateStr, industry_17_code],
    queryFn: async () => {
      return await IxService.getDocumentList({
        reportTypes: ["edjp", "edif", "edus"],
        dateStr: dateStr,
        industry17Code: industry_17_code,
      });
    },
  });

  if (!data || data.count === 0) {
    return <Box>データが見つかりません。</Box>;
  }

  const parentRef = useRef<Element | null>(null);

  const rowVirtualizer = useVirtualizer({
    count: data.count,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 1000,
    overscan: 30,
  });

  return (
    <>
      {/* デスクトップ */}
      {/* モバイル */}
      <Box
        ref={parentRef}
        w="100%"
        overflow="auto"
        height="100vh"
        {...props}
        my={2}
        css={{
          "&::-webkit-scrollbar": {
            display: "none", // Webkit系ブラウザでスクロールバーを非表示
          },
          scrollbarWidth: "none", // Firefoxでスクロールバーを非表示
        }}
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
                py={4}
              >
                <StockListItem item={item} />
              </List.Item>
            );
          })}
        </List.Root>
      </Box>
    </>
  );
};

export default StockList;
