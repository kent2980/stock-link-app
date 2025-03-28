import { MenuListStore } from "@/Store/Store";
import { Flex, FlexProps } from "@chakra-ui/react";
import { useNavigate } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import { useEffect } from "react";
import { HeaderStore } from "../../Store/HeaderStore";

function Header(props: FlexProps) {
  const navigate = useNavigate();
  const handleMenuClick = (menuUrl: string | null | undefined) => {
    if (menuUrl) {
      navigate({ to: menuUrl });
    }
  };
  const { HeaderAddressItems } = useStore(HeaderStore, (state) => state); // ストアからデータを取得

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
    <Flex
      id="header"
      h={headerHeight}
      {...props}
      position="fixed"
      top={0}
      right={0}
      w={"100%"}
      p={3}
      zIndex={100}
      boxShadow="0 2px 4px rgba(0, 0, 0, 0.1)"
    >
      <Flex
        dir="row"
        justify="space-between"
        alignItems="center"
        w={{ base: "100%", md: "720px" }}
        m={"0 auto"}
        h="100%"
        px={4}
        display={{ base: "none", md: "flex" }}
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
  );
}

export default Header;
