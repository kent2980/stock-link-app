import { Box, Text } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute(
  "/_layout/summary/$code/_layout/$headKey/summary"
)({
  component: Summary,
});

function Summary() {
  const { code, headKey } = Route.useParams();
  return (
    <Box>
      <Text>{code}</Text>
      <Text>{headKey}</Text>
    </Box>
  );
}
