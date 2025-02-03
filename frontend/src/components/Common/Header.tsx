import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  Flex,
  FlexProps,
  HStack,
  useColorModeValue,
} from "@chakra-ui/react";
import { useStore } from "@tanstack/react-store";
import { useEffect } from "react";
import { HeaderStore } from "../../Store/HeaderStore";

function Header(props: FlexProps) {
  const { HeaderAddressItems } = useStore(HeaderStore, (state) => state);
  const bgColor = useColorModeValue("ui.light", "ui.dark");
  const textColor = useColorModeValue("ui.dark", "ui.light");
  const boxShadow = useColorModeValue(
    "1px 1px 4px #c0bcbc",
    "1px 1px 4px #000000"
  );
  const headerHeight = 59;
  useEffect(() => {
    HeaderStore.setState((state) => ({
      ...state,
      height: headerHeight,
    }));
  }, [headerHeight]);

  return (
    <Flex
      h={headerHeight}
      {...props}
      bg={bgColor}
      color={textColor}
      position="fixed"
      top={0}
      right={0}
      zIndex={3000}
      w={"100%"}
      p={3}
      boxShadow={boxShadow}
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
    </Flex>
  );
}

export default Header;
