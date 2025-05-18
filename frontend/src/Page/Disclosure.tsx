"use client";

import {
  Badge,
  Box,
  Button,
  Card,
  Container,
  createListCollection,
  Field,
  Flex,
  Heading,
  Icon,
  Input,
  Menu,
  Portal,
  Select,
  Stack,
  Tabs,
  Text,
  VStack,
} from "@chakra-ui/react";
import { Bell, Calendar, Filter, Search } from "lucide-react";

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

// 開示情報カードコンポーネント
const DisclosureCard = ({ item }: { item: (typeof disclosureData)[0] }) => {
  return (
    <Card.Root overflow="hidden" variant="outline">
      <Card.Body p={0}>
        <Box borderLeftWidth="4px" borderLeftColor="brand.500" p={4}>
          <Flex
            mb={2}
            flexWrap="wrap"
            justifyContent="space-between"
            alignItems="center"
            gap={2}
          >
            <Flex alignItems="center">
              <Text mr={2} fontWeight="semibold" color="gray.900">
                {item.company}
              </Text>
              <Text fontSize="sm" color="gray.500">
                {item.code}
              </Text>
              {item.important && (
                <Badge ml={2} colorScheme="red" variant="subtle">
                  重要
                </Badge>
              )}
            </Flex>
            <Flex alignItems="center">
              <Badge variant="outline" mr={2}>
                {item.category}
              </Badge>
              <Text fontSize="sm" color="gray.500">
                {formatDate(item.date)}
              </Text>
            </Flex>
          </Flex>
          <Heading
            as="h3"
            size="md"
            mb={1}
            fontWeight="medium"
            color="gray.900"
          >
            {item.title}
          </Heading>
          <Text fontSize="sm" color="gray.600">
            {item.summary}
          </Text>
          <Box mt={3} textAlign="right">
            <Button colorScheme="brand">詳細を見る</Button>
          </Box>
        </Box>
      </Card.Body>
    </Card.Root>
  );
};

export default function DisclosurePage() {
  const frameworks = createListCollection({
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
    <Box minH="100vh">
      <Container as="main" maxW="container.xl" py={6} px={0}>
        <Box mb={6} bg="white" p={4} borderRadius="lg" shadow="sm">
          <Stack
            direction={{ base: "column", md: "row" }}
            gap={4}
            alignItems={{ md: "center" }}
          >
            <Field.Root flexGrow={1}>
              <Field.Label pointerEvents="none">
                <Search size={16} color="gray.400" />
              </Field.Label>
              <Input placeholder="企業名・銘柄コード・キーワードで検索" />
            </Field.Root>
            <Flex alignItems="center" gap={2}>
              <Menu.Root>
                <Menu.Trigger>
                  <Button variant="outline" size="sm">
                    <Filter /> フィルター
                  </Button>
                </Menu.Trigger>
              </Menu.Root>
              <Select.Root collection={frameworks}>
                <Select.Control>
                  <Select.Trigger>
                    <Select.ValueText placeholder="カテゴリ" />
                  </Select.Trigger>
                  <Select.IndicatorGroup>
                    <Select.Indicator />
                  </Select.IndicatorGroup>
                </Select.Control>
                <Portal>
                  <Select.Positioner>
                    <Select.Content>
                      {frameworks.items.map((framework) => (
                        <Select.Item item={framework} key={framework.value}>
                          {framework.label}
                          <Select.ItemIndicator />
                        </Select.Item>
                      ))}
                    </Select.Content>
                  </Select.Positioner>
                </Portal>
              </Select.Root>
              <Flex
                w="300px"
                alignItems="center"
                gap={2}
                borderWidth={1}
                borderColor="gray.200"
                borderRadius="md"
                p={2}
              >
                <Icon size="md">
                  <Calendar />
                </Icon>
                <Text fontSize="md">日付</Text>
              </Flex>
            </Flex>
          </Stack>
        </Box>

        <Tabs.Root variant="line" colorScheme="brand" mb={6}>
          <Tabs.List>
            <Tabs.Trigger value="all">すべて</Tabs.Trigger>
            <Tabs.Trigger value="important">
              <Flex alignItems="center">
                <Bell
                  size={16}
                  color="#34B47F"
                  style={{ marginRight: "4px" }}
                />
                重要
              </Flex>
            </Tabs.Trigger>
            <Tabs.Trigger value="today">本日</Tabs.Trigger>
            <Tabs.Trigger value="yesterday">昨日</Tabs.Trigger>
          </Tabs.List>
          <Tabs.ContentGroup>
            <Tabs.Content value="all" px={0} pt={4}>
              <VStack gap={4} align="stretch">
                {disclosureData.map((item) => (
                  <DisclosureCard key={item.id} item={item} />
                ))}
              </VStack>
            </Tabs.Content>
            <Tabs.Content value="important" px={0} pt={4}>
              <VStack gap={4} align="stretch">
                {disclosureData
                  .filter((item) => item.important)
                  .map((item) => (
                    <DisclosureCard key={item.id} item={item} />
                  ))}
              </VStack>
            </Tabs.Content>
            <Tabs.Content value="today" px={0} pt={4}>
              <VStack gap={4} align="stretch">
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
                    <DisclosureCard key={item.id} item={item} />
                  ))}
              </VStack>
            </Tabs.Content>
            <Tabs.Content value="yesterday" px={0} pt={4}>
              <VStack gap={4} align="stretch">
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
                    <DisclosureCard key={item.id} item={item} />
                  ))}
              </VStack>
            </Tabs.Content>
          </Tabs.ContentGroup>
        </Tabs.Root>

        <Flex justify="center" mt={8}>
          <Button variant="outline" mx={2}>
            前の10件
          </Button>
          <Button variant="outline" mx={2}>
            次の10件
          </Button>
        </Flex>
      </Container>
    </Box>
  );
}
