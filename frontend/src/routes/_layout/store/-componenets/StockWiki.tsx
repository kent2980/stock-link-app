import { WikiService } from "@/client";
import { Box, Flex, Link, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";

interface StockWikiProps {
  code: string;
}

const StockWiki: React.FC<StockWikiProps> = ({ code }) => {
  const { data, error } = useSuspenseQuery({
    queryKey: ["stock", code],
    queryFn: async () => {
      return await WikiService.getStockWikiItem({
        code: code,
      });
    },
    retry: 0,
  });

  const getUrl = (url: string | null) => {
    if (url === null) {
      return undefined;
    }
    return url;
  };

  if (error) {
    return <Text>エラーが発生しました</Text>;
  }

  return (
    <Box w={{ base: "100%", md: "60%" }}>
      <Box
        p={4}
        bg="ui.description"
        borderRadius={8}
        boxShadow="md"
        fontSize={{ base: 14, md: 16 }}
      >
        <Text>{data.description}</Text>
      </Box>
      <Flex direction={{ base: "column", md: "row" }} gap={2} pt={4}>
        <Text color="gray.500" fontSize={{ base: 12, md: 14 }} textAlign="left">
          引用: wikipedia
        </Text>
        <Text fontSize={{ base: 12, md: 14 }} textAlign="left">
          <Link
            href={getUrl(data.url)}
            target="_blank"
            rel="noopener noreferrer"
            color="ui.link"
            _hover={{ color: "ui.link_hover" }}
          >
            {data.url}
          </Link>
        </Text>
      </Flex>
    </Box>
  );
};

export default StockWiki;
