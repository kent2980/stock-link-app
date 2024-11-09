import { Badge, Box, BoxProps, Heading, Stack, Text } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import React from "react";
import { XbrlViewService } from "../../client";
interface SummaryHeaderProps extends BoxProps {
  head_item_key: string;
}

const SummaryHeader: React.FC<SummaryHeaderProps> = ({
  head_item_key,
  ...props
}) => {
  const { data: item, status } = useQuery({
    queryKey: ["head", head_item_key],
    queryFn: () =>
      XbrlViewService.readHeadItem({
        headItemKey: head_item_key,
      }),
    staleTime: 1000 * 60 * 60 * 24 * 7,
    gcTime: 1000 * 60 * 60 * 24 * 30,
  });

  if (status === "error") {
    return <Box>Error</Box>;
  }

  if (status === "pending") {
    return <Box>Loading...</Box>;
  }

  return (
    <Box
      as="header"
      borderWidth="1px"
      borderRadius="0"
      p={4}
      bg="white"
      textAlign="center"
      position="fixed"
      top={0}
      left={{ base: 0, md: 56 }}
      zIndex={1000}
      width="100%"
      {...props}
    >
      <Stack direction="row" spacing={6}>
        <Badge
          px={3}
          py={1}
          borderRadius="md"
          colorScheme="pink"
          variant="solid"
          display="flex"
          alignItems="center"
        >
          <Text>{item.securities_code}</Text>
        </Badge>
        <Heading
          as="h1"
          size={item.company_name.length > 15 ? "xs" : "sm"}
          color="blue.700"
          mx="auto"
          display="flex"
          alignItems="center"
        >
          {item.company_name}
        </Heading>
      </Stack>
      <Text
        fontSize={item.document_name.length > 28 ? "13px" : "sm"}
        color="gray.600"
        mt={2}
      >
        {item?.document_name.length > 25
          ? `${item.document_name.slice(0, 25)}...`
          : item.document_name}
      </Text>
    </Box>
  );
};

export default SummaryHeader;
