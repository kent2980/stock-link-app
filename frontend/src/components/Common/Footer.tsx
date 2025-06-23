import { Box, Grid, Link } from "@chakra-ui/react";
import { useNavigate, useRouterState } from "@tanstack/react-router";
import { Home, Menu } from "lucide-react";

export function Footer() {
  const navItems = [
    // {
    //   name: "検索",
    //   href: "/stocks",
    //   icon: Search,
    // },
    {
      name: "メニュー",
      href: "/menu",
      icon: Menu,
    },
  ];

  // useNavigateを使ってページ遷移を行う
  const navigate = useNavigate();
  // useRouterStateを使って現在のパスを取得
  const CurrentPath = useRouterState().location.pathname;

  // ホームに戻るハンドラー
  // 現在のパスが"/"の場合はページをTopにスクロール
  // それ以外の場合は"/"に遷移
  const switchHomeHandler = () => {
    // 現在のアドレスが"/"の場合
    if (CurrentPath === "/") {
      // ページをTopにスクロール
      window.scrollTo({ top: 0, behavior: "smooth" });
    } else {
      // それ以外の場合は"/"に遷移
      navigate({ to: "/" });
    }
  };

  return (
    <Box
      position="fixed"
      bottom={0}
      left={0}
      zIndex={50}
      width="100vw"
      pb={6}
      borderTop="1px"
      borderColor="gray.200"
      borderStyle="solid"
      bg="white"
      _dark={{ bg: "gray.900", borderColor: "gray.800" }}
      display={{ base: "block", md: "none" }}
    >
      <Grid
        mx="auto"
        h="56px"
        maxW="lg"
        templateColumns={`repeat(${navItems.length + 1}, 1fr)`}
      >
        <Box
          display="inline-flex"
          alignItems="center"
          justifyContent="center"
          px={5}
          py={3}
          color="green.600"
          _hover={{ color: "green.600" }}
          onClick={switchHomeHandler}
        >
          <Box
            as={Home}
            h={6}
            w={6}
            transition="colors"
            color="green.600"
            _groupHover={{ color: "green.600" }}
          />
        </Box>
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
