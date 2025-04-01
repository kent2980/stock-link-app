import { Box, HStack, IconButton, Text } from "@chakra-ui/react";
import { Heart, MessageCircle, Repeat } from "lucide-react";
import React from "react";

const Footer: React.FC = () => {
  const iconSize = "sm";

  return (
    <Box>
      <HStack justifyContent="space-between" alignItems="center">
        <HStack gap={4} align="center">
          <Text fontSize="xs" color="gray.400">
            2 hours ago
          </Text>
        </HStack>
        <HStack gap={4} align="center">
          <IconButton variant="ghost" size={iconSize} aria-label="Reply">
            <MessageCircle color="#3b82f6" />
          </IconButton>
          <IconButton variant="ghost" size={iconSize} aria-label="Retweet">
            <Repeat color="#3b82f6" />
          </IconButton>
          <IconButton variant="ghost" size={iconSize} aria-label="Like">
            <Heart color="#292327" />
          </IconButton>
        </HStack>
      </HStack>
    </Box>
  );
};

export default Footer;
