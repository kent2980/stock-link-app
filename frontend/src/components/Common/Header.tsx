import { MenuListStore } from "@/Store/Store";
import { Center, Flex, FlexProps, Heading } from "@chakra-ui/react";
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
        <Center color="gray.600">
          <Heading size="md">決 算 短 信</Heading>
        </Center>
      </Flex>
      {/* デスクトップ */}
      <Flex
        id="header"
        h={headerHeight}
        {...props}
        w={"100%"}
        p={3}
        boxShadow="md"
        bg="linear-gradient(to right, #ffffff, #fefefe)"
        borderBottom="1px solid #eaeaea"
        display={{ base: "none", md: "block" }}
        zIndex={1000}
      >
        <Flex
          dir="row"
          justify="space-between"
          alignItems="center"
          w={{ base: "100%", md: "720px" }}
          m={"0 auto"}
          h="100%"
          px={4}
        >
          {menuList.map((item, index) => (
            <Flex
              key={index}
              as="a"
              fontSize="lg"
              fontWeight="bold"
              _hover={{ textDecoration: "underline" }}
              _active={{ color: "ui.secondary" }}
              px={2}
              py={1}
              _focus={{ boxShadow: "outline" }}
              onClick={() => handleMenuClick(item.menuUrl)}
            >
              {item.menuLabel} {/* ここにメニューアイテムを追加 */}
            </Flex>
          ))}
        </Flex>
      </Flex>
    </>
  );
};

export default Header;
