import {
  Box,
  BoxProps,
  IconButton,
  IconButtonProps,
  VStack,
} from "@chakra-ui/react";
import { useNavigate } from "@tanstack/react-router";
import { IoHomeOutline, IoSettings } from "react-icons/io5";

const Sidebar: React.FC<BoxProps> = (props) => {
  const navigate = useNavigate();
  const handleHomeClick = (url: string) => {
    navigate({
      to: url,
    });
  };
  return (
    <Box
      display={{
        base: "none",
        md: "block",
      }}
      as="nav"
      w={"80px"}
      h="100vh"
      bg="gray.800"
      p={1}
      position="fixed"
      top="0"
      left="0"
      {...props}
    >
      <VStack align="start" gap="4">
        <CustomIconButton
          aria-label="home"
          onClick={() => handleHomeClick("/")}
        >
          <IoHomeOutline color="white" />
        </CustomIconButton>
        <CustomIconButton
          aria-label="settings"
          onClick={() => handleHomeClick("/settings")}
        >
          <IoSettings color="white" />
        </CustomIconButton>
      </VStack>
    </Box>
  );
};

interface CustomIconButtonProps extends IconButtonProps {
  children: React.ReactNode;
}

const CustomIconButton: React.FC<CustomIconButtonProps> = ({
  children,
  ...props
}) => {
  return (
    <IconButton
      bg="gray.800"
      size={"2xl"}
      variant="solid"
      color="white"
      _hover={{ bg: "gray.700" }}
      _active={{ bg: "gray.600" }}
      {...props}
    >
      {children}
    </IconButton>
  );
};

export default Sidebar;
