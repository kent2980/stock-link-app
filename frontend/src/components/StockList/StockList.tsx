import { InformationService } from "@/client";
import { Box, BoxProps, List } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useWindowVirtualizer } from "@tanstack/react-virtual";
import React from "react";
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
      return await InformationService.getDocumentList({
        reportTypes: ["edjp", "edif", "edus"],
        dateStr: dateStr,
        industry17Code: industry_17_code,
      });
    },
  });

  if (!data || data.count === 0) {
    return <Box>データが見つかりません。</Box>;
  }

  const listRef = React.useRef<HTMLDivElement | null>(null);

  const virtualizer = useWindowVirtualizer({
    count: data.count,
    estimateSize: () => 400,
    overscan: 30,
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
