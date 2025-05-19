import { Box, Flex } from "@chakra-ui/react";
import { createFileRoute, Outlet } from "@tanstack/react-router";

import Footer from "@/components/Common/Footer";
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

const HEADER_HEIGHT = 10;
const FOOTER_HEIGHT = 16;
function Layout() {
  return (
    <Flex direction="column">
      <Header />
      <Box w="100%" mx="auto" mb={{ base: FOOTER_HEIGHT, md: 0 }}>
        {/* <AppSidebar /> */}
        <Box bg="gray.50">
          <Outlet />
        </Box>
      </Box>
      {/* フッターはモバイルのみ表示 */}
      <Box display={{ base: "block", md: "none" }}>
        <Footer footerHeight={FOOTER_HEIGHT} />
      </Box>
    </Flex>
  );
}

export default Layout;
