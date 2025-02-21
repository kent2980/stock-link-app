import {
  Accordion,
  AccordionButton,
  AccordionIcon,
  AccordionItem,
  AccordionPanel,
  Box,
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  Drawer,
  DrawerBody,
  DrawerContent,
  DrawerFooter,
  DrawerHeader,
  DrawerOverlay,
  Flex,
  FlexProps,
  HStack,
  IconButton,
  List,
  ListItem,
  useColorModeValue,
  useDisclosure,
} from "@chakra-ui/react";
import { Link } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import { useEffect } from "react";
import { GrMenu } from "react-icons/gr";
import { HeaderStore } from "../../Store/HeaderStore";
import UserMenu from "./UserMenu";

function Header(props: FlexProps) {
  const { HeaderAddressItems } = useStore(HeaderStore, (state) => state); // ストアからデータを取得

  // ダークモードの設定
  const bgColor = useColorModeValue("ui.light", "ui.dark");
  const textColor = useColorModeValue("ui.dark", "ui.light");
  const boxShadow = useColorModeValue(
    "1px 1px 4px #c0bcbc",
    "1px 1px 4px #000000"
  );

  // ヘッダーの高さを設定
  const headerHeight = 59;
  useEffect(() => {
    HeaderStore.setState((state) => ({
      // ストアにデータをセット
      ...state,
      height: headerHeight,
    }));
  }, [headerHeight]); // ヘッダーの高さが変更された場合のみ実行

  const { isOpen, onOpen, onClose } = useDisclosure(); // メニューの開閉状態を管理

  return (
    <Flex
      h={headerHeight}
      {...props}
      bg={bgColor}
      color={textColor}
      position="fixed"
      top={0}
      right={0}
      w={"100%"}
      p={3}
      boxShadow={boxShadow}
      zIndex={100}
    >
      <HStack spacing={3} ml={3}>
        <Breadcrumb separator=">" fontSize="md" color="gray.800" spacing="16px">
          {HeaderAddressItems.map((item, index) => (
            <BreadcrumbItem key={index}>
              <BreadcrumbLink href={item.href}>{item.label}</BreadcrumbLink>
            </BreadcrumbItem>
          ))}
        </Breadcrumb>
      </HStack>
      <HStack spacing={6} ml="auto">
        <Box zIndex={120}>
          <IconButton aria-label="Menu" icon={<GrMenu />} onClick={onOpen} />
          <Drawer isOpen={isOpen} placement="left" onClose={onClose}>
            <DrawerOverlay />
            <DrawerContent bg="ui.dark">
              <DrawerHeader borderBottomWidth="1px" fontSize={14}>
                デザインマップ
              </DrawerHeader>
              <DrawerBody>
                <DesignMapAccordion />
              </DrawerBody>
              <DrawerFooter></DrawerFooter>
            </DrawerContent>
          </Drawer>
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
      params: { code: "7605" },
    },
  ];
  const items = [
    { title: "固定ページ", pages: [{ title: "トップページ", path: "/" }] },
    { title: "決算サマリーページ", pages: summaryPages },
  ];
  return (
    <Accordion allowToggle>
      {items.map((item, index) => (
        <AccordionItem key={index}>
          <h2>
            <AccordionButton>
              <Box as="span" flex={1} textAlign={"left"} fontSize={14}>
                {item.title}
              </Box>
              <AccordionIcon />
            </AccordionButton>
          </h2>
          <AccordionPanel pb={4}>
            <List fontSize={12.5}>
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
            </List>
          </AccordionPanel>
        </AccordionItem>
      ))}
    </Accordion>
  );
}

export default Header;
