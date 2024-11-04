import {
  Box,
  BoxProps,
  Button,
  HStack,
  Input,
  Tag,
  TagLabel,
  Text,
  VStack,
} from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import dayjs from "dayjs";
import React from "react";
import { XbrlIxHeadService } from "../../client";
import StockList from "./StockList";

interface SelectItemProps extends BoxProps {
  selectDate: string;
}

const SelectItem: React.FC<SelectItemProps> = ({ selectDate, ...props }) => {
  const { data: reportCount } = useQuery({
    queryKey: ["report_type_count", selectDate],
    queryFn: () =>
      XbrlIxHeadService.getCountReportType({
        dateStr: selectDate,
      }),
    // gcTime: 1000 * 60 * 60 * 24,
    // staleTime: 1000 * 60 * 60 * 24,
  });

  let earningsReportCount = 0;
  let performanceForecastRevisionCount = 0;
  let dividendForecastRevisionCount = 0;

  reportCount?.data.forEach((item) => {
    if (item.report_type.startsWith("ed")) {
      earningsReportCount += item.count;
    } else if (item.report_type.startsWith("rvfc")) {
      performanceForecastRevisionCount += item.count;
    } else if (item.report_type.startsWith("rvdf")) {
      dividendForecastRevisionCount += item.count;
    }
  });

  return (
    <Box {...props} w="100vw">
      <Box
        py={1}
        width={140}
        bg="white"
        boxShadow="md"
        border="0.5px solid #ccc"
        borderRadius="4px"
        position="fixed"
        top={120}
        left={2}
        zIndex={1}
      >
        <Text textAlign="center">
          {dayjs(selectDate).format("YYYY.MM.DD (ddd)")}
        </Text>
      </Box>
      <Box
        bg="white"
        boxShadow="md"
        position="fixed"
        zIndex="1"
        top="calc(100vh - 140px)"
        left={2}
        border="0.5px solid #ccc"
        borderRadius="4px"
        display="none"
      >
        <Button colorScheme="blue" variant="outline" size="sm">
          日付選択解除
        </Button>
      </Box>
      <VStack spacing={1} w="full">
        <Box
          borderBottom="1px"
          borderColor="gray.200"
          w="full"
          display="flex"
          alignItems="center"
          justifyContent="center"
          px={4}
          py={2}
        >
          <Input variant="filled" placeholder="銘柄コードで検索" />
        </Box>
        <Box borderBottom="1px" borderColor="gray.200" w="full">
          <HStack
            align="end"
            m={1}
            p={2}
            spacing={2}
            color="gray.600"
            fontWeight="500"
            fontSize="10px"
            justifyContent="space-between"
          >
            <Tag>
              <TagLabel fontSize="12px">
                決算短信 {earningsReportCount} 件
              </TagLabel>
            </Tag>
            <Tag>
              <TagLabel fontSize="12px">
                業績予想の修正 {performanceForecastRevisionCount} 件
              </TagLabel>
            </Tag>
            <Tag>
              <TagLabel fontSize="12px">
                配当予想の修正 {dividendForecastRevisionCount} 件
              </TagLabel>
            </Tag>
          </HStack>
        </Box>

        <StockList selectDate={selectDate} />
      </VStack>
    </Box>
  );
};

export default SelectItem;
