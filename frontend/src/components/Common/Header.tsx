import { MenuListStore } from "@/Store/Store";
import {
  Box,
  Center,
  Flex,
  FlexProps,
  Heading,
  HStack,
} from "@chakra-ui/react";
import { useNavigate } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import React, { useEffect } from "react";
import { HeaderStore } from "../../Store/HeaderStore";

const Header: React.FC<FlexProps> = ({ ...props }) => {
  const navigate = useNavigate();
  const handleMenuClick = (menuUrl: string | null | undefined) => {
    console.log("menuUrl", menuUrl);
    if (menuUrl) {
      navigate({ to: menuUrl });
    }
  };

  // ヘッダーの高さを設定
  const headerHeight = 12;
  useEffect(() => {
    HeaderStore.setState((state) => ({
      // ストアにデータをセット
      ...state,
      height: headerHeight,
    }));
  }, [headerHeight]); // ヘッダーの高さが変更された場合のみ実行

  const { menuList } = useStore(MenuListStore, (state) => state); // ストアからデータを取得
  return (
    <>
      {/* モバイル */}
      <Flex
        id="header"
        {...props}
        w={"100%"}
        p={3}
        boxShadow="md"
        bg="linear-gradient(to right, #ffffff, #fefefe)"
        borderBottom="1px solid #eaeaea"
        display={{ base: "block", md: "none" }}
        position={"fixed"}
        top={0}
        zIndex={1000}
      >
        <Center>
          <Heading size="md">決 算 短 信</Heading>
        </Center>
      </Flex>
      {/* デスクトップ */}
      <Flex
        id="header"
        h={headerHeight}
        {...props}
        w="100vw" // 横幅を 1024px に変更
        display={{ base: "none", md: "block" }}
        zIndex={1000}
        mx="auto"
        p={3}
        color="gray.400"
        _hover={{ bg: "rgba(167, 167, 167, 0.1)" }}
      >
        <Center>
          <HStack gap={10}>
            {menuList.map((item, index) => (
              <Box key={index} _hover={{ color: "white" }}>
                {item.menuLabel}
              </Box>
            ))}
          </HStack>
        </Center>
      </Flex>
    </>
  );
};

export default Header;
