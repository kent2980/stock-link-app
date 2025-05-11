import { FinancialSummaryService } from "@/client";
import { Box } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";

interface DividendTableProps {
  HeadItemKey: string;
}
const DividendTable: React.FC<DividendTableProps> = ({ HeadItemKey }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["Dividend", HeadItemKey],
    queryFn: async () => {
      return await FinancialSummaryService.getDividends({
        headItemKey: HeadItemKey,
      });
    },
  });
  const value = data.data;
  return (
    <Box>
      <Box>{value?.FirstQuarterMember?.result?.curValue?.value}</Box>
      <Box>{value?.SecondQuarterMember?.result?.curValue?.value}</Box>
      <Box>{value?.ThirdQuarterMember?.result?.curValue?.value}</Box>
      <Box>{value?.YearEndMember?.result?.curValue?.value}</Box>
      <Box>{value?.AnnualMember?.result?.curValue?.value}</Box>
    </Box>
  );
};
export default DividendTable;
