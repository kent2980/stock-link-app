import { Box, BoxProps, Flex, IconButton, Text } from "@chakra-ui/react";
import { useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
import { FiLogOut } from "react-icons/fi";

import type { UserPublic } from "@/client";
import useAuth from "@/hooks/useAuth";
import { GrMenu } from "react-icons/gr";
import {
  DrawerBackdrop,
  DrawerBody,
  DrawerCloseTrigger,
  DrawerContent,
  DrawerRoot,
  DrawerTrigger,
} from "../ui/drawer";
import SidebarItems from "./SidebarItems";

const Sidebar = (props: BoxProps) => {
  const queryClient = useQueryClient();
  const currentUser = queryClient.getQueryData<UserPublic>(["currentUser"]);
  const { logout } = useAuth();
  const [open, setOpen] = useState(false);

  return (
    <>
      {/* Mobile */}
      <DrawerRoot
        placement="start"
        open={open}
        onOpenChange={(e) => setOpen(e.open)}
      >
        <DrawerBackdrop />
        <DrawerTrigger asChild>
          <IconButton
            display={{ base: "flex", md: "none" }}
            aria-label="Open Menu"
            position="absolute"
            zIndex="140"
            m={4}
            top={0}
            borderRadius={10}
            size="sm"
          >
            <GrMenu />
          </IconButton>
        </DrawerTrigger>
        <DrawerContent maxW="xs">
          <DrawerCloseTrigger />
          <DrawerBody>
            <Flex flexDir="column" justify="space-between">
              <Box>
                <SidebarItems />
                <Flex
                  as="button"
                  onClick={() => {
                    logout();
                  }}
                  alignItems="center"
                  gap={4}
                  px={4}
                  py={2}
                >
                  <FiLogOut />
                  <Text>Log Out</Text>
                </Flex>
              </Box>
              {currentUser?.email && (
                <Text fontSize="sm" p={2} truncate maxW="sm">
                  Logged in as: {currentUser.email}
                </Text>
              )}
            </Flex>
          </DrawerBody>
          <DrawerCloseTrigger />
        </DrawerContent>
      </DrawerRoot>

      {/* Desktop */}

      <Box
        display={{ base: "none", md: "flex" }}
        position="relative"
        flexBasis="auto"
        flexShrink="0"
        bg="ui.light"
        p={4}
        m="0"
        justifyContent="flex-end" // 追加
        {...props}
      >
        <Box bg="ui.main" id="sideBarItem" p={4} borderRadius="md" w="100%">
          <SidebarItems />
        </Box>
      </Box>
    </>
  );
};

export default Sidebar;
