import {
  DrawerBackdrop,
  DrawerBody,
  DrawerContent,
  DrawerFooter,
  DrawerHeader,
  DrawerRoot,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer";
import {
  AccordionItem,
  AccordionItemContent,
  AccordionItemTrigger,
  AccordionRoot,
  Box,
  Breadcrumb,
  Button,
  Flex,
  FlexProps,
  HStack,
  ListItem,
  ListRoot,
} from "@chakra-ui/react";
import { Link } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import { useEffect, useState } from "react";
import { GrMenu } from "react-icons/gr";
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

  const [open, setOpen] = useState(false);

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
        <Box zIndex={120}>
          <DrawerRoot
            placement="start"
            open={open}
            onOpenChange={(e: any) => setOpen(e.open)}
          >
            <DrawerBackdrop />
            <DrawerTrigger>
              <Button>
                <GrMenu />
              </Button>
            </DrawerTrigger>
            <DrawerContent>
              <DrawerHeader borderBottomWidth="1px" fontSize={14}>
                <DrawerTitle>デザインマップ</DrawerTitle>
              </DrawerHeader>
              <DrawerBody>
                <DesignMapAccordion />
              </DrawerBody>
              <DrawerFooter></DrawerFooter>
            </DrawerContent>
          </DrawerRoot>
        </Box>
        <UserMenu />
      </HStack>
    </Flex>
  );
}

type CustomItemProps = {
  title: string;
  path: string;
  params?: any | undefined;
};

function DesignMapAccordion() {
  const summaryPages: CustomItemProps[] = [
    { title: "エラーページ", path: "/summary" },
    {
      title: "共通コンテンツ",
      path: "/summary/$code/layout/stockInfo",
      params: { code: "1758" },
    },
  ];
  const items = [
    { title: "固定ページ", pages: [{ title: "トップページ", path: "/" }] },
    { title: "決算サマリーページ", pages: summaryPages },
  ];
  return (
    <AccordionRoot>
      {items.map((item, index) => (
        <AccordionItem key={index} value={item.title}>
          <AccordionItemTrigger>
            <h2>
              <Box as="span" flex={1} textAlign={"left"} fontSize={14}>
                {item.title}
              </Box>
            </h2>
          </AccordionItemTrigger>
          <AccordionItemContent pb={4}>
            <ListRoot fontSize={12.5}>
              {item.pages.map((page, index) => (
                <ListItem
                  key={index}
                  ml={4}
                  p={1}
                  _hover={{ bg: "gray.100", color: "ui.dark" }}
                >
                  <Link to={page.path} params={page.params}>
                    {page.title}
                  </Link>
                </ListItem>
              ))}
            </ListRoot>
          </AccordionItemContent>
        </AccordionItem>
      ))}
    </AccordionRoot>
  );
}

export default Header;
