import { IxService } from "@/client";
import { HeaderStore } from "@/Store/HeaderStore";
import { Box, BoxProps, List } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useVirtualizer } from "@tanstack/react-virtual";
import React, { useEffect, useRef } from "react";
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
    overscan: 3,
  });

  useEffect(() => {
    const handleScroll = (event: Event) => {
      const target = event.target as HTMLElement;
      console.log("Scroll position:", target.scrollTop);
      if (59 < target.scrollTop) {
        HeaderStore.setState((state) => ({
          ...state,
          height: 0,
        }));
        // id="header"の要素を取得
        const header = document.getElementById("header");
        // headerのdisplayをnoneにする
        if (header) {
          header.style.display = "none";
        }
      }
      if (target.scrollTop < 59) {
        HeaderStore.setState((state) => ({
          ...state,
          height: 59,
        }));
        const header = document.getElementById("header");
        if (header) {
          header.style.display = "block";
        }
      }
    };

    const scrollElement = parentRef.current;
    if (scrollElement) {
      scrollElement.addEventListener("scroll", handleScroll);
    }

    return () => {
      if (scrollElement) {
        scrollElement.removeEventListener("scroll", handleScroll);
      }
    };
  }, []);
  return (
    <Box ref={parentRef} w="100%" overflow="auto" height="100vh" {...props}>
      <List.Root
        height={rowVirtualizer.getTotalSize()}
        w="100%"
        position="relative"
        bg="ui.bgGradation"
        fontSize={{ base: 12, md: 16 }}
      >
        {rowVirtualizer.getVirtualItems().map((virtualRow) => {
          const item = data.data[virtualRow.index];
          return (
            <List.Item
              key={virtualRow.index}
              data-index={virtualRow.index}
              ref={rowVirtualizer.measureElement}
              position="absolute"
              top={0}
              left={0}
              transform={`translateY(${virtualRow.start}px)`}
              listStyleType="none"
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
