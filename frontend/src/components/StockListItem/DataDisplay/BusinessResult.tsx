import { SummaryService } from "@/client";
import { Box, BoxProps, Skeleton } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { Suspense } from "react";
import DataDisplay from "../DataDisplay";

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

  const items = data.data.flatMap(
    (item) =>
      item.result?.data?.map((dataItem) => ({
        name: dataItem.label,
        currentValue: dataItem.curValue?.value ?? 0,
        changeRate: dataItem.curChange?.value ?? 0,
        displayScale: dataItem.curValue?.display_scale ?? "",
        previousValue: dataItem.preValue?.value ?? 0,
        previousChangeRate: dataItem.preChange?.value ?? 0,
      })) ?? []
  );
  return (
    <Box>
      <Suspense fallback={<Skeleton height="20px" width="100%" />}>
        <DataDisplay data={items} title="経営成績" />
      </Suspense>
    </Box>
  );
};
export default BusinessResult;
