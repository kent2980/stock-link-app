import { Box, Flex } from "@chakra-ui/react";
import { createFileRoute, Outlet, redirect } from "@tanstack/react-router";

import Footer from "@/components/Common/Footer";
import Header from "@/components/Common/Header";
import AppSidebar from "@/components/Common/Sidebar";
import { isLoggedIn } from "@/hooks/useAuth";

export const Route = createFileRoute("/_layout")({
  component: Layout,
  beforeLoad: async () => {
    if (!isLoggedIn()) {
      throw redirect({
        to: "/login",
      });
    }
  },
});

const HEADER_HEIGHT = "96px";
const FOOTER_HEIGHT = "64px";

function Layout() {
  return (
    <Flex direction="column">
      <Header headerHeight={HEADER_HEIGHT} />
      <Box
        w="100%"
        mx="auto"
        pt={HEADER_HEIGHT}
        pb={{ base: FOOTER_HEIGHT, md: 0 }}
      >
        <AppSidebar />
        <Box
          ml={{ base: 0, md: "16" }}
          bg="gray.50"
          h={{
            base: "calc(100vh - 160px)",
            md: "calc(100vh - 96px)", // デスクトップはフッタ分を引かない
          }}
        >
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
