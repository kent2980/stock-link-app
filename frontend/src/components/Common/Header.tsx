import { MenuListStore } from "@/Store/Store";
import { Box, Center, Flex, FlexProps, HStack } from "@chakra-ui/react";
import { useNavigate } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import React from "react";

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

  const { menuList } = useStore(MenuListStore, (state) => state); // ストアからデータを取得
  return (
    <>
      <Flex
        id="header"
        h={headerHeight}
        {...props}
        w="100vw"
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
