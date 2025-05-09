import useAuth from "@/hooks/useAuth";
import { HeaderStore, MenuListStore } from "@/Store/Store";
import {
  Box,
  BoxProps,
  Container,
  Flex,
  HStack,
  Input,
  InputGroup,
  Text,
} from "@chakra-ui/react";
import { useNavigate } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import { format } from "date-fns";
import React, { useState } from "react";
import { BiSearch } from "react-icons/bi";

interface HeaderProps extends BoxProps {
  headerHeight?: number; // ヘッダーの高さを指定するプロパティ
}

const Header: React.FC<HeaderProps> = ({ headerHeight = 12, ...props }) => {
  const { logout } = useAuth();
  const navigate = useNavigate();
  const { menuList } = useStore(MenuListStore, (state) => state); // ストアからデータを取得

  const [isVisible, setIsVisible] = useState(true); // ヘッダーの表示状態
  const [lastScrollY, setLastScrollY] = useState(0); // 最後のスクロール位置

  const handleLogout = () => {
    logout();
  };

  const handleMenuClick = (menuUrl: string | null | undefined) => {
    if (menuUrl) {
      navigate({ to: menuUrl });
    }
  };

  // ストアからPublicデータを取得
  const { SelectDateStr, CurrentCategory } = useStore(
    HeaderStore,
    (state) => state
  );

  const currentItem = () => {
    if (CurrentCategory) {
      return CurrentCategory;
    } else {
      if (SelectDateStr) {
        const date = new Date(SelectDateStr);
        return format(date, "yyyy.MM.dd");
      } else {
        return "";
      }
    }
  };
  const textColor = "#666666";
  const activeTextColor = "#333333";
  const logoutColor = "#e74c3c";

  return (
    <Box
      as="header"
      bg="white"
      position="fixed"
      boxShadow="xs" // BoxShadowを薄く変更
      top={{ base: isVisible ? 0 : `-${headerHeight * 4}px`, md: 0 }} // 隠すときは上に移動
      left={0}
      id="header"
      w="100vw"
      zIndex={1000}
      h={headerHeight}
      {...props}
    >
      {/* 上段: メインヘッダー */}
      <Box id="main-header">
        <Container maxW="container.xl">
          <Flex align="center" height="100%">
            <Text fontWeight="600" fontSize="14px">
              Closio
            </Text>
          </Flex>
        </Container>
      </Box>

      {/* 下段: ナビゲーションメニュー */}
      <Box bg="white" id="secondary-header">
        <Container maxW="container.xl">
          {/* 1段目: ナビゲーションメニュー */}
          <Flex justify="space-between" py={2}>
            <HStack gap={8}>
              {menuList.map((item, index) => (
                <Text
                  key={index}
                  fontWeight="500"
                  color={index === 0 ? activeTextColor : textColor}
                  cursor="pointer"
                  onClick={() => handleMenuClick(item.menuUrl)}
                >
                  {item.menuLabel}
                </Text>
              ))}
            </HStack>

            <Flex align="center">
              <Text
                color={logoutColor}
                mr={4}
                cursor="pointer"
                onClick={handleLogout}
              >
                ログアウト
              </Text>
            </Flex>
          </Flex>

          {/* 2段目: 検索バーと日付 */}
          <Flex gap={4}>
            {/* 検索バー（左側） */}
            <Box width="250px">
              <InputGroup startElement={<BiSearch />}>
                <Input size="sm" fontSize="16px" h="30px" />
              </InputGroup>
            </Box>

            {/* 日付表示（右側） */}
            <Box
              w={{ base: "calc(100vw - 250px)", md: "200px" }}
              px={4}
              borderRadius="md"
              borderBottom="1px solid"
              borderColor="gray.200"
              h="30px"
            >
              <Flex align="center" justify="center" h="100%">
                <Text color={textColor} fontSize="14px" fontWeight="bold">
                  {currentItem()}
                </Text>
              </Flex>
            </Box>
          </Flex>
        </Container>
      </Box>
    </Box>
  );
};

export default Header;
