import { Breadcrumb, Flex, FlexProps, HStack } from "@chakra-ui/react";
import { useStore } from "@tanstack/react-store";
import { useEffect } from "react";
import { HeaderStore } from "../../Store/HeaderStore";
import UserMenu from "./UserMenu";

function Header(props: FlexProps) {
  const { HeaderAddressItems } = useStore(HeaderStore, (state) => state); // ストアからデータを取得

  // ヘッダーの高さを設定
  const headerHeight = 59;
  useEffect(() => {
    HeaderStore.setState((state) => ({
      // ストアにデータをセット
      ...state,
      height: headerHeight,
    }));
  }, [headerHeight]); // ヘッダーの高さが変更された場合のみ実行

  return (
    <Flex
      h={headerHeight}
      {...props}
      position="fixed"
      top={0}
      right={0}
      w={"100%"}
      p={3}
      zIndex={100}
      bg="ui.main"
    >
      <HStack gap={3} ml={3}>
        <Breadcrumb.Root fontSize="md" color="gray.800" gap="16px">
          {HeaderAddressItems.map((item, index) => (
            <>
              <Breadcrumb.Item key={index}>
                <Breadcrumb.Link href={item.href}>{item.label}</Breadcrumb.Link>
              </Breadcrumb.Item>
              <Breadcrumb.Separator>/</Breadcrumb.Separator>
            </>
          ))}
        </Breadcrumb.Root>
      </HStack>
      <HStack gap={6} ml="auto" wrap={"wrap"}>
        <UserMenu />
      </HStack>
    </Flex>
  );
}

export default Header;
