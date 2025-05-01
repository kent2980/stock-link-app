import useAuth from "@/hooks/useAuth";
import { MenuListStore } from "@/Store/Store";
import { Box, BoxProps, Flex, HStack } from "@chakra-ui/react";
import { useNavigate } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import React, { useEffect, useState } from "react";

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

      // スクロール方向に応じて即座に表示・非表示を切り替える
      setIsVisible(currentScrollY <= lastScrollY);

      setLastScrollY(currentScrollY);
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, [lastScrollY]);

  return (
    <Box
      color="gray.400"
      bg="gray.50"
      borderBottom="solid 1px"
      borderColor="gray.200"
      position="fixed"
      top={{ base: isVisible ? 0 : `-${headerHeight * 4}px`, md: 0 }} // 隠すときは上に移動
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
