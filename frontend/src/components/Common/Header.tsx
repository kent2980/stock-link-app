import useAuth from "@/hooks/useAuth";
import { MenuListStore } from "@/Store/Store";
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
import React, { useEffect, useState } from "react";
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

  // スクロールイベントを監視
  useEffect(() => {
    const handleScroll = () => {
      const currentScrollY = window.scrollY;

      if (currentScrollY > lastScrollY && currentScrollY > 50) {
        setIsVisible(false); // 下にスクロールしている場合は隠す
      } else {
        setIsVisible(true); // 上にスクロールしている場合は表示
      }

      setLastScrollY(currentScrollY);
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, [lastScrollY]);

  const currentDate = format(new Date(), "yyyy-MM-dd");
  const bgColor = "#3498db";
  const menuBgColor = "#f8f9fa";
  const textColor = "#666666";
  const activeTextColor = "#333333";
  const logoutColor = "#e74c3c";

  return (
    <Box
      as="header"
      bg="gray.50"
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
      <Box bg={bgColor}>
        <Container maxW="container.xl">
          <Flex align="center" height="100%">
            <Text color="white" fontWeight="600" fontSize="14px">
              Closio
            </Text>
          </Flex>
        </Container>
      </Box>

      {/* 下段: ナビゲーションメニュー */}
      <Box bg={menuBgColor} id="secondary-header">
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
          <Flex justify="space-between">
            {/* 検索バー（左側） */}
            <Box width="200px">
              <InputGroup startElement={<BiSearch />}>
                <Input size="xs" fontSize="16px" />
              </InputGroup>
            </Box>

            {/* 日付表示（右側） */}
            <Text color={textColor} fontSize="16px">
              {currentDate}
            </Text>
          </Flex>
        </Container>
      </Box>
    </Box>
  );
};

export default Header;
