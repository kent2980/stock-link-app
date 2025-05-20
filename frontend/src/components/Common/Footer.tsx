import { Box, Grid, Link } from "@chakra-ui/react";
import { BarChart2, Briefcase, Heart, Home, Search } from "lucide-react";

export function Footer() {
  const navItems = [
    {
      name: "ホーム",
      href: "/",
      icon: Home,
    },
    {
      name: "検索",
      href: "/stocks",
      icon: Search,
    },
    {
      name: "チャート",
      href: "/chart-analysis",
      icon: BarChart2,
    },
    {
      name: "ポートフォリオ",
      href: "/portfolio",
      icon: Briefcase,
    },
    {
      name: "お気に入り",
      href: "/favorites",
      icon: Heart,
    },
  ];

  return (
    <Box
      position="fixed"
      bottom={0}
      left={0}
      zIndex={50}
      width="100vw"
      py={2}
      borderTop="1px"
      borderColor="gray.200"
      borderStyle="solid"
      bg="white"
      _dark={{ bg: "gray.900", borderColor: "gray.800" }}
      display={{ base: "block", md: "none" }}
    >
      <Grid mx="auto" h="56px" maxW="lg" templateColumns="repeat(5, 1fr)">
        {navItems.map((item) => (
          <Link
            key={item.name}
            href={item.href}
            display="inline-flex"
            alignItems="center"
            justifyContent="center"
            px={5}
            py={3}
            color="green.600"
            _hover={{ color: "green.600" }}
          >
            <Box
              as={item.icon}
              h={6}
              w={6}
              transition="colors"
              color="green.600"
              _groupHover={{ color: "green.600" }}
            />
          </Link>
        ))}
      </Grid>
    </Box>
  );
}
