import { IxService } from "@/client";
import { HeaderStore } from "@/Store/HeaderStore";
import { Box, Flex, List, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useStore } from "@tanstack/react-store";
import { useVirtualizer } from "@tanstack/react-virtual";
import {
  differenceInDays,
  differenceInHours,
  format,
  parseISO,
} from "date-fns";
import { ja } from "date-fns/locale";
import { Suspense, useRef } from "react";
import IRSummary from "./IRSummary";
function MainDataView() {
  return (
    <Box>
      <Suspense fallback={<div>Loading...</div>}>
        <ViewItems />
      </Suspense>
    </Box>
  );
}

export default MainDataView;

function ViewItems() {
  // APIサーバーからデータを取得
  const { data } = useSuspenseQuery({
    queryKey: ["MainDataView"],
    queryFn: async () => {
      return await IxService.getDocumentList({});
    },
  });

  const parentRef = useRef<Element | null>(null);

  const rowVirtualizer = useVirtualizer({
    count: data.count,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 1000,
    overscan: 5,
  });

  const { height } = useStore(HeaderStore, (state) => state);

  const today = new Date();

  for (let i = 0; i < data.count; i++) {
    if (["edjp", "edif", "edus"].includes(data.data[i].report_type)) {
      rowVirtualizer.resizeItem(i, 1000);
    } else {
      rowVirtualizer.resizeItem(i, 300);
    }
  }

  return (
    <>
      <Box ref={parentRef} overflow="auto" height={`calc(100vh - ${height}px)`}>
        <List.Root
          h={`${rowVirtualizer.getTotalSize()}px`}
          w="100%"
          position="relative"
          maxW={{ base: "100%", md: "calc(100vw - 250px)" }}
          m="auto" // 中央に配置
        >
          {rowVirtualizer.getVirtualItems().map((virtualRow) => {
            const item = data.data[virtualRow.index];
            const item_key = item.head_item_key;
            const date_str = item.insert_date;
            const date = parseISO(date_str);
            const diff = differenceInDays(today, date);
            const diff_hour = differenceInHours(today, date);
            const japanDate_str = format(date, "yyyy.MM.dd", {
              locale: ja,
            });
            return (
              <List.Item
                key={virtualRow.index}
                position="absolute"
                top={virtualRow.start}
                left={0}
                width="100%"
                height={virtualRow.size}
                display="flex"
                border="1px solid"
                borderColor="gray.200"
                p={4}
                bg="white"
              >
                <Flex direction="column" gap={4} w="100%">
                  {/* ヘッダー */}
                  <Flex gap={4} direction="row" w="100%">
                    {/* 投稿日 */}
                    <Box color="gray.500">
                      {diff < 1 && <Text>{diff_hour}時間前</Text>}
                      {diff >= 1 && 7 >= diff && <Text>{diff}日前</Text>}
                      {diff > 7 && <Text>{japanDate_str}</Text>}
                    </Box>
                    {/* 銘柄コード */}
                    <Box>
                      <Text>{data.data[virtualRow.index].securities_code}</Text>
                    </Box>
                    {/* 銘柄名 */}
                    <Box>
                      <Text>{data.data[virtualRow.index].company_name}</Text>
                    </Box>
                    {/* 報告書タイトル */}
                    <Box>
                      <Text>
                        {data.data[virtualRow.index].document_short_name}
                      </Text>
                    </Box>
                  </Flex>
                  {/* コンテンツ */}
                  <IRSummary head_item_key={item_key} />
                </Flex>
              </List.Item>
            );
          })}
        </List.Root>
      </Box>
    </>
  );
}
