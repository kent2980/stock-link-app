import { Box, Heading, Text, VStack } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/")({
  component: Index,
});

function Index() {
  const menuItems = [
    { label: "未読アイテム", path: "/unread" },
    { label: "既読アイテム", path: "/read" },
    { label: "お気に入り", path: "/favorite" },
    { label: "業種別", path: "/industry" },
    { label: "銘柄別", path: "/stock" },
    { label: "設定", path: "/settings" },
    { label: "ヘルプ", path: "/help" },
  ];
  return (
    <VStack h="100%" bg="ui.background" p={6} gap={10}>
      <Box w="300px" mx="auto" mb={4}>
        <Heading as="h1" size="5xl" textAlign="center">
          C
          <Text
            as="span"
            textDecoration="underline"
            textUnderlineOffset="8px"
            mx={1}
          >
            losi
          </Text>
          o
        </Heading>
      </Box>
      <VStack gap={4}>
        {menuItems.map((item) => (
          <Box
            w={300}
            borderBottomWidth={1}
            borderBottomStyle="solid"
            borderColor="black"
            p={2}
          >
            {item.label}
          </Box>
        ))}
      </VStack>
    </VStack>
  );
}
