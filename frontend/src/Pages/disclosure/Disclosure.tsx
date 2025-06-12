import { FinancialSummaryService } from "@/client";
import {
  Badge,
  Box,
  Button,
  Container,
  createListCollection,
  Flex,
  HStack,
  Input,
  Link,
  List,
  Select,
  Text,
} from "@chakra-ui/react";
import { useInfiniteQuery } from "@tanstack/react-query";
import { Link as RouterLink } from "@tanstack/react-router";
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
          {items?.map((item) => (
            <List.Item
              key={item?.id}
              overflow="hidden"
              style={{
                scrollSnapAlign: "start",
                scrollSnapStop: "always",
                scrollSnapType: "y mandatory",
              }}
              borderStyle="solid"
              borderColor="gray.200"
              borderBottomWidth="1px"
            >
              <Link as={RouterLink}>
                <Box p={2}>
                  <Flex
                    direction={{ base: "column", md: "row" }}
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
                      {item?.important && (
                        <Badge
                          bg="red.100"
                          color="red.800"
                          _hover={{ bg: "red.100" }}
                        >
                          重要
                        </Badge>
                      )}
                      <Box
                        as="h3"
                        fontSize="xs"
                        fontWeight="medium"
                        color="gray.900"
                      >
                        {item?.title}
                      </Box>
                      <Box as="p" fontSize="sm" color="gray.600">
                        {item?.summary}
                      </Box>
                    </Flex>
                  </Flex>
                </Box>
              </Link>
            </List.Item>
          ))}
        </List.Root>
        {isFetchingNextPage && <Box>Loading...</Box>}
        <Box visibility="hidden" height={0} ref={ref}>
          <Box />
        </Box>
      </Flex>
    </Container>
  );
}
