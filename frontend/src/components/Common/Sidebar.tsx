import {
  Box,
  Button,
  Drawer,
  DrawerBody,
  DrawerCloseButton,
  DrawerContent,
  DrawerOverlay,
  Flex,
  Icon,
  IconButton,
  Text,
  useColorModeValue,
  useDisclosure,
} from "@chakra-ui/react";
import { useQueryClient } from "@tanstack/react-query";
import { FiLogOut, FiMenu } from "react-icons/fi";

import { forwardRef } from "react";
import { MdMail } from "react-icons/md";
import type { UserPublic } from "../../client";
import useAuth from "../../hooks/useAuth";
import SidebarItems from "./SidebarItems";

interface sidebarProps {
  marginTop: string | number;
}

const Sidebar = forwardRef<HTMLDivElement, sidebarProps>(
  ({ marginTop }, ref) => {
    const queryClient = useQueryClient();
    const bgColor = useColorModeValue("ui.light", "ui.dark");
    const textColor = useColorModeValue("ui.dark", "ui.light");
    const currentUser = queryClient.getQueryData<UserPublic>(["currentUser"]);
    const { isOpen, onOpen, onClose } = useDisclosure();
    const { logout } = useAuth();

    const handleLogout = async () => {
      logout();
    };

    return (
      <>
        {/* Mobile */}
        <IconButton
          onClick={onOpen}
          display={{ base: "flex", md: "none" }}
          aria-label="Open Menu"
          position="fixed"
          top={0}
          right={0}
          fontSize="20px"
          mx={4}
          mt={14}
          icon={<FiMenu />}
          zIndex={3}
        />
        <Drawer isOpen={isOpen} placement="left" onClose={onClose}>
          <DrawerOverlay />
          <DrawerContent maxW="250px" zIndex={4000} mt={marginTop}>
            <DrawerCloseButton />
            <DrawerBody py={8}>
              <Flex flexDir="column" justify="space-between">
                <Box>
                  <SidebarItems onClose={onClose} />
                  <Flex
                    as="button"
                    onClick={handleLogout}
                    p={2}
                    color="ui.danger"
                    fontWeight="bold"
                    alignItems="center"
                  >
                    <FiLogOut />
                    <Text ml={2}>Log out</Text>
                  </Flex>
                </Box>
                {currentUser?.email && (
                  <Text color={textColor} noOfLines={2} fontSize="sm" p={2}>
                    Logged in as: {currentUser.email}
                  </Text>
                )}
              </Flex>
            </DrawerBody>
          </DrawerContent>
        </Drawer>

        {/* Desktop */}
        <Box
          ref={ref}
          bg={bgColor}
          p={1}
          h="100vh"
          position="fixed"
          display={{ base: "none", md: "flex" }}
          zIndex={3}
          minW={230}
          mt={marginTop}
        >
          <Flex flexDir="column" p={4} borderRadius={12} gap={6}>
            <Box>
              <SidebarItems />
            </Box>
            {currentUser?.email && (
              <Flex alignItems="center">
                <Icon as={MdMail} />
                <Text
                  color={textColor}
                  noOfLines={2}
                  fontSize="sm"
                  p={2}
                  maxW="180px"
                >
                  {currentUser.email}
                </Text>
              </Flex>
            )}
            <Box>
              <Flex justifyContent="center">
                <Button
                  fontSize={12}
                  color="ui.danger"
                  fontWeight={600}
                  onClick={handleLogout}
                  leftIcon={<FiLogOut />}
                >
                  ログアウト
                </Button>
              </Flex>
            </Box>
          </Flex>
        </Box>
      </>
    );
  }
);

export default Sidebar;
