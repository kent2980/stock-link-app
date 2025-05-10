import { Box, Heading, Text, VStack } from "@chakra-ui/react";
import { createFileRoute, useNavigate } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/")({
  component: Index,
});

function Index() {
  const menuItems = [
    { label: "タイムライン", path: "/stock" },
    { label: "お気に入り", path: "/favorite" },
    { label: "業種別", path: "/industry" },
    { label: "銘柄別", path: "/stock" },
    { label: "設定", path: "/settings" },
    { label: "ヘルプ", path: "/help" },
  ];

  const navigate = useNavigate({
    from: "/_layout/",
  });
  const handleClick = (path: any) => {
    navigate({
      to: path,
    });
  };
  return (
    <VStack h="100%" bg="ui.background" p={6} gap={10}>
      <Box mx="auto" mb={4}>
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
      <VStack>
        {menuItems.map((item, key) => (
          <Box
            key={key}
            w={{ base: 300, md: 500 }}
            h={{ base: 12, md: 16 }}
            borderBottomWidth={1}
            borderBottomStyle="solid"
            borderColor="black"
            p={2}
            display="flex"
            alignItems="center"
            onClick={() => handleClick(item.path)}
          >
            <Text>{item.label}</Text>
          </Box>
        ))}
      </VStack>
    </VStack>
  );
}
