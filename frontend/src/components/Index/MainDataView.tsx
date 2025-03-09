import { IxService } from "@/client";
import { HeaderStore } from "@/Store/HeaderStore";
import { Box, Flex } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useStore } from "@tanstack/react-store";
import { useVirtualizer } from "@tanstack/react-virtual";
import { Suspense, useRef } from "react";
import CustomListItem from "./CustomListItem";
import CustomListRoot from "./CustomListRoot";
import IRSummary from "./IRSummary";
import SummaryHeader from "./IRSummary/SummaryHeader";

function MainDataView() {
  // APIサーバーからデータを取得
  const { data } = useSuspenseQuery({
    queryKey: ["getDocumentList"],
    queryFn: async () => {
      return await IxService.getDocumentList({});
    },
  });

  const parentRef = useRef<Element | null>(null);

  const rowVirtualizer = useVirtualizer({
    count: data.count,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 1000,
    overscan: 3,
  });

  const { height } = useStore(HeaderStore, (state) => state);

  for (let i = 0; i < data.count; i++) {
    if (!["edjp", "edif", "edus"].includes(data.data[i].report_type)) {
      rowVirtualizer.resizeItem(i, 300);
    }
  }

  return (
    <>
      <Box ref={parentRef} overflow="auto" height={`calc(100vh - ${height}px)`}>
        <CustomListRoot height={`${rowVirtualizer.getTotalSize()}px`}>
          {rowVirtualizer.getVirtualItems().map((virtualRow) => {
            const item = data.data[virtualRow.index]; // アイテムの取得
            const item_key = item.head_item_key; // アイテムキーの取得
            return (
              <CustomListItem
                key={virtualRow.index}
                top={virtualRow.start}
                height={virtualRow.size}
              >
                <Flex direction="column" gap={4} w="100%">
                  {/* ヘッダー */}
                  <SummaryHeader item={item} />
                  {/* コンテンツ */}
                  <Suspense fallback={<div>Loading...</div>}>
                    <IRSummary head_item_key={item_key} />
                  </Suspense>
                </Flex>
              </CustomListItem>
            );
          })}
        </CustomListRoot>
      </Box>
    </>
  );
}

export default MainDataView;
