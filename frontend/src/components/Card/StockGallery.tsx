import { DisclosureItem, FinancialSummaryService } from "@/client";
import { Box, Container, Flex, List, Skeleton, Text } from "@chakra-ui/react";
import { useInfiniteQuery } from "@tanstack/react-query";
import { Suspense, useEffect, useRef, useState } from "react";
import { useInView } from "react-intersection-observer";
import StockCard from "./StockCard";
import StockInfo from "./StockInfo";

interface StockGalleryProps {
  code_17?: number | null;
}

export default function StockGallery(props: StockGalleryProps) {
  const [discItem, setDiscItem] = useState<DisclosureItem | null>(null);
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
      <Box h="30%">
        <Suspense fallback={<Box>Loading...</Box>}>
          <StockInfo item={discItem} />
        </Suspense>
      </Box>
      {/* ヘッダーを固定表示 */}
      <Box h="70%">
        <Flex
          className="stock-card-header"
          direction="row"
          p={2}
          borderBottom="0.5px solid"
          borderColor="#545458"
          position="sticky"
          top={0}
          zIndex={1}
        >
          <Text fontSize="12px" color="#b8b8b8" w="300px" textAlign="center">
            会社名・銘柄情報
          </Text>
          <Text
            fontSize="12px"
            color="#b8b8b8"
            w="calc((100% - 300px) / 2)"
            textAlign="center"
          >
            実EPS
          </Text>
          <Text
            fontSize="12px"
            color="#b8b8b8"
            w="calc((100% - 300px) / 2)"
            textAlign="center"
          >
            予EPS
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
            >
              {items?.map((item, key) => {
                if (!item) return null;
                return (
                  <List.Item key={key} onClick={() => setDiscItem(item)}>
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
