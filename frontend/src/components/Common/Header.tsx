import {
  Box,
  Flex,
  FlexProps,
  HStack,
  Image,
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
import useAuth from "../../hooks/useAuth";

const Header: React.FC<FlexProps> = (props) => {
  const { logout } = useAuth();

  function handleLogout() {
    logout();
  }

  return (
    <Flex
      {...props}
      position="fixed"
      top="0"
      left="0"
      right="0"
      bg={"gray.50"}
      color={"gray.700"}
      py={2}
      pr={4}
      borderBottom={"1px"}
      borderStyle={"solid"}
      borderColor={"gray.200"}
      align={"center"}
    >
      <Flex flex={1} align={"center"}>
        <Link href="/">
          <Image src="/assets/images/app-logo.png" alt="logo" boxSize="80px" />
        </Link>
        <HeaderMenu />
      </Flex>
      <Flex>
        <Text onClick={handleLogout}>LogOut</Text>
      </Flex>
    </Flex>
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
