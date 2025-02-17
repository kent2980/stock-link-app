import { Box, Button, Text, VStack } from "@chakra-ui/react";
import { createFileRoute, useNavigate } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/summary/")({
  component: Index,
});

function Index() {
  const navigate = useNavigate({
    from: "src/routes/_layout/summary/index.tsx",
  });
  const handleReturnHome = () => {
    navigate({ to: "/" });
  };
  return (
    <Box
      display="flex"
      alignItems="center"
      justifyContent="center"
      height="100vh"
      p={4}
    >
      <VStack spacing={4} textAlign="center">
        <Text fontSize="md" color="gray.700">
          銘柄コードが指定されていません。
        </Text>
        <Button onClick={handleReturnHome} colorScheme="teal" size="md">
          ホームに戻る
        </Button>
      </VStack>
    </Box>
  );
}
