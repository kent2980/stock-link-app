import { DisclosureItem, FinancialSummaryService } from "@/client";
import {
  Box,
  Container,
  Flex,
  List,
  Popover,
  Portal,
  Skeleton,
  Text,
} from "@chakra-ui/react";
import { useInfiniteQuery } from "@tanstack/react-query";
import { Suspense, useEffect, useRef, useState } from "react";
import { useInView } from "react-intersection-observer";
import DatePickerDial from "../Common/DatePickerDial";
import StockCard from "./StockCard";
import StockInfo from "./StockInfo";

interface StockGalleryProps {
  code_17?: number | null;
}

export default function StockGallery(props: StockGalleryProps) {
  const [discItem, setDiscItem] = useState<DisclosureItem | null>(null);
  const [selectDate, setSelectDate] = useState<string | null>(null);
  const [open, setOpen] = useState(false);
  // コード17をpropsから取得
  const { code_17 } = props;
  // const navigate = useNavigate({ from: "disclosure" });
  const containerRef = useRef<HTMLDivElement>(null);
  const {
    data,
    isLoading,
    hasNextPage,
    fetchNextPage,
    isFetchingNextPage,
    hasPreviousPage,
    fetchPreviousPage,
    isFetchingPreviousPage,
  } = useInfiniteQuery({
    queryKey: ["disclosureItems17", code_17],
    queryFn: async ({ pageParam = 1 }) => {
      return await FinancialSummaryService.getDisclosureItems({
        page: pageParam,
        limit: 20,
        code17: code_17,
        isDistinct: false,
        selectDate: selectDate,
      });
    },
    gcTime: 24 * 60 * 60 * 1000, // 24時間後にガーベジコレクション
    staleTime: 10 * 60 * 1000, // 10分間のステールタイム
    initialPageParam: 1,
    retry: false,
    getNextPageParam: (lastPage) =>
      lastPage.next_page ? lastPage.page + 1 : undefined,
    getPreviousPageParam: (firstPage) =>
      firstPage.previous_page ? firstPage.page - 1 : undefined,
  });
  const { ref, inView } = useInView();
  const { ref: prevRef, inView: prevInView } = useInView();

  useEffect(() => {
    if (hasNextPage && inView) {
      fetchNextPage();
    }
  }, [inView, hasNextPage, fetchNextPage]);

  useEffect(() => {
    if (hasPreviousPage && prevInView) {
      fetchPreviousPage();
    }
  }, [prevInView, hasPreviousPage, fetchPreviousPage]);

  if (isLoading) {
    return <LoadingItems length={20} />;
  } else if (!data) {
    return (
      <Box p={4} h="100%">
        No data available
      </Box>
    );
  }

  const items = data.pages.map((page) => page.data).flat();

  return (
    <Container
      ref={containerRef}
      pb={0}
      px={0}
      h="100%"
      maxW="100vw"
      overflowY="hidden"
    >
      <Box h="250px">
        <Suspense fallback={<Box>Loading...</Box>}>
          <StockInfo item={discItem} />
        </Suspense>
      </Box>
      {/* ヘッダーを固定表示 */}
      <Box h="calc(100% - 250px)">
        <Flex
          className="stock-card-header"
          direction="row"
          p={1}
          borderBottom="0.5px solid"
          borderColor="#545458"
          position="sticky"
          top={0}
          zIndex={1}
        >
          <Text
            fontSize="10px"
            color="#b8b8b8"
            w={{ base: "60vw", md: "300px" }}
            textAlign="center"
          >
            会社名
            <br />
            銘柄情報
          </Text>
          <Text fontSize="10px" color="#b8b8b8" flex={1} textAlign="center">
            実利益
            <br />
            増減率
          </Text>
          <Text fontSize="10px" color="#b8b8b8" flex={1} textAlign="center">
            予利益
            <br />
            増減率
          </Text>
        </Flex>
        {/* リスト部分のみスクロール */}
        <Box flex="1" overflowY="auto" h="calc(100% - 48px)">
          <Flex direction="column" gap={0}>
            {isFetchingPreviousPage && <Box>Loading previous...</Box>}
            <Box visibility="hidden" height={0} ref={prevRef}>
              <Box />
            </Box>
            <List.Root
              className="stock-card-list"
              gap={0}
              m={4}
              listStyle="none"
              style={{
                scrollSnapType: "y mandatory",
                overflowY: "auto",
                maxHeight: "100%",
                padding: 0,
              }}
            >
              {items?.map((item, key) => {
                if (!item) return null;
                if (key === 0 && !discItem) {
                  setDiscItem(item);
                }
                return (
                  <List.Item
                    key={key}
                    onClick={() => setDiscItem(item)}
                    cursor="pointer"
                    scrollSnapAlign="start"
                    bg={discItem === item ? "#383a40" : "transparent"}
                  >
                    <Suspense fallback={<LoadingItems length={1} />}>
                      <StockCard item={item} />
                    </Suspense>
                  </List.Item>
                );
              })}
            </List.Root>
            {isFetchingNextPage && <LoadingItems length={20} />}
            <Box visibility="hidden" height={0} ref={ref}>
              <Box />
            </Box>
          </Flex>
        </Box>
      </Box>
      {/* 画面右下にフロートボタンを表示 */}

      {/*  */}
      <Popover.Root open={open} onOpenChange={(e) => setOpen(e.open)}>
        <Popover.Trigger asChild>
          <Box
            position="fixed"
            bottom={20}
            right={4}
            zIndex={1000}
            bg="rgba(255, 255, 255, 1)"
            p={2}
            borderRadius="full"
            boxShadow="md"
            onClick={() =>
              setSelectDate(new Date().toISOString().split("T")[0])
            }
            cursor="pointer"
          >
            <Text fontSize="12px" color="black">
              日付選択
            </Text>
          </Box>
        </Popover.Trigger>
        <Portal>
          <Popover.Positioner>
            <Popover.Content>
              <Popover.Arrow />
              <Popover.Body>
                <Box color="black" fontSize="16px">
                  <DatePickerDial />
                </Box>
              </Popover.Body>
            </Popover.Content>
          </Popover.Positioner>
        </Portal>
      </Popover.Root>
    </Container>
  );
}

function LoadingItems({ length = 20 }: { length?: number }) {
  return (
    <Flex gap={4}>
      {Array.from({ length: length }).map((_, index: number) => (
        <Skeleton h="30px" key={index} />
      ))}
    </Flex>
  );
}
