import { Link, Text, VStack } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";
import { WikiService } from "../../../../../client";

interface WikiInfoProps {
  code: string;
}

const WikiInfo: React.FC<WikiInfoProps> = ({ code }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["wikiInfo", { code }],
    queryFn: async () => {
      return await WikiService.getStockWikiItem({ code: code });
    },
    retry: 0,
  });

  const get_url = (url: string | null) => {
    if (url) {
      return url;
    } else {
      return undefined;
    }
  };

  return (
    <>
      <VStack bg="gray.900" spacing={2} align="start">
        <Text fontSize="md">企業情報</Text>
        <Text color="gray.300" fontSize="sm">
          {data?.description}
        </Text>
        <Text fontSize="sm" color="gray.500" textAlign="left">
          引用元: Wikipedia URL:
          <Link href={get_url(data?.url)}>{data?.url}</Link>
        </Text>
      </VStack>
    </>
  );
};

export default WikiInfo;
