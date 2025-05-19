import { Box, Flex } from "@chakra-ui/react";
import { createFileRoute, Outlet } from "@tanstack/react-router";

import { Footer } from "@/components/Common/Footer";
import { Header } from "@/components/Common/Header";

export const Route = createFileRoute("/_layout")({
  component: Layout,
  // リダイレクト設定は必要に応じて行う
  // beforeLoad: async () => {
  //   if (!isLoggedIn()) {
  //     throw redirect({
  //       to: "/login",
  //     });
  //   }
  // },
});

function Layout() {
  return (
    <Flex direction="column">
      <Header />
      {/* <AppSidebar /> */}
      <Box bg="gray.50" pb={{ base: "80px", md: "40px" }} pt="20px">
        <Outlet />
      </Box>
      {/* フッターはモバイルのみ表示 */}
      <Box display={{ base: "block", md: "none" }}>
        <Footer />
      </Box>
    </Flex>
  );
}

export default Layout;
