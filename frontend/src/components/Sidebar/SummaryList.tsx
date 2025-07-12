import { FinancialSummaryService } from "@/client";
import { Box, Container, Flex, List, Skeleton } from "@chakra-ui/react";
import { useInfiniteQuery } from "@tanstack/react-query";
import React, { useEffect, useRef } from "react";
import { useInView } from "react-intersection-observer";

const SummaryList: React.FC = () => {
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
    queryKey: ["disclosureItems17"],
    queryFn: async ({ pageParam = 1 }) => {
      return await FinancialSummaryService.getDisclosureItems({
        page: pageParam,
        limit: 20,
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
      <Box p={4} h="100vh">
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
      maxH="calc(100vh - 200px)"
      overflowY="auto"
    >
      {/* メインコンテンツ */}
      <Flex
        direction="column"
        gap={0}
        // style={{ height: contentHeight }}
      >
        {isFetchingPreviousPage && <Box>Loading previous...</Box>}
        <Box visibility="hidden" height={0} ref={prevRef}>
          <Box />
        </Box>
        <List.Root gap={4} m={4} listStyle="none">
          {items?.map((item, key) => {
            if (!item) return null;
            return <List.Item key={key}>{item.company}</List.Item>;
          })}
        </List.Root>
        {isFetchingNextPage && <LoadingItems length={20} />}
        <Box visibility="hidden" height={0} ref={ref}>
          <Box />
        </Box>
      </Flex>
    </Container>
  );
};

function LoadingItems({ length = 20 }: { length?: number }) {
  return (
    <>
      {Array.from({ length: length }).map((_, index: number) => (
        <Box key={index} p={3} bg="white" boxShadow="sm" m={3} h="60vh">
          <Flex direction="column" gap={2}>
            <Skeleton h="20vh" />
            <Skeleton h="8vh" />
            <Skeleton h="8vh" />
            <Skeleton h="8vh" />
            <Skeleton h="5vh" />
          </Flex>
        </Box>
      ))}
    </>
  );
}

export default SummaryList;
