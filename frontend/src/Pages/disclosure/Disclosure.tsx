import {
  FinancialSummaryService,
  FinItemsResponse,
  FinValueFinance,
} from "@/client";
import {
  Box,
  Container,
  Flex,
  Heading,
  HStack,
  List,
  Skeleton,
  Text,
  VStack,
} from "@chakra-ui/react";
import { useInfiniteQuery } from "@tanstack/react-query";
import { useNavigate } from "@tanstack/react-router";
import { Calendar } from "lucide-react";
import { useEffect, useRef } from "react";
import { useInView } from "react-intersection-observer";

export default function DisclosurePage() {
  const navigate = useNavigate({ from: "disclosure" });
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
    queryKey: ["disclosureItems"],
    queryFn: async ({ pageParam = 1 }) => {
      return await FinancialSummaryService.getDisclosureItems({
        page: pageParam,
        limit: 20,
      });
    },
    gcTime: 24 * 60 * 60 * 1000, // 24時間後にガーベジコレクション
    staleTime: 10 * 60 * 1000, // 10分間のステールタイム
    initialPageParam: 1,
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

  if (isLoading || !data) {
    return <LoadingItems length={20} />;
  }

  const items = data.pages.map((page) => page.data).flat();

  const handleLinkClick = (itemId: string) => {
    // クリックされたアイテムの詳細ページへ遷移
    navigate({ to: `/disclosure/page/${itemId}` });
  };

  return (
    <Container ref={containerRef} pb={0} px={0}>
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
        <List.Root gap={0}>
          {items?.map((item, key) => {
            const ope = item?.operating_result;
            const forecast = item?.forecast;
            const cashflow = item?.cashflow;
            return (
              <List.Item
                key={key}
                overflow="hidden"
                style={{
                  scrollSnapAlign: "start",
                  scrollSnapStop: "always",
                  scrollSnapType: "y mandatory",
                }}
                m={3}
                bg="white"
                boxShadow="sm"
                onClick={() => handleLinkClick(item?.headItemKey ?? "")}
              >
                <Box p={2}>
                  <Flex
                    direction="column"
                    alignItems="flex-start"
                    justifyContent="space-between"
                    gap={1}
                  >
                    {/* 1列目 */}
                    <Flex alignItems="center" fontSize="2xs">
                      <HStack color="gray.500" gap={1}>
                        <Calendar hanging={10} width={10} color="#4381ae" />
                        <Text>{item?.insert_date ?? ""}</Text>
                      </HStack>
                    </Flex>
                    {/* 2列目 */}
                    <Flex alignItems="center" gap={2}>
                      <Box
                        as="span"
                        fontSize="sm"
                        border="1px solid"
                        borderColor="gray.200"
                        px={2}
                        bg="gray.100"
                      >
                        {item?.code}
                      </Box>
                      <Box
                        as="span"
                        fontWeight="semibold"
                        color="gray.900"
                        className="company-name"
                      >
                        {item?.company}
                      </Box>
                    </Flex>
                    {/* ３列目 */}
                    <Flex alignItems="center" gap={2}>
                      <Box
                        as="h3"
                        fontSize="xs"
                        fontWeight="medium"
                        color="gray.900"
                      >
                        {item?.title}
                      </Box>
                    </Flex>
                    {/* 4列目 */}
                    <VStack gap={2} fontSize="xs" color="gray.600" width="100%">
                      <ValueList items={ope} type="operating_result" />
                      <ValueList items={forecast} type="forecast" />
                      <ValueList items={cashflow} type="cashflow" />
                    </VStack>
                    {/* 5列目 */}
                    <Flex
                      alignItems="center"
                      gap={2}
                      fontSize="xs"
                      color="gray.600"
                    >
                      <Box
                        p={2}
                        rounded="md"
                        bg="white"
                        m={2}
                        mx="auto"
                        border="1px solid"
                        borderColor="gray.200"
                        width="100%"
                      >
                        <Text>{item?.summary}</Text>
                      </Box>
                    </Flex>
                  </Flex>
                </Box>
              </List.Item>
            );
          })}
        </List.Root>
        {isFetchingNextPage && <LoadingItems length={20} />}
        <Box visibility="hidden" height={0} ref={ref}>
          <Box />
        </Box>
      </Flex>
    </Container>
  );
}

interface ValueListProps {
  items: FinItemsResponse | null | undefined;
  type: string;
}

function ValueList({ items, type }: ValueListProps) {
  const itemValue = (item: FinValueFinance) => {
    switch (type) {
      case "operating_result":
        return item.result?.curChange?.value != null &&
          item.result?.curChange?.display_scale != null
          ? `${item.result.curChange.value.toFixed(1).toString().replace("-", "△")} ${item.result.curChange.display_scale}`
          : " - ";
      case "forecast":
        // curValue?.unitが"JPYPerShare"の場合はcurValue?.valueを表示
        if (
          item.forecast?.curValue?.unit === "JPYPerShares" &&
          item.forecast?.curValue?.value != null
        ) {
          return `${item.forecast.curValue.value.toString().replace("-", "△")} ${item.forecast.curValue.display_scale}`;
        }
        return item.forecast?.curChange?.value != null &&
          item.forecast?.curChange?.display_scale != null
          ? `${item.forecast.curChange.value.toFixed(1).toString().replace("-", "△")} ${item.forecast.curChange.display_scale}`
          : " - ";
      case "cashflow":
        return item.result?.curValue?.value != null &&
          item.result?.curValue?.display_scale != null
          ? `${item.result.curValue.value.toString().replace("-", "△")} ${item.result.curValue.display_scale}`
          : " - ";
      default:
        return " - ";
    }
  };
  const itemPreValue = (item: FinValueFinance) => {
    switch (type) {
      case "operating_result":
        return item.result?.preChange?.value != null &&
          item.result?.preChange?.display_scale != null
          ? `${item.result.preChange.value.toFixed(1).toString().replace("-", "△")} ${item.result.preChange.display_scale}`
          : " - ";
      case "forecast":
        return null;
      case "cashflow":
        return item.result?.preValue?.value != null &&
          item.result?.preValue?.display_scale != null
          ? `${item.result.preValue.value.toString().replace("-", "△")} ${item.result.preValue.display_scale}`
          : " - ";
      default:
        return " - ";
    }
  };
  const headingLabel = (type: string) => {
    switch (type) {
      case "operating_result":
        return "経営成績";
      case "forecast":
        return "業績予想";
      case "cashflow":
        return "キャッシュフロー";
      default:
        return "その他";
    }
  };
  console.log("ValueList items:", items);
  return (
    <Box w="100%" display={items ? "block" : "none"}>
      <Heading
        as="h4"
        size="xs"
        mb={2}
        px={4}
        py={1}
        color="green.600"
        borderY="1px solid"
        borderColor="gray.200"
      >
        {headingLabel(type)}
      </Heading>
      <List.Root listStyle="none">
        {items?.data?.map((item, index) => (
          <List.Item
            key={index}
            borderBottom={
              index !== (items.data?.length ?? 0) - 1 ? "1px solid" : undefined
            }
            borderColor={
              index !== (items.data?.length ?? 0) - 1 ? "gray.200" : undefined
            }
          >
            <HStack justify="space-between">
              <Text className="label">
                {item.label?.replace("によるキャッシュ・フロー", "CF")}
              </Text>
              <HStack>
                <Text className="value">{itemValue(item)}</Text>
                <Text
                  className="pre-value"
                  color="gray.500"
                  textAlign="right"
                  display={itemPreValue(item) ? "block" : "none"}
                >
                  ({itemPreValue(item)})
                </Text>
              </HStack>
            </HStack>
          </List.Item>
        ))}
      </List.Root>
    </Box>
  );
}

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
