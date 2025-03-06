import { Card } from "@chakra-ui/react";
import React from "react";

interface CustomCardProps extends Card.RootProps {
  children: React.ReactNode;
}

function CustomCard({ children, ...props }: CustomCardProps) {
  return (
    <Card.Root {...props} h="220px" m={{ base: "1", md: "2" }}>
      {children}
    </Card.Root>
  );
}

export default CustomCard;
