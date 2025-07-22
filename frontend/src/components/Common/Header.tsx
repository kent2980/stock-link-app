"use client";

import {
  Badge,
  Box,
  BoxProps,
  Menu as ChakraMenu,
  Drawer,
  DrawerBody,
  Flex,
  Heading,
  HStack,
  IconButton,
  Input,
  InputGroup,
  Link,
  VStack,
} from "@chakra-ui/react";
import {
  BarChart3,
  Bell,
  BookOpen,
  FileText,
  LineChart,
  Newspaper,
  PieChart,
  Search,
  Settings,
  TrendingUp,
  User,
  X,
} from "lucide-react";
import { useState } from "react";
import CustomDrawer from "./CustomDrawer";

const mainNavItems = [
  {
    title: "適時開示速報",
    href: "/disclosure",
    icon: <Newspaper size={20} />,
  },
  {
    title: "業績検索",
    href: "/performance",
    icon: <Search size={20} />,
  },
  {
    title: "銘柄辞書",
    href: "/stocks",
    icon: <BookOpen size={20} />,
  },
  {
    title: "財務諸表",
    href: "/financial-statements",
    icon: <FileText size={20} />,
  },
  {
    title: "財務検索",
    href: "/financial-search",
    icon: <BarChart3 size={20} />,
  },
  {
    title: "ポートフォリオ管理",
    href: "/portfolio",
    icon: <PieChart size={20} />,
  },
  {
    title: "市場ニュース",
    href: "/market-news",
    icon: <TrendingUp size={20} />,
  },
  {
    title: "チャート分析",
    href: "/chart-analysis",
    icon: <LineChart size={20} />,
  },
];

export const Header: React.FC<BoxProps> = (props) => {
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [open, setOpen] = useState(false);
  return (
    <Box
      as="header"
      {...props}
      pt={2}
      borderBottom="solid 0.5px"
      borderColor="gray.600"
    >
      <Flex maxW="container.xl" mx="auto" align="center" px={4}>
        {/* Drawer for mobile */}
        <Box display={{ base: "block", md: "none" }} mr={2}>
          <CustomDrawer open={open} setOpen={setOpen} />
          <Drawer.Root>
            <Drawer.Content maxW={{ base: "300px", sm: "400px" }}>
              <Drawer.Header>
                <Link href="/" style={{ textDecoration: "none" }}>
                  <Flex
                    align="center"
                    gap={2}
                    color="green.600"
                    fontWeight="bold"
                    fontSize="lg"
                  >
                    <Box as="span" fontSize={24} color="#059669">
                      株式投資総合管理
                    </Box>
                  </Flex>
                </Link>
              </Drawer.Header>
              <DrawerBody>
                <VStack align="stretch" gap={2} py={6}>
                  {mainNavItems.map((item) => (
                    <Link
                      key={item.href}
                      href={item.href}
                      style={{ textDecoration: "none" }}
                    >
                      <Flex
                        align="center"
                        gap={3}
                        px={3}
                        py={2}
                        borderRadius="md"
                        fontSize="sm"
                        fontWeight="medium"
                        bg="green.50"
                        color="green.200"
                        _hover={{
                          bg: "gray.100",
                          color: "gray.900",
                          textDecoration: "none",
                        }}
                      >
                        {item.icon}
                        <Box as="span">{item.title}</Box>
                      </Flex>
                    </Link>
                  ))}
                  <Link href="/settings" style={{ textDecoration: "none" }}>
                    <Flex
                      align="center"
                      gap={3}
                      px={3}
                      py={2}
                      borderRadius="md"
                      fontSize="sm"
                      fontWeight="medium"
                      bg="green.50"
                      color="green.300"
                      _hover={{
                        bg: "gray.100",
                        color: "gray.900",
                        textDecoration: "none",
                      }}
                    >
                      <Settings size={20} />
                      <Box as="span">設定</Box>
                    </Flex>
                  </Link>
                </VStack>
              </DrawerBody>
            </Drawer.Content>
          </Drawer.Root>
        </Box>

        {/* Logo */}
        <Link href="/" style={{ textDecoration: "none" }}>
          <Flex align="center" mr={6}>
            <TrendingUp size={24} color="#059669" />
            <Box
              as="span"
              display={{ base: "none", md: "inline-block" }}
              fontWeight="bold"
              fontSize={16}
              color="green.300"
              ml={2}
            >
              株式投資総合管理
            </Box>
          </Flex>
        </Link>

        {/* ページタイトル */}
        <Flex align="center" mr="auto">
          <Heading as="h1" size="md" fontWeight="semibold">
            {/* ここにページタイトルを挿入 */}トップページ
          </Heading>
        </Flex>

        {/* Main nav for desktop */}
        <HStack gap={1} display={{ base: "none", md: "flex" }}>
          {mainNavItems.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              style={{ textDecoration: "none" }}
              fontWeight="medium"
              fontSize="sm"
              px={3}
              h={10}
            >
              {item.title}
            </Link>
          ))}
        </HStack>

        {/* Right side actions */}
        <HStack gap={2} ml={4}>
          {isSearchOpen ? (
            <InputGroup
              maxW="sm"
              w="full"
              endElement={
                <IconButton
                  aria-label="検索を閉じる"
                  variant="ghost"
                  size="sm"
                  onClick={() => setIsSearchOpen(false)}
                >
                  <X size={16} />
                </IconButton>
              }
            >
              <Input
                type="search"
                placeholder="銘柄名・コードで検索..."
                pr="2.5rem"
                autoFocus
                onBlur={() => setIsSearchOpen(false)}
                bg="white"
              />
            </InputGroup>
          ) : (
            <IconButton
              aria-label="検索"
              variant="ghost"
              size="md"
              onClick={() => setIsSearchOpen(true)}
            >
              <Search size={20} color="#ffffff" />
            </IconButton>
          )}

          <Box position="relative">
            <IconButton aria-label="通知" variant="ghost" size="md">
              <Bell size={20} color="#ffffff" />
            </IconButton>
            <Badge
              position="absolute"
              top="-1"
              right="-1"
              rounded="full"
              px={2}
              py={1}
              fontSize="xs"
              colorScheme="red"
            >
              3
            </Badge>
          </Box>

          <ChakraMenu.Root>
            <IconButton
              variant="ghost"
              size="md"
              rounded="full"
              aria-label="ユーザーメニュー"
            >
              <User size={20} color="#ffffff" />
            </IconButton>
            <ChakraMenu.Positioner>
              <ChakraMenu.Content title="マイアカウント">
                <ChakraMenu.Item value="/profile">
                  {<User size={16} />}プロフィール
                </ChakraMenu.Item>
                <ChakraMenu.Item value="/notifications">
                  {<Bell size={16} />}通知
                </ChakraMenu.Item>
                <ChakraMenu.Item value="/settings">
                  {<Settings size={16} />}設定
                </ChakraMenu.Item>
              </ChakraMenu.Content>
              <ChakraMenu.Item value="/logout">
                {<X size={16} />}ログアウト
              </ChakraMenu.Item>
            </ChakraMenu.Positioner>
          </ChakraMenu.Root>
        </HStack>
      </Flex>
    </Box>
  );
};
