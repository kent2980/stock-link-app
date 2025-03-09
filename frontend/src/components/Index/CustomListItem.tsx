import { List, ListItemProps } from "@chakra-ui/react";
import React from "react";

interface CustomListItemProps extends ListItemProps {
  children: React.ReactNode;
  key: React.Key | null | undefined;
  top: number | string;
  height: number | string;
}

const CustomListItem = ({
  children,
  key,
  top,
  height,
  ...props
}: CustomListItemProps) => {
  return (
    <List.Item
      key={key}
      position="absolute"
      top={top}
      left={0}
      width="100%"
      height={height}
      display="flex"
      border="1px solid"
      borderColor="gray.200"
      p={4}
      bg="white"
      {...props}
    >
      {children}
    </List.Item>
  );
};

export default CustomListItem;
