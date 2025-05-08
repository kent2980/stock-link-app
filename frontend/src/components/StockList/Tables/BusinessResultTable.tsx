import { FinancialSummaryService } from "@/client";
import { Box, Wrap } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";
import FinStructWrapItem from "./FinStructTable";

interface BusinessResultTableProps {
  HeadItemKey: string;
}

const BusinessResultTable: React.FC<BusinessResultTableProps> = ({
  HeadItemKey,
}) => {
  const { data } = useSuspenseQuery({
    queryKey: ["BusinessResult", HeadItemKey],
    queryFn: async () => {
      return await FinancialSummaryService.getOperatingResults({
        headItemKey: HeadItemKey,
      });
    },
  });
  return (
    <Box>
      <Wrap>
        {data?.data?.map((item, index) => (
          <FinStructWrapItem
            key={index}
            label={item.label}
            value={item.result?.curValue?.value}
            valueScale={item.result?.curValue?.display_scale}
            changeValue={item.result?.curChange}
          />
        ))}
      </Wrap>
    </Box>
  );
};
export default BusinessResultTable;
