import { Box, Flex } from "@chakra-ui/react";
import { createFileRoute, Outlet } from "@tanstack/react-router";

import { Footer } from "@/components/Common/Footer";
import { Header } from "@/components/Common/Header";
import Sidebar from "@/components/Common/Sidebar";

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
    <Flex direction="column" h="100vh" w="100vw" position="relative">
      {/* ヘッダーを上部に固定 */}
      <Box position="fixed" top={0} left={0} w="100vw" zIndex={1000}>
        <Header h="50px" />
      </Box>
      {/* サイドバーは必要に応じて調整 */}
      <Sidebar mt={16} w={60} links={[]} />
      {/* Outletを中央に配置（Header/Footer分の余白を確保） */}
      <Box
        flex="1"
        overflow="auto"
        pt="50px" // Headerの高さ分
        pb={{ base: "60px", md: 0 }} // Footerの高さ分（モバイルのみ）
        h="calc(100vh - 110px)" // Headerの高さを引いた残りの高さ
        w="100vw"
      >
        <Outlet />
      </Box>
      {/* フッターを下部に固定（モバイルのみ表示） */}
      <Box
        position="fixed"
        bottom={0}
        left={0}
        w="100vw"
        zIndex={1000}
        display={{ base: "block", md: "none" }}
      >
        <Footer h="60px" />
      </Box>
    </Flex>
  );
}

export default Layout;
