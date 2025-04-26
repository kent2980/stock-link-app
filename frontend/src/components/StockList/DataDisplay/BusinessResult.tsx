import { SummaryService } from "@/client";
import { Box, BoxProps, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";

interface BusinessResultProps extends BoxProps {
  headItemKey: string;
}
const BusinessResult: React.FC<BusinessResultProps> = ({ headItemKey }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["BusinessResult", headItemKey],
    queryFn: async () => {
      return await SummaryService.getOperatingResults({
        headItemKey: headItemKey,
      });
    },
  });

  const items =
    data.result?.data?.map((dataItem) => ({
      name: dataItem.label,
      currentValue: dataItem.curValue?.value ?? 0,
      changeRate: dataItem.curChange?.value ?? 0,
      displayScale: dataItem.curValue?.display_scale ?? "",
      previousValue: dataItem.preValue?.value ?? 0,
      previousChangeRate: dataItem.preChange?.value ?? 0,
    })) ?? [];

  return (
    <Box>
      {items.map((item, index) => (
        <Box key={index} mb={2}>
          <Text fontSize="14px" fontWeight="bold">
            {item.name}{" "}
          </Text>
        </Box>
      ))}
    </Box>
  );
};
export default BusinessResult;
