import { XbrlIxHeadService } from "@/client";
import { Box, Flex } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { Suspense } from "react";
import ForecastProgressRate from "./IRSummary/ForecastProgressRate";
import ForecastTable from "./IRSummary/ForecastTable";
import OperatingResult from "./IRSummary/OperatingResult";

interface IXSummaryProps {
  head_item_key: string;
}

function IRSummary({ head_item_key }: IXSummaryProps) {
  const { data } = useSuspenseQuery({
    queryKey: ["IxHeadItem", head_item_key],
    queryFn: async () => {
      return await XbrlIxHeadService.readIxHeadTitleItem({
        headItemKey: head_item_key,
      });
    },
  });

  const reportTypes = ["edjp", "edif", "edus"];
  return (
    <Box>
      {reportTypes.includes(data.report_type ?? "") ? (
        <Flex direction="column" gap={4}>
          <Suspense fallback={<div>Loading...</div>}>
            <OperatingResult head_item_key={head_item_key} />
          </Suspense>
          <Suspense fallback={<div>Loading...</div>}>
            <ForecastTable head_item_key={head_item_key} />
          </Suspense>
          <Suspense fallback={<div>Loading...</div>}>
            <ForecastProgressRate head_item_key={head_item_key} />
          </Suspense>
        </Flex>
      ) : (
        <div>Not supported</div>
      )}
    </Box>
  );
}

export default IRSummary;
