import { Box, Flex, Icon, Separator, Text } from "@chakra-ui/react";
import { useQueryClient } from "@tanstack/react-query";
import { Link as RouterLink } from "@tanstack/react-router";
import { FiHome, FiUsers } from "react-icons/fi";
import type { IconType } from "react-icons/lib";

import type { UserPublic } from "@/client";
import { GrAction, GrCube, GrNew } from "react-icons/gr";

const items = [
  { icon: FiHome, title: "Home", path: "/" },
  { icon: GrNew, title: "IR Store", path: "/store" },
  { icon: GrCube, title: "銘柄別", path: "/settings" },
  { icon: GrAction, title: "仮想化", path: "/virtual" },
  { icon: GrAction, title: "responsive", path: "/Responsive" },
];

interface SidebarItemsProps {
  onClose?: () => void;
}

interface Item {
  icon: IconType;
  title: string;
  path: string;
}

const SidebarItems = ({ onClose }: SidebarItemsProps) => {
  const queryClient = useQueryClient();
  const currentUser = queryClient.getQueryData<UserPublic>(["currentUser"]);

  const finalItems: Item[] = currentUser?.is_superuser
    ? [...items, { icon: FiUsers, title: "Admin", path: "/admin" }]
    : items;

  const listItems = finalItems.map(({ icon, title, path }) => (
    <>
      <RouterLink key={title} to={path} onClick={onClose}>
        <Flex
          gap={4}
          px={4}
          py={2}
          _hover={{
            background: "gray.subtle",
          }}
          alignItems="center"
          fontSize="sm"
        >
          <Icon as={icon} alignSelf="center" />
          <Text ml={2}>{title}</Text>
        </Flex>
      </RouterLink>
      <Separator size="sm" borderColor="#adadad" borderWidth="0.4px" />
    </>
  ));

  return (
    <>
      <Text fontSize="xs" px={4} py={2} fontWeight="bold">
        Menu
      </Text>
      <Box>{listItems}</Box>
    </>
  );
};

export default SidebarItems;
