import {
  FinancialSummaryService,
  FinItemsResponse,
  FinValueFinance,
} from "@/client";
import {
  Box,
  Button,
  Container,
  createListCollection,
  Flex,
  Heading,
  HStack,
  Input,
  List,
  Select,
  Text,
} from "@chakra-ui/react";
import { useInfiniteQuery } from "@tanstack/react-query";
import { useNavigate } from "@tanstack/react-router";
import {
  Calendar,
  ChevronDown,
  ChevronUp,
  Filter,
  Search,
  SlidersHorizontal,
} from "lucide-react";
import { useEffect, useRef, useState } from "react";
import { useInView } from "react-intersection-observer";

function CustomFilterButton({
  showFilters,
  setShowFilters,
}: {
  showFilters: boolean;
  setShowFilters: (show: boolean) => void;
}) {
  const selectItems = createListCollection({
    items: [
      { value: "all", label: "すべて" },
      { value: "financial", label: "決算短信" },
      { value: "dividend", label: "配当" },
      { value: "forecast", label: "業績予想" },
      { value: "management", label: "役員異動" },
      { value: "stock", label: "自己株式" },
      { value: "other", label: "その他" },
    ],
  });

  return (
    <>
      {/* 検索・フィルターボタン（固定表示） */}
      <Box
        zIndex={10}
        position="fixed"
        right={4}
        top="80px"
        display="flex"
        justifyContent="flex-end"
        mb={4}
      >
        <Button
          onClick={() => setShowFilters(!showFilters)}
          variant="solid"
          size="sm"
          borderRadius="full"
          boxShadow="md"
          bg="emerald.600"
          _hover={{ bg: "emerald.700" }}
          color="white"
          display="flex"
          alignItems="center"
        >
          <SlidersHorizontal className="h-4 w-4 mr-2" />
          {showFilters ? "フィルターを閉じる" : "検索・フィルター"}
          {showFilters ? (
            <ChevronUp className="h-4 w-4 ml-2" />
          ) : (
            <ChevronDown className="h-4 w-4 ml-2" />
          )}
        </Button>
      </Box>

      {/* 検索・フィルターエリア（トグル表示） */}
      {showFilters && (
        <Box
          mb={6}
          rounded="lg"
          bg="white"
          p={4}
          boxShadow="sm"
          transition="all 0.3s ease-in-out"
        >
          <Box
            display="flex"
            flexDirection={{ base: "column", md: "row" }}
            alignItems={{ md: "center" }}
            gap={{ base: 4, md: 0 }}
          >
            <Box
              position="relative"
              flex="1"
              mb={{ base: 4, md: 0 }}
              mr={{ md: 4 }}
            >
              <Box
                as={Search}
                position="absolute"
                left="12px"
                top="50%"
                transform="translateY(-50%)"
                h={4}
                w={4}
                color="gray.400"
                pointerEvents="none"
              />
              <Input
                placeholder="企業名・銘柄コード・キーワードで検索"
                pl="32px"
              />
            </Box>
            <Box display="flex" flexWrap="wrap" alignItems="center" gap={2}>
              <Button
                variant="outline"
                size="sm"
                display="flex"
                alignItems="center"
              >
                <Filter style={{ marginRight: 8, height: 16, width: 16 }} />
                <Box as="span">フィルター</Box>
              </Button>
              <Box w="180px">
                <Select.Root
                  collection={selectItems}
                  size="sm"
                  placeholder="カテゴリー"
                >
                  {selectItems.items.map((item) => (
                    <Select.Item key={item.value} item={item}>
                      {item.label}
                    </Select.Item>
                  ))}
                </Select.Root>
              </Box>
              <Button
                variant="outline"
                size="sm"
                display="flex"
                alignItems="center"
              >
                <Calendar style={{ marginRight: 8, height: 16, width: 16 }} />
                <Box as="span">日付</Box>
              </Button>
            </Box>
          </Box>
        </Box>
      )}
    </>
  );
}

export default function DisclosurePage() {
  const navigate = useNavigate({ from: "disclosure" });
  const [showFilters, setShowFilters] = useState(false);
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
      });
    },
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
    return <div>Loading...</div>;
  }

  const items = data.pages.map((page) => page.data).flat();

  const handleLinkClick = (itemId: string) => {
    // クリックされたアイテムの詳細ページへ遷移
    navigate({ to: `/disclosure/page/${itemId}` });
  };

  return (
    <Container ref={containerRef} pb={0} pt={12} px={0}>
      {/* フィルターボタン */}
      <CustomFilterButton
        showFilters={showFilters}
        setShowFilters={setShowFilters}
      />
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
        <List.Root
          border="1px solid"
          borderColor="gray.200"
          borderTopWidth="1px"
          borderXWidth="1px"
        >
          {items?.map((item, key) => {
            const ope: FinItemsResponse = JSON.parse(
              item?.operating_result_json ?? "{}"
            );
            const forecast: FinItemsResponse = JSON.parse(
              item?.forecast_json ?? "{}"
            );
            const cashflow: FinItemsResponse = JSON.parse(
              item?.cashflow_json ?? "{}"
            );
            return (
              <List.Item
                key={key}
                overflow="hidden"
                style={{
                  scrollSnapAlign: "start",
                  scrollSnapStop: "always",
                  scrollSnapType: "y mandatory",
                }}
                borderStyle="solid"
                borderColor="gray.200"
                borderBottomWidth="1px"
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
                      <Box as="span" fontSize="sm" color="gray.500">
                        {item?.code}
                      </Box>
                      <Box as="span" fontWeight="semibold" color="gray.900">
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
                    <Flex
                      direction="column"
                      alignItems="center"
                      gap={2}
                      fontSize="xs"
                      color="gray.600"
                    >
                      <ValueList items={ope} type="operating_result" />
                      <ValueList items={forecast} type="forecast" />
                      <ValueList items={cashflow} type="cashflow" />
                    </Flex>
                    {/* 5列目 */}
                    <Flex
                      alignItems="center"
                      gap={2}
                      fontSize="xs"
                      color="gray.600"
                    >
                      <Box>
                        <Heading as="h4" size="xs" mb={1}>
                          概要
                        </Heading>
                        <Text>{item?.summary}</Text>
                      </Box>
                    </Flex>
                  </Flex>
                </Box>
              </List.Item>
            );
          })}
        </List.Root>
        {isFetchingNextPage && <Box>Loading...</Box>}
        <Box visibility="hidden" height={0} ref={ref}>
          <Box />
        </Box>
      </Flex>
    </Container>
  );
}

interface ValueListProps {
  items: FinItemsResponse;
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
  return (
    <Box w="100vw">
      <Heading as="h4" size="xs" mb={2} bg="gray.100" px={4} py={1}>
        {headingLabel(type)}
      </Heading>
      <List.Root listStyle="none">
        {items?.data?.map((item, index) => (
          <List.Item
            key={index}
            px={6}
            borderBottom={
              index !== (items.data?.length ?? 0) - 1 ? "1px solid" : undefined
            }
            borderColor={
              index !== (items.data?.length ?? 0) - 1 ? "gray.200" : undefined
            }
          >
            <HStack justify="space-between">
              <Text className="label">{item.label}</Text>
              <Text className="value">{itemValue(item)}</Text>
            </HStack>
          </List.Item>
        ))}
      </List.Root>
    </Box>
  );
}
