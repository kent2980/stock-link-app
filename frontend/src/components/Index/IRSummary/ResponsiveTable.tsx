import { useColorModeValue } from "@/components/ui/color-mode";
import { MenuContent, MenuItem, MenuRoot } from "@/components/ui/menu";
import {
  Badge,
  Box,
  CardBody,
  CardRoot,
  Flex,
  Heading,
  IconButton,
  Input,
  Stack,
  Table,
  Text,
  useBreakpointValue,
} from "@chakra-ui/react";
import { useState } from "react";
import { FaAdjust, FaSearch } from "react-icons/fa";
import { FiSettings } from "react-icons/fi";

// サンプルデータ
const initialData = [
  {
    id: 1,
    name: "佐藤太郎",
    status: "アクティブ",
    role: "管理者",
    lastActive: "2分前",
    project: "ダッシュボード",
  },
  {
    id: 2,
    name: "鈴木花子",
    status: "オフライン",
    role: "デザイナー",
    lastActive: "3時間前",
    project: "モバイルアプリ",
  },
  {
    id: 3,
    name: "田中誠",
    status: "アクティブ",
    role: "開発者",
    lastActive: "5分前",
    project: "APIインテグレーション",
  },
  {
    id: 4,
    name: "伊藤美咲",
    status: "ミーティング中",
    role: "マネージャー",
    lastActive: "1時間前",
    project: "データ分析",
  },
  {
    id: 5,
    name: "高橋健太",
    status: "アクティブ",
    role: "開発者",
    lastActive: "1分前",
    project: "バックエンド",
  },
  {
    id: 6,
    name: "渡辺純",
    status: "休暇中",
    role: "デザイナー",
    lastActive: "2日前",
    project: "UI/UXリデザイン",
  },
];

// ステータスに応じた色の設定
const getStatusColor = (status: any) => {
  switch (status) {
    case "アクティブ":
      return "green";
    case "オフライン":
      return "gray";
    case "ミーティング中":
      return "blue";
    case "休暇中":
      return "orange";
    default:
      return "gray";
  }
};

const ResponsiveTable = () => {
  const [data, setData] = useState(initialData);
  const [searchTerm, setSearchTerm] = useState("");

  // 検索機能
  const filteredData = data.filter(
    (item) =>
      item.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      item.role.toLowerCase().includes(searchTerm.toLowerCase()) ||
      item.project.toLowerCase().includes(searchTerm.toLowerCase())
  );

  // カラー設定
  const bgColor = useColorModeValue("white", "gray.800");
  const textColor = useColorModeValue("gray.800", "white");
  const borderColor = useColorModeValue("gray.200", "gray.700");
  const hoverBg = useColorModeValue("gray.50", "gray.700");

  // レスポンシブ設定
  const isMobile = useBreakpointValue({ base: true, md: false });

  return (
    <Box p={4}>
      <CardRoot boxShadow="lg" borderRadius="xl" overflow="hidden">
        <CardBody p={0}>
          <Flex
            p={4}
            justifyContent="space-between"
            alignItems="center"
            borderBottom="1px"
            borderColor={borderColor}
          >
            <Heading size="md">チームメンバー</Heading>
            <Flex>
              <Box position="relative" mr={2}>
                <Input
                  placeholder="検索..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  size="sm"
                  borderRadius="full"
                  pl={8}
                  width="200px"
                />
                <Box position="absolute" left={3} top="9px">
                  <FaSearch color="gray.400" size={3} />
                </Box>
              </Box>
              <MenuRoot>
                <IconButton
                  as={IconButton}
                  variant="ghost"
                  size="sm"
                  borderRadius="full"
                >
                  <FiSettings />
                </IconButton>
                <MenuContent>
                  <MenuItem value="">列の表示設定</MenuItem>
                  <MenuItem value="">エクスポート</MenuItem>
                  <MenuItem value="">フィルター設定</MenuItem>
                </MenuContent>
              </MenuRoot>
            </Flex>
          </Flex>

          {isMobile ? (
            // モバイル表示
            <Box>
              {filteredData.map((item) => (
                <Box
                  key={item.id}
                  p={4}
                  borderBottom="1px"
                  borderColor={borderColor}
                  _hover={{ bg: hoverBg }}
                  transition="background 0.2s"
                >
                  <Flex justify="space-between" mb={2}>
                    <Text fontWeight="bold">{item.name}</Text>
                    <Badge
                      colorScheme={getStatusColor(item.status)}
                      borderRadius="full"
                      px={2}
                    >
                      {item.status}
                    </Badge>
                  </Flex>
                  <Stack gap={1} fontSize="sm" color="gray.600">
                    <Flex>
                      <Text width="80px" fontWeight="medium">
                        役割:
                      </Text>
                      <Text>{item.role}</Text>
                    </Flex>
                    <Flex>
                      <Text width="80px" fontWeight="medium">
                        プロジェクト:
                      </Text>
                      <Text>{item.project}</Text>
                    </Flex>
                    <Flex>
                      <Text width="80px" fontWeight="medium">
                        最終活動:
                      </Text>
                      <Text>{item.lastActive}</Text>
                    </Flex>
                  </Stack>
                </Box>
              ))}
            </Box>
          ) : (
            // デスクトップ表示
            <Table.Root striped>
              <Table.Header>
                <Table.Row>
                  <Table.ColumnHeader borderColor={borderColor}>
                    名前
                  </Table.ColumnHeader>
                  <Table.ColumnHeader borderColor={borderColor}>
                    ステータス
                  </Table.ColumnHeader>
                  <Table.ColumnHeader borderColor={borderColor}>
                    役割
                  </Table.ColumnHeader>
                  <Table.ColumnHeader borderColor={borderColor}>
                    最終活動
                  </Table.ColumnHeader>
                  <Table.ColumnHeader borderColor={borderColor}>
                    プロジェクト
                  </Table.ColumnHeader>
                  <Table.ColumnHeader
                    borderColor={borderColor}
                  ></Table.ColumnHeader>
                </Table.Row>
              </Table.Header>
              <Table.Body>
                {filteredData.map((item) => (
                  <Table.Row
                    key={item.id}
                    _hover={{ bg: hoverBg }}
                    transition="background 0.2s"
                  >
                    <Table.Cell borderColor={borderColor}>
                      <Flex align="center">
                        <Box
                          w="32px"
                          h="32px"
                          borderRadius="full"
                          bg="blue.500"
                          color="white"
                          display="flex"
                          alignItems="center"
                          justifyContent="center"
                          fontWeight="bold"
                          mr={3}
                          fontSize="xs"
                        >
                          {item.name.charAt(0)}
                        </Box>
                        <Text fontWeight="medium">{item.name}</Text>
                      </Flex>
                    </Table.Cell>
                    <Table.Cell borderColor={borderColor}>
                      <Badge
                        colorScheme={getStatusColor(item.status)}
                        borderRadius="full"
                        px={2}
                      >
                        {item.status}
                      </Badge>
                    </Table.Cell>
                    <Table.Cell borderColor={borderColor}>
                      {item.role}
                    </Table.Cell>
                    <Table.Cell borderColor={borderColor}>
                      {item.lastActive}
                    </Table.Cell>
                    <Table.Cell borderColor={borderColor}>
                      {item.project}
                    </Table.Cell>
                    <Table.Cell borderColor={borderColor}>
                      <MenuRoot>
                        <IconButton as={IconButton} variant="ghost" size="sm">
                          <FaAdjust />
                        </IconButton>
                        <MenuContent>
                          <MenuItem value="">詳細を見る</MenuItem>
                          <MenuItem value="">編集</MenuItem>
                          <MenuItem value="">削除</MenuItem>
                        </MenuContent>
                      </MenuRoot>
                    </Table.Cell>
                  </Table.Row>
                ))}
              </Table.Body>
            </Table.Root>
          )}

          <Flex
            p={4}
            justifyContent="space-between"
            borderTop="1px"
            borderColor={borderColor}
            alignItems="center"
          >
            <Text fontSize="sm" color="gray.500">
              {filteredData.length}件 / {data.length}件 表示
            </Text>
            <Flex>
              <Box fontSize="sm">1 / 1 ページ</Box>
            </Flex>
          </Flex>
        </CardBody>
      </CardRoot>
    </Box>
  );
};

export default ResponsiveTable;
