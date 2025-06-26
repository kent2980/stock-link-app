import { JpxService } from "@/client";
import { Box, Flex } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { useState } from "react";
import "swiper/css";
import "swiper/css/navigation";
import DisclosurePage from "./Disclosure";

const DisclosureIndex: React.FC = () => {
  const { data } = useSuspenseQuery({
    queryKey: ["disclosureIndex"],
    queryFn: async () => {
      return await JpxService.readJpxStockInfoIndustryNames({
        type: 17,
      });
    },
    retry: false,
    staleTime: 1000 * 60 * 60 * 24, // 1 day
    gcTime: 1000 * 60 * 60 * 24, // 1 day
  });

  const [code, setCode] = useState<number | undefined>(undefined);
  return (
    <>
      <Flex
        as="nav"
        direction="row"
        overflowX="auto"
        maxW="100vw"
        py={2}
        px={1}
        gap={2}
        style={{
          scrollbarWidth: "thin",
        }}
      >
        {data.data.map((item) => (
          <Box
            key={item.code}
            as="button"
            onClick={() => setCode(item.code)}
            w={180}
            minW={180}
            mx={1}
            px={4}
            py={2}
            borderRadius="md"
            bg={code === item.code ? "blue.500" : "gray.100"}
            color={code === item.code ? "white" : "gray.800"}
            fontWeight={code === item.code ? "bold" : "normal"}
            boxShadow={code === item.code ? "md" : "none"}
            border={
              code === item.code ? "2px solid #3182ce" : "1px solid #e2e8f0"
            }
            cursor="pointer"
            transition="all 0.2s"
            _hover={{
              bg: code === item.code ? "blue.600" : "gray.200",
            }}
            whiteSpace="nowrap"
            flexShrink={0}
          >
            {item.name}
          </Box>
        ))}
      </Flex>
      <DisclosurePage code_17={code} />
    </>
  );
};

export default DisclosureIndex;
