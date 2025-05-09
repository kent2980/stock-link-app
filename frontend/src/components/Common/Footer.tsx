import { MenuListStore } from "@/Store/Store";
import { Flex, FlexProps, IconButton } from "@chakra-ui/react";
import { useNavigate } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import React from "react";

interface FooterProps extends FlexProps {
  footerHeight?: number; // ヘッダーの高さを指定するプロパティ
}

const Footer: React.FC<FooterProps> = ({ footerHeight = 12, ...props }) => {
  const { menuList } = useStore(MenuListStore, (state) => state); // ストアからデータを取得
  const navigate = useNavigate();
  const handleMenuClick = (menuUrl: string | null | undefined) => {
    if (menuUrl) {
      navigate({ to: menuUrl });
    }
  };

  return (
    <Flex
      id="footer"
      as="footer"
      w="100%"
      justifyContent="center"
      alignItems="center"
      position="fixed"
      bottom={{ base: `-${footerHeight * 4}px`, md: 0 }} // 隠すときは上に移動
      display={{ base: "flex", md: "none" }}
      zIndex={1000}
      boxShadow="md"
      h={footerHeight}
      bg="gray.50"
      {...props}
    >
      <Flex
        direction="row"
        justifyContent="space-evenly"
        alignItems="center"
        m={"0 auto"}
        px={4}
        w="100%"
      >
        {menuList.map((item, index) => (
          <IconButton
            key={index}
            aria-label={item.menuLabel}
            variant="ghost"
            onClick={() => handleMenuClick(item.menuUrl)}
            _hover={{ bg: "gray.200" }}
            _active={{ bg: "gray.300" }}
            _focus={{ boxShadow: "outline" }}
            size={"2xl"}
          >
            {item.menuIcon}
          </IconButton>
        ))}
      </Flex>
    </Flex>
  );
};
export default Footer;
