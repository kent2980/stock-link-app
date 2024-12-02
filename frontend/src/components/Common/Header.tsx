import {
  Box,
  Flex,
  HStack,
  Link,
  Popover,
  PopoverArrow,
  PopoverBody,
  PopoverCloseButton,
  PopoverContent,
  PopoverHeader,
  PopoverTrigger,
  Text,
} from "@chakra-ui/react";
import React from "react";

interface HeaderProps {}

const Header: React.FC<HeaderProps> = () => {
  return (
    <Box>
      <Flex
        bg={"gray.50"}
        color={"gray.700"}
        minH={"60px"}
        py={2}
        px={4}
        borderBottom={"1px"}
        borderStyle={"solid"}
        borderColor={"gray.200"}
        align={"center"}
      >
        <Flex flex={1} align={"center"}>
          <HeaderMenu />
        </Flex>
      </Flex>
    </Box>
  );
};

export default Header;

const HeaderMenu: React.FC = () => {
  return (
    <HStack spacing={4}>
      {HEADER_ITEMS.map((item) => (
        <Box key={item.label}>
          <Popover trigger="hover" placement="bottom-start">
            <PopoverTrigger>
              <Box>
                <Link href={item.href}>
                  <Text>{item.label}</Text>
                </Link>
              </Box>
            </PopoverTrigger>
            <PopoverContent>
              <PopoverArrow />
              <PopoverCloseButton />
              <PopoverHeader>{item.label}</PopoverHeader>
              <PopoverBody>
                {item.children.map((child) => (
                  <Link key={child.label} href={child.href}>
                    <Text>{child.label}</Text>
                  </Link>
                ))}
              </PopoverBody>
            </PopoverContent>
          </Popover>
        </Box>
      ))}
    </HStack>
  );
};

interface HeaderItem {
  label: string;
  subLabel: string;
  children: Array<HeaderItem>;
  href: string;
}

const HEADER_ITEMS: Array<HeaderItem> = [
  {
    label: "Home",
    subLabel: "Dashboard",
    children: [],
    href: "/",
  },
  {
    label: "User",
    subLabel: "settings",
    children: [],
    href: "/user",
  },
  {
    label: "Settings",
    subLabel: "Settings",
    children: [],
    href: "/settings",
  },
];
