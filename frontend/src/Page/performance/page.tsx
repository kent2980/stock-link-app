import {
  Badge,
  Box,
  Button,
  Card,
  Checkbox,
  Collapsible,
  Container,
  Heading,
  Input,
  Link,
  Menu,
  Select,
  Separator,
  Table,
  Tabs,
  Text,
  createListCollection,
} from "@chakra-ui/react";
import {
  ArrowLeft,
  BarChart3,
  ChevronDown,
  Download,
  Filter,
  LineChart,
  Search,
  SlidersHorizontal,
} from "lucide-react";
import { useState } from "react";

interface Company {
  id: number;
  name: string;
  code: string;
  sector: string;
  industry: string;
  financials: {
    revenue: Record<string, number>;
    operatingProfit: Record<string, number>;
    netIncome: Record<string, number>;
    eps: Record<string, number>;
    roe: Record<string, number>;
    per: Record<string, number>;
    pbr: Record<string, number>;
  };
}

// モックデータ - 実際のアプリでは API から取得
const companiesData: Company[] = [
  {
    id: 1,
    name: "テクノ株式会社",
    code: "1234",
    sector: "情報・通信業",
    industry: "ソフトウェア",
    financials: {
      revenue: {
        "2023": 13800,
        "2024": 15200,
        "2025": 16500,
      },
      operatingProfit: {
        "2023": 1605,
        "2024": 1850,
        "2025": 2050,
      },
      netIncome: {
        "2023": 1108,
        "2024": 1250,
        "2025": 1390,
      },
      eps: {
        "2023": 55.4,
        "2024": 62.5,
        "2025": 69.5,
      },
      roe: {
        "2023": 6.8,
        "2024": 7.2,
        "2025": 7.6,
      },
      per: {
        "2023": 18.2,
        "2024": 16.8,
        "2025": 15.1,
      },
      pbr: {
        "2023": 1.2,
        "2024": 1.1,
        "2025": 1.0,
      },
    },
  },
  {
    id: 2,
    name: "グローバル商事",
    code: "5678",
    sector: "卸売業",
    industry: "総合商社",
    financials: {
      revenue: {
        "2023": 42500,
        "2024": 45800,
        "2025": 48200,
      },
      operatingProfit: {
        "2023": 3200,
        "2024": 3650,
        "2025": 3950,
      },
      netIncome: {
        "2023": 2100,
        "2024": 2450,
        "2025": 2750,
      },
      eps: {
        "2023": 105.0,
        "2024": 122.5,
        "2025": 137.5,
      },
      roe: {
        "2023": 8.4,
        "2024": 9.2,
        "2025": 9.8,
      },
      per: {
        "2023": 12.5,
        "2024": 11.8,
        "2025": 10.9,
      },
      pbr: {
        "2023": 1.0,
        "2024": 0.9,
        "2025": 0.8,
      },
    },
  },
  {
    id: 3,
    name: "未来電機",
    code: "9012",
    sector: "電気機器",
    industry: "電子部品",
    financials: {
      revenue: {
        "2023": 28600,
        "2024": 31200,
        "2025": 33500,
      },
      operatingProfit: {
        "2023": 2450,
        "2024": 2850,
        "2025": 3150,
      },
      netIncome: {
        "2023": 1650,
        "2024": 1950,
        "2025": 2200,
      },
      eps: {
        "2023": 82.5,
        "2024": 97.5,
        "2025": 110.0,
      },
      roe: {
        "2023": 7.8,
        "2024": 8.6,
        "2025": 9.2,
      },
      per: {
        "2023": 15.8,
        "2024": 14.2,
        "2025": 13.1,
      },
      pbr: {
        "2023": 1.1,
        "2024": 1.0,
        "2025": 0.9,
      },
    },
  },
  {
    id: 4,
    name: "東京建設",
    code: "3456",
    sector: "建設業",
    industry: "総合建設",
    financials: {
      revenue: {
        "2023": 35200,
        "2024": 36800,
        "2025": 38500,
      },
      operatingProfit: {
        "2023": 1850,
        "2024": 2050,
        "2025": 2250,
      },
      netIncome: {
        "2023": 1250,
        "2024": 1400,
        "2025": 1550,
      },
      eps: {
        "2023": 62.5,
        "2024": 70.0,
        "2025": 77.5,
      },
      roe: {
        "2023": 6.2,
        "2024": 6.8,
        "2025": 7.2,
      },
      per: {
        "2023": 14.5,
        "2024": 13.8,
        "2025": 12.9,
      },
      pbr: {
        "2023": 0.9,
        "2024": 0.8,
        "2025": 0.8,
      },
    },
  },
  {
    id: 5,
    name: "日本物流",
    code: "7890",
    sector: "陸運業",
    industry: "陸運",
    financials: {
      revenue: {
        "2023": 18500,
        "2024": 19800,
        "2025": 21200,
      },
      operatingProfit: {
        "2023": 1250,
        "2024": 1450,
        "2025": 1650,
      },
      netIncome: {
        "2023": 850,
        "2024": 980,
        "2025": 1120,
      },
      eps: {
        "2023": 42.5,
        "2024": 49.0,
        "2025": 56.0,
      },
      roe: {
        "2023": 5.8,
        "2024": 6.4,
        "2025": 7.0,
      },
      per: {
        "2023": 16.2,
        "2024": 15.3,
        "2025": 14.2,
      },
      pbr: {
        "2023": 0.8,
        "2024": 0.8,
        "2025": 0.7,
      },
    },
  },
  {
    id: 6,
    name: "メディカルサイエンス",
    code: "2345",
    sector: "医薬品",
    industry: "医薬品",
    financials: {
      revenue: {
        "2023": 9800,
        "2024": 11200,
        "2025": 12800,
      },
      operatingProfit: {
        "2023": 1850,
        "2024": 2250,
        "2025": 2650,
      },
      netIncome: {
        "2023": 1350,
        "2024": 1650,
        "2025": 1950,
      },
      eps: {
        "2023": 67.5,
        "2024": 82.5,
        "2025": 97.5,
      },
      roe: {
        "2023": 9.2,
        "2024": 10.5,
        "2025": 11.8,
      },
      per: {
        "2023": 22.5,
        "2024": 19.8,
        "2025": 17.2,
      },
      pbr: {
        "2023": 1.8,
        "2024": 1.6,
        "2025": 1.4,
      },
    },
  },
  {
    id: 7,
    name: "エネルギー開発",
    code: "6789",
    sector: "鉱業",
    industry: "石油・石炭",
    financials: {
      revenue: {
        "2023": 32500,
        "2024": 30800,
        "2025": 33200,
      },
      operatingProfit: {
        "2023": 3850,
        "2024": 3450,
        "2025": 3750,
      },
      netIncome: {
        "2023": 2650,
        "2024": 2350,
        "2025": 2550,
      },
      eps: {
        "2023": 132.5,
        "2024": 117.5,
        "2025": 127.5,
      },
      roe: {
        "2023": 12.8,
        "2024": 10.5,
        "2025": 11.2,
      },
      per: {
        "2023": 8.5,
        "2024": 9.8,
        "2025": 9.2,
      },
      pbr: {
        "2023": 1.0,
        "2024": 0.9,
        "2025": 0.9,
      },
    },
  },
  {
    id: 8,
    name: "デジタルソリューションズ",
    code: "0123",
    sector: "情報・通信業",
    industry: "情報サービス",
    financials: {
      revenue: {
        "2023": 8500,
        "2024": 10200,
        "2025": 12500,
      },
      operatingProfit: {
        "2023": 950,
        "2024": 1250,
        "2025": 1650,
      },
      netIncome: {
        "2023": 650,
        "2024": 850,
        "2025": 1150,
      },
      eps: {
        "2023": 32.5,
        "2024": 42.5,
        "2025": 57.5,
      },
      roe: {
        "2023": 7.5,
        "2024": 9.2,
        "2025": 11.5,
      },
      per: {
        "2023": 25.8,
        "2024": 21.2,
        "2025": 17.5,
      },
      pbr: {
        "2023": 1.7,
        "2024": 1.5,
        "2025": 1.3,
      },
    },
  },
];

// 業種のリスト
const sectors = [
  "情報・通信業",
  "卸売業",
  "電気機器",
  "建設業",
  "陸運業",
  "医薬品",
  "鉱業",
];

// 財務指標のリスト
const financialMetrics = [
  { id: "revenue", name: "売上高", unit: "百万円" },
  { id: "operatingProfit", name: "営業利益", unit: "百万円" },
  { id: "netIncome", name: "当期純利益", unit: "百万円" },
  { id: "eps", name: "EPS", unit: "円" },
  { id: "roe", name: "ROE", unit: "%" },
  { id: "per", name: "PER", unit: "倍" },
  { id: "pbr", name: "PBR", unit: "倍" },
];

// 年度のリスト
const years = createListCollection({
  items: ["2023", "2024", "2025"],
});

export default function PerformancePage() {
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedSectors, setSelectedSectors] = useState<string[]>([]);
  const [selectedMetrics, setSelectedMetrics] = useState<string[]>([
    "revenue",
    "operatingProfit",
    "netIncome",
  ]);
  const [selectedYear, setSelectedYear] = useState("2024");
  const [showFilters, setShowFilters] = useState(false);
  const [sortBy, setSortBy] = useState("name");
  const [sortOrder, setSortOrder] = useState("asc");

  // 検索とフィルタリングの適用
  const filteredCompanies = companiesData
    .filter((company) => {
      // 検索語句でフィルタリング
      if (
        searchTerm &&
        !company.name.toLowerCase().includes(searchTerm.toLowerCase()) &&
        !company.code.includes(searchTerm)
      ) {
        return false;
      }

      // 業種でフィルタリング
      if (
        selectedSectors.length > 0 &&
        !selectedSectors.includes(company.sector)
      ) {
        return false;
      }

      return true;
    })
    .sort((a, b) => {
      // 名前でソート
      if (sortBy === "name") {
        return sortOrder === "asc"
          ? a.name.localeCompare(b.name)
          : b.name.localeCompare(a.name);
      }

      // 財務指標でソート
      const metricA =
        a.financials[sortBy as keyof typeof a.financials][selectedYear];
      const metricB =
        b.financials[sortBy as keyof typeof b.financials][selectedYear];

      return sortOrder === "asc" ? metricA - metricB : metricB - metricA;
    });

  // 業種のチェックボックス状態を切り替える
  const toggleSector = (sector: string) => {
    if (selectedSectors.includes(sector)) {
      setSelectedSectors(selectedSectors.filter((s) => s !== sector));
    } else {
      setSelectedSectors([...selectedSectors, sector]);
    }
  };

  // 財務指標のチェックボックス状態を切り替える
  const toggleMetric = (metric: string) => {
    if (selectedMetrics.includes(metric)) {
      setSelectedMetrics(selectedMetrics.filter((m) => m !== metric));
    } else {
      setSelectedMetrics([...selectedMetrics, metric]);
    }
  };

  // ソート順を切り替える
  const toggleSort = (metric: string) => {
    if (sortBy === metric) {
      setSortOrder(sortOrder === "asc" ? "desc" : "asc");
    } else {
      setSortBy(metric);
      setSortOrder("desc"); // 新しい指標でソートする場合は降順から
    }
  };

  return (
    <Box minH="100vh" bg="gray.50">
      <Box as="header" bg="white" boxShadow="sm">
        <Box maxW="container.lg" mx="auto" px={4} py={4}>
          <Box display="flex" alignItems="center">
            <Link href="/" mr={4} _hover={{ textDecoration: "none" }}>
              <ArrowLeft
                size={20}
                color="#6B7280"
                style={{ transition: "color 0.2s" }}
              />
            </Link>
            <Heading as="h1" fontSize="xl" fontWeight="bold" color="gray.900">
              業績検索
            </Heading>
          </Box>
        </Box>
      </Box>

      <Container maxW="container.lg" px={4} py={6}>
        {/* 検索バー */}
        <Box mb={6} rounded="lg" bg="white" p={4} boxShadow="sm">
          <Box
            display={{ base: "flex", md: "flex" }}
            flexDirection={{ base: "column", md: "row" }}
            alignItems={{ md: "center" }}
            gap={{ base: 4, md: 4 }}
          >
            <Box position="relative" flex="1">
              <Search
                style={{
                  position: "absolute",
                  left: 12,
                  top: "50%",
                  transform: "translateY(-50%)",
                  height: 16,
                  width: 16,
                  color: "#9CA3AF",
                  pointerEvents: "none",
                }}
              />
              <Input
                placeholder="企業名・銘柄コードで検索"
                pl={10}
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </Box>
            <Box
              display="flex"
              alignItems="center"
              gap={2}
              mt={{ base: 4, md: 0 }}
            >
              <Button
                variant="outline"
                size="sm"
                display="flex"
                alignItems="center"
                onClick={() => setShowFilters(!showFilters)}
              >
                <Filter style={{ marginRight: 8, height: 16, width: 16 }} />
                <Text>フィルター</Text>
              </Button>
              <Select.Root
                collection={years}
                onValueChange={(e) => setSelectedYear(e.items[0])}
              >
                <Select.Trigger width="100px">
                  <Select.ValueText placeholder="年度" />
                </Select.Trigger>
                <Select.Content>
                  {years.items.map((year) => (
                    <Select.Item key={year} item={year}>
                      {year}年度
                    </Select.Item>
                  ))}
                </Select.Content>
              </Select.Root>
              <Menu.Root>
                <Menu.Trigger asChild>
                  <Button
                    variant="outline"
                    size="sm"
                    display="flex"
                    alignItems="center"
                  >
                    <SlidersHorizontal
                      style={{ marginRight: 8, height: 16, width: 16 }}
                    />
                    <Text>表示項目</Text>
                  </Button>
                </Menu.Trigger>
                <Menu.Content width="224px">
                  {financialMetrics.map((metric) => (
                    <Menu.Item
                      value={metric.id}
                      key={metric.id}
                      display="flex"
                      alignItems="center"
                    >
                      <Checkbox.Root
                        id={`metric-${metric.id}`}
                        checked={selectedMetrics.includes(metric.id)}
                        mr={2}
                        onCheckedChange={() => toggleMetric(metric.id)}
                      />
                      <Text>{metric.name}</Text>
                    </Menu.Item>
                  ))}
                </Menu.Content>
              </Menu.Root>
            </Box>
          </Box>

          {/* フィルターパネル */}
          <Collapsible.Root open={showFilters} mt={4}>
            <Collapsible.Content>
              <Box
                mt={4}
                rounded="md"
                borderWidth={1}
                borderColor="gray.200"
                p={4}
              >
                <Heading
                  as="h3"
                  mb={3}
                  fontWeight="medium"
                  color="gray.900"
                  fontSize="md"
                >
                  業種でフィルター
                </Heading>
                <Box
                  display="grid"
                  gridTemplateColumns={{
                    base: "repeat(2, 1fr)",
                    sm: "repeat(3, 1fr)",
                    md: "repeat(4, 1fr)",
                  }}
                  gap={2}
                >
                  {sectors.map((sector) => (
                    <Box key={sector} display="flex" alignItems="center">
                      <Checkbox.Root
                        id={`sector-${sector}`}
                        checked={selectedSectors.includes(sector)}
                        onCheckedChange={() => toggleSector(sector)}
                        mr={2}
                      />
                      <Text fontSize="sm" fontWeight="medium" color="gray.700">
                        {sector}
                      </Text>
                    </Box>
                  ))}
                </Box>
              </Box>
            </Collapsible.Content>
          </Collapsible.Root>
        </Box>

        {/* タブ切り替え */}
        <Tabs.Root defaultValue="table" mb={6}>
          <Tabs.List mb={4} display="flex" gap={2}>
            <Tabs.Trigger
              value="table"
              display="flex"
              alignItems="center"
              px={4}
              py={2}
              borderRadius="md"
              fontWeight="medium"
              fontSize="sm"
              _selected={{ bg: "gray.100", color: "emerald.600" }}
              _focus={{ boxShadow: "outline" }}
            >
              <BarChart3 style={{ marginRight: 8, height: 16, width: 16 }} />
              テーブル表示
            </Tabs.Trigger>
            <Tabs.Trigger
              value="cards"
              display="flex"
              alignItems="center"
              px={4}
              py={2}
              borderRadius="md"
              fontWeight="medium"
              fontSize="sm"
              _selected={{ bg: "gray.100", color: "emerald.600" }}
              _focus={{ boxShadow: "outline" }}
            >
              <LineChart style={{ marginRight: 8, height: 16, width: 16 }} />
              カード表示
            </Tabs.Trigger>
          </Tabs.List>

          {/* テーブル表示 */}
          <Tabs.Content value="table" mt={4}>
            <Box rounded="lg" bg="white" boxShadow="sm">
              <Box overflow="auto">
                <Table.Root width="100%" style={{ borderCollapse: "collapse" }}>
                  <Table.Header>
                    <Table.Row bg="gray.50">
                      <Table.ColumnHeader
                        cursor="pointer"
                        borderBottom="1px"
                        borderColor="gray.200"
                        p={3}
                        textAlign="left"
                        fontSize="sm"
                        fontWeight="semibold"
                        color="gray.900"
                        onClick={() => toggleSort("name")}
                      >
                        <Box display="flex" alignItems="center">
                          <Text>企業名</Text>
                          {sortBy === "name" && (
                            <ChevronDown
                              style={{
                                marginLeft: 4,
                                height: 16,
                                width: 16,
                                transform:
                                  sortOrder === "desc"
                                    ? "rotate(180deg)"
                                    : undefined,
                              }}
                            />
                          )}
                        </Box>
                      </Table.ColumnHeader>
                      <Table.ColumnHeader
                        borderBottom="1px"
                        borderColor="gray.200"
                        p={3}
                        textAlign="left"
                        fontSize="sm"
                        fontWeight="semibold"
                        color="gray.900"
                      >
                        コード
                      </Table.ColumnHeader>
                      <Table.ColumnHeader
                        borderBottom="1px"
                        borderColor="gray.200"
                        p={3}
                        textAlign="left"
                        fontSize="sm"
                        fontWeight="semibold"
                        color="gray.900"
                      >
                        業種
                      </Table.ColumnHeader>
                      {selectedMetrics.map((metricId) => {
                        const metric = financialMetrics.find(
                          (m) => m.id === metricId
                        );
                        return (
                          <Table.ColumnHeader
                            key={metricId}
                            cursor="pointer"
                            borderBottom="1px"
                            borderColor="gray.200"
                            p={3}
                            textAlign="right"
                            fontSize="sm"
                            fontWeight="semibold"
                            color="gray.900"
                            onClick={() => toggleSort(metricId)}
                          >
                            <Box
                              display="flex"
                              alignItems="center"
                              justifyContent="flex-end"
                            >
                              <Text>{metric?.name}</Text>
                              {sortBy === metricId && (
                                <ChevronDown
                                  style={{
                                    marginLeft: 4,
                                    height: 16,
                                    width: 16,
                                    transform:
                                      sortOrder === "desc"
                                        ? "rotate(180deg)"
                                        : undefined,
                                  }}
                                />
                              )}
                            </Box>
                          </Table.ColumnHeader>
                        );
                      })}
                    </Table.Row>
                  </Table.Header>
                  <Table.Body>
                    {filteredCompanies.map((company) => (
                      <Table.Row key={company.id} _hover={{ bg: "gray.50" }}>
                        <Table.Cell
                          data-label="企業名"
                          borderBottom="1px"
                          borderColor="gray.200"
                          p={3}
                          fontSize="sm"
                          fontWeight="medium"
                          color="gray.900"
                        >
                          {company.name}
                        </Table.Cell>
                        <Table.Cell
                          data-label="コード"
                          borderBottom="1px"
                          borderColor="gray.200"
                          p={3}
                          fontSize="sm"
                          color="gray.700"
                        >
                          {company.code}
                        </Table.Cell>
                        <Table.Cell
                          data-label="業種"
                          borderBottom="1px"
                          borderColor="gray.200"
                          p={3}
                          fontSize="sm"
                          color="gray.700"
                        >
                          {company.sector}
                        </Table.Cell>
                        {selectedMetrics.map((metricId) => {
                          const metric = financialMetrics.find(
                            (m) => m.id === metricId
                          );
                          const value =
                            company.financials[
                              metricId as keyof typeof company.financials
                            ][selectedYear];
                          return (
                            <Table.Cell
                              key={`${company.id}-${metricId}`}
                              data-label={metric?.name}
                              borderBottom="1px"
                              borderColor="gray.200"
                              p={3}
                              fontSize="sm"
                              color="gray.700"
                              textAlign="right"
                            >
                              {value.toLocaleString()} {metric?.unit}
                            </Table.Cell>
                          );
                        })}
                      </Table.Row>
                    ))}
                  </Table.Body>
                </Table.Root>
              </Box>
              {filteredCompanies.length === 0 && (
                <Box p={6} textAlign="center" color="gray.500">
                  検索条件に一致する企業が見つかりませんでした。
                </Box>
              )}
            </Box>
          </Tabs.Content>

          {/* カード表示 */}
          <Tabs.Content value="cards" mt={4}>
            <Box
              display="grid"
              gridTemplateColumns={{
                base: "1fr",
                md: "repeat(2, 1fr)",
                lg: "repeat(3, 1fr)",
              }}
              gap={4}
            >
              {filteredCompanies.map((company) => (
                <Card.Root key={company.id} overflow="hidden">
                  <Card.Body p={0}>
                    <Box
                      borderBottom="1px"
                      borderColor="gray.200"
                      bg="gray.50"
                      p={4}
                    >
                      <Box
                        display="flex"
                        alignItems="center"
                        justifyContent="space-between"
                      >
                        <Box>
                          <Heading
                            as="h3"
                            fontSize="lg"
                            fontWeight="semibold"
                            color="gray.900"
                          >
                            {company.name}
                          </Heading>
                          <Box display="flex" alignItems="center">
                            <Text fontSize="sm" color="gray.500">
                              {company.code}
                            </Text>
                            <Badge variant="outline" ml={2}>
                              {company.sector}
                            </Badge>
                          </Box>
                        </Box>
                      </Box>
                    </Box>
                    <Box p={4}>
                      <Heading
                        as="h4"
                        mb={2}
                        fontSize="sm"
                        fontWeight="medium"
                        color="gray.500"
                      >
                        {selectedYear}年度 業績
                      </Heading>
                      <Box>
                        {selectedMetrics.map((metricId) => {
                          const metric = financialMetrics.find(
                            (m) => m.id === metricId
                          );
                          const value =
                            company.financials[
                              metricId as keyof typeof company.financials
                            ][selectedYear];
                          return (
                            <Box
                              key={metricId}
                              display="flex"
                              alignItems="center"
                              justifyContent="space-between"
                              mb={2}
                            >
                              <Text fontSize="sm" color="gray.700">
                                {metric?.name}:
                              </Text>
                              <Text fontWeight="medium" color="gray.900">
                                {value.toLocaleString()} {metric?.unit}
                              </Text>
                            </Box>
                          );
                        })}
                      </Box>
                      <Separator my={3} />
                      <Box display="flex" justifyContent="flex-end">
                        <Button
                          variant="ghost"
                          color="emerald.600"
                          _hover={{ color: "emerald.700" }}
                        >
                          詳細を見る
                        </Button>
                      </Box>
                    </Box>
                  </Card.Body>
                </Card.Root>
              ))}
            </Box>
            {filteredCompanies.length === 0 && (
              <Box
                mt={4}
                rounded="lg"
                bg="white"
                p={6}
                textAlign="center"
                color="gray.500"
                boxShadow="sm"
              >
                検索条件に一致する企業が見つかりませんでした。
              </Box>
            )}
          </Tabs.Content>
        </Tabs.Root>

        <Box mt={6} display="flex" justifyContent="space-between">
          <Box>
            <Text fontSize="sm" color="gray.500">
              {filteredCompanies.length}件の企業が見つかりました
            </Text>
          </Box>
          <Button
            variant="outline"
            size="sm"
            display="flex"
            alignItems="center"
          >
            <Download style={{ marginRight: 8, height: 16, width: 16 }} />
            <Text>CSVダウンロード</Text>
          </Button>
        </Box>
      </Container>
    </Box>
  );
}
