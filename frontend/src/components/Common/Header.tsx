import useAuth from "@/hooks/useAuth";
import { MenuListStore } from "@/Store/Store";
import { Box, BoxProps, Flex, HStack } from "@chakra-ui/react";
import { useNavigate } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import React from "react";

const Header: React.FC<BoxProps> = ({ ...props }) => {
  const { logout } = useAuth();
  const handleLogout = () => {
    logout();
  };

  const navigate = useNavigate();
  const handleMenuClick = (menuUrl: string | null | undefined) => {
    console.log("menuUrl", menuUrl);
    if (menuUrl) {
      navigate({ to: menuUrl });
    }
  };

  // ヘッダーの高さを設定
  const headerHeight = 12;

  const { menuList } = useStore(MenuListStore, (state) => state); // ストアからデータを取得
  return (
    <Box
      color="gray.400"
      _hover={{ bg: "rgba(167, 167, 167, 0.1)" }}
      bg="gray.50"
      borderBottom="solid 1px"
      borderColor="gray.200"
      position="fixed"
      top={0}
      left={0}
      id="header"
      w="100vw"
      zIndex={1000}
      h={headerHeight}
      {...props}
    >
      <Flex mx="auto" p={3} justifyContent="space-between" px={14}>
        <HStack gap={10}>
          {menuList.map((item, index) => (
            <Box
              key={index}
              _hover={{ color: "white" }}
              onClick={() => handleMenuClick(item.menuUrl)}
            >
              {item.menuLabel}
            </Box>
          ))}
        </HStack>
        <Box
          cursor="pointer"
          color="gray.500"
          _hover={{ color: "red.500" }}
          onClick={handleLogout} // ログアウト処理を呼び出す
        >
          Logout
        </Box>
      </Flex>
    </Box>
  );
};

export default Header;
