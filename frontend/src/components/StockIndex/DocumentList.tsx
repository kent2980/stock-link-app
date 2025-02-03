import { Box, Select, Text, VStack } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";
import { XbrlIxHeadService } from "../../client";
import { StockIndexStore } from "../../Store/StockIndexStore";

interface DocumentInfoProps {
  code: string;
}

const DocumentList: React.FC<DocumentInfoProps> = ({ code }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["DocumentInfoFromCode", code],
    queryFn: async () => {
      return await XbrlIxHeadService.getDocumentInfo({
        code: code,
      });
    },
    staleTime: 1000 * 60 * 60 * 24 * 30, // 30 days
    gcTime: 1000 * 60 * 60 * 24 * 30, // 30 days
  });
  const handleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    console.log(e.target.value);
    StockIndexStore.setState((state) => ({
      ...state,
      head_item_key: e.target.value,
    }));
  };
  StockIndexStore.setState((state) => ({
    ...state,
    head_item_key: data?.data[0].item_key,
  }));
  return (
    <Box>
      <VStack spacing={4}>
        <Text alignSelf="flex-start" mx={4}>
          書類選択
        </Text>
        <Select onChange={handleChange}>
          {data?.data.map((item) => {
            const optionText = `${item.reporting_date}    ${item.current_period ?? ""}    ${item.document_name}`;
            return (
              <option value={item.item_key} key={item.item_key}>
                {optionText}
              </option>
            );
          })}
        </Select>
      </VStack>
    </Box>
  );
};

export default DocumentList;
