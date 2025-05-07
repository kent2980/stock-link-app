import { FinancialSummary2Service } from "@/client";
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
      return await FinancialSummary2Service.getOperatingResults({
        headItemKey: HeadItemKey,
      });
    },
  });
  return (
    <Box>
      <Wrap>
        {data?.result?.data?.map((item, index) => (
          <FinStructWrapItem
            key={index}
            label={item.label}
            value={item.curValue?.value}
            valueScale={item.curValue?.display_scale}
            changeValue={item.curChange}
          />
        ))}
      </Wrap>
    </Box>
  );
};
export default BusinessResultTable;
