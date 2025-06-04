import {
  FinancialSummaryGetDisclosureItemsResponse,
  FinancialSummaryService,
} from "@/client";
import {
  Badge,
  Box,
  Button,
  Card,
  Container,
  createListCollection,
  Flex,
  Input,
  Link,
  Select,
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

// 日付をフォーマットする関数
function formatDate(dateString: string) {
  const date = new Date(dateString);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  const hours = String(date.getHours()).padStart(2, "0");
  const minutes = String(date.getMinutes()).padStart(2, "0");

  return `${year}/${month}/${day} ${hours}:${minutes}`;
}

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
  const { data, isLoading, hasNextPage, fetchNextPage, isFetchingNextPage } =
    useInfiniteQuery({
      queryKey: ["disclosureItems"],
      queryFn: async () => {
        return await FinancialSummaryService.getDisclosureItems();
      },
      initialPageParam: 0,
      getNextPageParam: (
        lastPage: FinancialSummaryGetDisclosureItemsResponse
      ) => (lastPage.offset != null ? lastPage.offset : undefined),
    });
  const { ref, inView } = useInView();

  useEffect(() => {
    if (hasNextPage && inView) {
      fetchNextPage();
    }
  }, [inView, hasNextPage, fetchNextPage]);

  if (isLoading || !data) {
    return <div>Loading...</div>;
  }

  const items = data.pages.map((page) => page.data).flat();

  return (
    <Container
      ref={containerRef}
      pb={{ base: 6, md: 0 }}
      pt={12}
      px={{ base: 0, md: 4 }}
    >
      {/* フィルターボタン */}
      <CustomFilterButton
        showFilters={showFilters}
        setShowFilters={setShowFilters}
      />
      {/* メインコンテンツ */}
      <Flex
        direction="column"
        gap={4}
        // style={{ height: contentHeight }}
      >
        {items?.map((item) => (
          <Card.Root
            key={item?.id}
            className="overflow-hidden snap-start snap-always"
          >
            <Card.Body className="p-0" p={0}>
              <Link as={RouterLink}>
                <Box
                  borderLeft="4px solid"
                  borderColor="green.emphasized"
                  p={4}
                >
                  <Box
                    mb={2}
                    display="flex"
                    flexWrap="wrap"
                    alignItems="center"
                    justifyContent="space-between"
                    gap={2}
                  >
                    <Box display="flex" alignItems="center">
                      <Box
                        as="span"
                        mr={2}
                        fontWeight="semibold"
                        color="gray.900"
                      >
                        {item?.company}
                      </Box>
                      <Box as="span" fontSize="sm" color="gray.500">
                        {item?.code}
                      </Box>
                      {item?.important && (
                        <Badge
                          ml={2}
                          bg="red.100"
                          color="red.800"
                          _hover={{ bg: "red.100" }}
                        >
                          重要
                        </Badge>
                      )}
                    </Box>
                    <Box display="flex" alignItems="center">
                      <Badge variant="outline" mr={2}>
                        {item?.category}
                      </Badge>
                      <Box as="span" fontSize="sm" color="gray.500">
                        {formatDate(item?.date ?? "")}
                      </Box>
                    </Box>
                  </Box>
                  <Box
                    as="h3"
                    mb={1}
                    fontSize="lg"
                    fontWeight="medium"
                    color="gray.900"
                  >
                    {item?.title}
                  </Box>
                  <Box as="p" fontSize="sm" color="gray.600">
                    {item?.summary}
                  </Box>
                  <Box mt={3} textAlign="right">
                    <Button
                      color="emerald.600"
                      _hover={{ color: "emerald.700" }}
                    >
                      詳細を見る
                    </Button>
                  </Box>
                </Box>
              </Link>
            </Card.Body>
          </Card.Root>
        ))}
        {isFetchingNextPage && <div>Loading...</div>}
      </Flex>
    </Container>
  );
}
