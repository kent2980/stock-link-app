import { List, ListRootProps } from "@chakra-ui/react";
import React from "react";
interface CustomListRootProps extends ListRootProps {
  children: React.ReactNode;
  height: number | string;
}

const CustomListRoot = ({
  children,
  height,
  ...props
}: CustomListRootProps) => {
  return (
    <List.Root
      h={height}
      w="100%"
      position="relative"
      maxW={{ base: "100%", md: "calc(100vw - 250px)" }}
      m="auto" // 中央に配置
      {...props}
    >
      {children}
    </List.Root>
  );
};

export default CustomListRoot;
