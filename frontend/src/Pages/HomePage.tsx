import { DashboardInfo } from "@/components/Home/dashboard-info";
import {
  Box,
  Link as ChakraLink,
  Flex,
  Grid,
  Heading,
  Stack,
  Text,
} from "@chakra-ui/react";
import { useNavigate } from "@tanstack/react-router";
import {
  BarChart3,
  BookOpen,
  FileText,
  LineChart,
  Newspaper,
  PieChart,
  Search,
  Settings,
  TrendingUp,
} from "lucide-react";

export default function HomePage() {
  const navigate = useNavigate({ from: "/" });

  const handleClick = (url: string) => {
    navigate({ to: url });
  };

  const menuItems = [
    {
      title: "適時開示速報",
      description: "最新の企業情報をリアルタイムで確認",
      icon: <Newspaper className="h-8 w-8" color="#059669" />,
      href: "/disclosure",
    },
    {
      title: "業績検索",
      description: "企業の業績データを検索・比較",
      icon: <Search className="h-8 w-8" color="#059669" />,
      href: "/performance",
    },
    {
      title: "銘柄辞書",
      description: "株式銘柄の詳細情報を確認",
      icon: <BookOpen className="h-8 w-8" color="#059669" />,
      href: "/stocks",
    },
    {
      title: "財務諸表",
      description: "企業の財務諸表を閲覧・分析",
      icon: <FileText className="h-8 w-8" color="#059669" />,
      href: "/financial-statements",
    },
    {
      title: "財務検索",
      description: "財務指標による企業検索",
      icon: <BarChart3 className="h-8 w-8" color="#059669" />,
      href: "/financial-search",
    },
    {
      title: "ポートフォリオ管理",
      description: "保有株式の管理と分析",
      icon: <PieChart className="h-8 w-8" color="#059669" />,
      href: "/portfolio",
    },
    {
      title: "市場ニュース",
      description: "株式市場の最新ニュースをチェック",
      icon: <TrendingUp className="h-8 w-8" color="#059669" />,
      href: "/market-news",
    },
    {
      title: "チャート分析",
      description: "株価チャートの詳細分析",
      icon: <LineChart className="h-8 w-8" color="#059669" />,
      href: "/chart-analysis",
    },
    {
      title: "設定",
      description: "アプリの設定とカスタマイズ",
      icon: <Settings className="h-8 w-8" color="#059669" />,
      href: "/settings",
    },
  ];

  return (
    <Box minH="100vh" bg="gray.50">
      <Flex
        direction="column"
        gap={4}
        as="main"
        maxW="container.lg"
        py={8}
        px={0}
      >
        <DashboardInfo />
        <Grid
          templateColumns={{
            base: "repeat(1, 1fr)",
            md: "repeat(2, 1fr)",
            lg: "repeat(3, 1fr)",
          }}
          gap={3}
        >
          {menuItems.map((item, index) => (
            <ChakraLink
              href={item.href}
              key={index}
              _hover={{ textDecoration: "none" }}
              onClick={(e) => {
                e.preventDefault();
                handleClick(item.href);
              }}
            >
              <Box
                bg="white"
                borderWidth="1px"
                borderColor="gray.200"
                borderRadius="lg"
                transition="all 0.2s"
                _hover={{
                  boxShadow: "md",
                  borderColor: "emerald.300",
                }}
                h="full"
                w="full"
              >
                <Stack align="center" p={6} textAlign="center" gap={4}>
                  <Flex
                    mb={2}
                    rounded="full"
                    bg="emerald.50"
                    p={3}
                    align="center"
                    justify="center"
                  >
                    {item.icon}
                  </Flex>
                  <Heading as="h2" size="md" color="gray.900">
                    {item.title}
                  </Heading>
                  <Text fontSize="sm" color="gray.500">
                    {item.description}
                  </Text>
                </Stack>
              </Box>
            </ChakraLink>
          ))}
        </Grid>
      </Flex>
    </Box>
  );
}
