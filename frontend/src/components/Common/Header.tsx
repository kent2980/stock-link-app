import useAuth from "@/hooks/useAuth";
import { HeaderStore, MenuListStore } from "@/Store/Store";
import { Box, BoxProps, Container, Flex, HStack, Text } from "@chakra-ui/react";
import { useNavigate } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import { format } from "date-fns";
import React from "react";

interface HeaderProps extends BoxProps {
  headerHeight?: number | string; // ヘッダーの高さを指定するプロパティ
}

const Header: React.FC<HeaderProps> = ({ headerHeight = 12, ...props }) => {
  const { logout } = useAuth();
  const navigate = useNavigate();
  const { menuList } = useStore(MenuListStore, (state) => state); // ストアからデータを取得

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
      top={0} // 隠すときは上に移動
      left={0}
      id="header"
      w="100vw"
      zIndex={1000}
      h={headerHeight}
      {...props}
    >
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
        </Container>
      </Box>
    </Box>
  );
};

export default Header;
