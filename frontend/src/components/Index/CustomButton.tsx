import { Button, ButtonProps } from "@chakra-ui/react";
import React from "react";

const CustomButton: React.FC<ButtonProps> = (props) => {
  const { children } = props;
  return (
    <Button {...props} size="sm" borderRadius={0}>
      {children}
    </Button>
  );
};

export default CustomButton;
