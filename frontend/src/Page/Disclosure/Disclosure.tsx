import {
  Badge,
  Box,
  Button,
  Card,
  createListCollection,
  Flex,
  Input,
  Link,
  Select,
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@chakra-ui/react";
import { Link as RouterLink } from "@tanstack/react-router";
import {
  Bell,
  Calendar,
  ChevronDown,
  ChevronUp,
  Filter,
  Search,
  SlidersHorizontal,
} from "lucide-react";
import { useRef, useState } from "react";
// モックデータ - 実際のアプリでは API から取得
const disclosureData = [
  {
    id: 1,
    company: "テクノ株式会社",
    code: "1234",
    date: "2025-05-18T14:30:00",
    title: "2025年3月期 決算短信〔日本基準〕（連結）",
    summary: "売上高10%増、営業利益15%増の好決算を発表",
    category: "決算短信",
    important: true,
  },
  {
    id: 2,
    company: "グローバル商事",
    code: "5678",
    date: "2025-05-18T13:15:00",
    title: "新製品開発に関するお知らせ",
    summary: "AI技術を活用した新サービスの開発を発表",
    category: "その他",
    important: false,
  },
  {
    id: 3,
    company: "未来電機",
    code: "9012",
    date: "2025-05-18T10:00:00",
    title: "代表取締役の異動に関するお知らせ",
    summary: "6月1日付けで代表取締役社長が交代",
    category: "役員異動",
    important: true,
  },
  {
    id: 4,
    company: "東京建設",
    code: "3456",
    date: "2025-05-17T16:45:00",
    title: "配当予想の修正に関するお知らせ",
    summary: "期末配当を1株当たり5円増配し、年間配当は25円に",
    category: "配当",
    important: true,
  },
  {
    id: 5,
    company: "日本物流",
    code: "7890",
    date: "2025-05-17T15:30:00",
    title: "自己株式取得に係る事項の決定に関するお知らせ",
    summary:
      "取得株式数100万株、取得価額の総額20億円を上限とした自己株式の取得を決定",
    category: "自己株式",
    important: false,
  },
  {
    id: 6,
    company: "メディカルサイエンス",
    code: "2345",
    date: "2025-05-17T14:00:00",
    title: "臨床試験結果に関するお知らせ",
    summary: "新薬の第III相臨床試験において主要評価項目を達成",
    category: "その他",
    important: true,
  },
  {
    id: 7,
    company: "エネルギー開発",
    code: "6789",
    date: "2025-05-17T11:20:00",
    title: "業績予想の修正に関するお知らせ",
    summary: "原材料価格の高騰により、営業利益予想を10%下方修正",
    category: "業績予想",
    important: true,
  },
  {
    id: 8,
    company: "デジタルソリューションズ",
    code: "0123",
    date: "2025-05-16T16:00:00",
    title: "子会社の設立に関するお知らせ",
    summary: "東南アジア市場開拓のため、シンガポールに子会社を設立",
    category: "その他",
    important: false,
  },
];

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

  return (
    <Box ref={containerRef} pb={{ base: 6, md: 0 }}>
      {/* フィルターボタン */}
      <CustomFilterButton
        showFilters={showFilters}
        setShowFilters={setShowFilters}
      />
      {/* メインコンテンツ */}
      <Box className="container mx-auto px-4 py-6 h-full flex flex-col">
        <Tabs.Root
          mt={6}
          defaultValue="all"
          display="flex"
          flexDirection="column"
          flex="1"
        >
          <TabsList>
            <TabsTrigger value="all">すべて</TabsTrigger>
            <TabsTrigger value="important" display="flex" alignItems="center">
              <Bell className="mr-1 h-4 w-4 text-emerald-600" />
              重要
            </TabsTrigger>
            <TabsTrigger value="today">本日</TabsTrigger>
            <TabsTrigger value="yesterday">昨日</TabsTrigger>
          </TabsList>

          <TabsContent value="all" mt={4} flex="1">
            <Flex
              overflowY="auto"
              direction="column"
              gap={4}
              // style={{ height: contentHeight }}
            >
              {disclosureData.map((item) => (
                <Card.Root
                  key={item.id}
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
                              {item.company}
                            </Box>
                            <Box as="span" fontSize="sm" color="gray.500">
                              {item.code}
                            </Box>
                            {item.important && (
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
                              {item.category}
                            </Badge>
                            <Box as="span" fontSize="sm" color="gray.500">
                              {formatDate(item.date)}
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
                          {item.title}
                        </Box>
                        <Box as="p" fontSize="sm" color="gray.600">
                          {item.summary}
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
            </Flex>
          </TabsContent>

          <TabsContent value="important" mt={4} flex="1">
            <Flex overflowY="auto" direction="column" gap={4}>
              {disclosureData
                .filter((item) => item.important)
                .map((item) => (
                  <Card.Root
                    key={item.id}
                    className="overflow-hidden snap-start snap-always"
                  >
                    <Card.Body className="p-0">
                      <Link as={RouterLink}>
                        <Box
                          borderLeft="4px solid"
                          borderColor="emerald.500"
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
                                {item.company}
                              </Box>
                              <Box as="span" fontSize="sm" color="gray.500">
                                {item.code}
                              </Box>
                              <Badge
                                ml={2}
                                bg="red.100"
                                color="red.800"
                                _hover={{ bg: "red.100" }}
                              >
                                重要
                              </Badge>
                            </Box>
                            <Box display="flex" alignItems="center">
                              <Badge variant="outline" mr={2}>
                                {item.category}
                              </Badge>
                              <Box as="span" fontSize="sm" color="gray.500">
                                {formatDate(item.date)}
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
                            {item.title}
                          </Box>
                          <Box as="p" fontSize="sm" color="gray.600">
                            {item.summary}
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
            </Flex>
          </TabsContent>

          <TabsContent value="today" className="mt-4 flex-grow overflow-hidden">
            <Flex overflowY="auto" direction="column" gap={4}>
              {disclosureData
                .filter((item) => {
                  const today = new Date();
                  const itemDate = new Date(item.date);
                  return (
                    itemDate.getDate() === today.getDate() &&
                    itemDate.getMonth() === today.getMonth() &&
                    itemDate.getFullYear() === today.getFullYear()
                  );
                })
                .map((item) => (
                  <Card.Root
                    key={item.id}
                    className="overflow-hidden snap-start snap-always"
                  >
                    <Card.Body className="p-0">
                      <Link as={RouterLink}>
                        <Box
                          borderLeft="4px solid"
                          borderColor="emerald.500"
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
                                {item.company}
                              </Box>
                              <Box as="span" fontSize="sm" color="gray.500">
                                {item.code}
                              </Box>
                              {item.important && (
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
                                {item.category}
                              </Badge>
                              <Box as="span" fontSize="sm" color="gray.500">
                                {formatDate(item.date)}
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
                            {item.title}
                          </Box>
                          <Box as="p" fontSize="sm" color="gray.600">
                            {item.summary}
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
            </Flex>
          </TabsContent>

          <TabsContent
            value="yesterday"
            className="mt-4 flex-grow overflow-hidden"
          >
            <Flex overflowY="auto" direction="column" gap={4}>
              {disclosureData
                .filter((item) => {
                  const today = new Date();
                  const yesterday = new Date(today);
                  yesterday.setDate(yesterday.getDate() - 1);
                  const itemDate = new Date(item.date);
                  return (
                    itemDate.getDate() === yesterday.getDate() &&
                    itemDate.getMonth() === yesterday.getMonth() &&
                    itemDate.getFullYear() === yesterday.getFullYear()
                  );
                })
                .map((item) => (
                  <Card.Root
                    key={item.id}
                    className="overflow-hidden snap-start snap-always"
                  >
                    <Card.Body className="p-0">
                      <Link as={RouterLink}>
                        <Box
                          borderLeft="4px solid"
                          borderColor="emerald.500"
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
                                {item.company}
                              </Box>
                              <Box as="span" fontSize="sm" color="gray.500">
                                {item.code}
                              </Box>
                              {item.important && (
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
                                {item.category}
                              </Badge>
                              <Box as="span" fontSize="sm" color="gray.500">
                                {formatDate(item.date)}
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
                            {item.title}
                          </Box>
                          <Box as="p" fontSize="sm" color="gray.600">
                            {item.summary}
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
            </Flex>
          </TabsContent>
        </Tabs.Root>
      </Box>
    </Box>
  );
}
