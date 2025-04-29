import { Box, Flex, Icon, Link, Text, VStack } from "@chakra-ui/react";
import React from "react";
import { FiHome, FiSettings, FiTrendingUp } from "react-icons/fi";

interface SidebarProps {
  links: { name: string; icon: React.ElementType; href: string }[];
}

const Sidebar: React.FC<SidebarProps> = ({ links }) => {
  return (
    <Box
      bg="gray.50"
      w={60}
      pos="fixed"
      h="full"
      shadow="md"
      display={{ base: "none", md: "block" }}
    >
      <Flex h="20" alignItems="center" justifyContent="center" shadow="sm">
        <Text fontSize="2xl" fontWeight="bold" color="gray.700">
          Sidebar
        </Text>
      </Flex>
      <VStack gap={4} mt={4} align="stretch">
        {links.map((link) => (
          <Link
            key={link.name}
            href={link.href}
            style={{ textDecoration: "none" }}
            _hover={{ textDecoration: "none", bg: "gray.200" }}
          >
            <Flex
              align="center"
              p={4}
              mx={4}
              borderRadius="lg"
              role="group"
              cursor="pointer"
              _hover={{
                bg: "gray.300",
                color: "black",
              }}
            >
              <Icon
                mr={4}
                fontSize="16"
                as={link.icon}
                _groupHover={{
                  color: "black",
                }}
              />
              <Text>{link.name}</Text>
            </Flex>
          </Link>
        ))}
      </VStack>
    </Box>
  );
};

export default function AppSidebar() {
  const links = [
    { name: "Home", icon: FiHome, href: "/" },
    { name: "Trending", icon: FiTrendingUp, href: "/trending" },
    { name: "Settings", icon: FiSettings, href: "/settings" },
  ];

  return <Sidebar links={links} />;
}
