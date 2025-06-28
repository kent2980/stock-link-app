import { JpxService } from "@/client";
import { Box, Flex, List, Spinner, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useNavigate } from "@tanstack/react-router";
import React from "react";

const Industries: React.FC = () => {
  const { data, isPending, isError } = useSuspenseQuery({
    queryKey: ["industriesList"],
    queryFn: async () => {
      return await JpxService.getIndustriesInfo({ type: 33 });
    },
    staleTime: 1000 * 60 * 60 * 24,
    gcTime: 1000 * 60 * 60 * 24,
    retry: false,
  });

  if (isPending) {
    return (
      <Box py={8} textAlign="center">
        <Spinner size="xl" />
      </Box>
    );
  }

  if (isError) {
    return (
      <Box py={8} textAlign="center">
        <Text color="red.500">業種情報の取得に失敗しました。</Text>
      </Box>
    );
  }
  const navigate = useNavigate({ from: "/industries" });

  const handleIndustryClick = (code: string, select_date: string) => {
    navigate({
      to: "/industries/$code/$selectDate",
      params: { code, selectDate: select_date },
    });
  };

  return (
    <Box maxW="lg" mx="auto">
      <List.Root gap={4} m={4} listStyle="none">
        {data.data.map((industry) => (
          <List.Item
            key={industry.code}
            p={3}
            borderWidth="1px"
            bg="#477bcf"
            color="white"
            _hover={{ bg: "#3b5f9f" }}
            transition="background-color 0.2s"
            onClick={() =>
              handleIndustryClick(
                industry.code?.toString(),
                industry.new_report_date
              )
            }
          >
            <Flex justifyContent="space-between" alignItems="center">
              <Text fontWeight="bold">{industry.name}</Text>
              <Text fontSize="sm">新規: {industry.todays_record ?? 0}件</Text>
            </Flex>
          </List.Item>
        ))}
      </List.Root>
    </Box>
  );
};

export default Industries;
