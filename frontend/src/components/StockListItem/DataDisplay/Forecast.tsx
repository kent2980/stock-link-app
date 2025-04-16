import { SummaryService } from "@/client";
import { Box } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";
import { DataItem } from "../DataDisplay";

interface ForecastProps {
  headItemKey: string;
}

const Forecast: React.FC<ForecastProps> = ({ headItemKey }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["Forecast", headItemKey],
    queryFn: async () => {
      return await SummaryService.getForecasts({
        headItemKey: headItemKey,
      });
    },
  });
  const items: DataItem[] =
    data.forecast?.data?.map((dataItem) => ({
      name: dataItem.label,
      currentValue: dataItem.curValue?.value ?? 0,
      changeRate: dataItem.curChange?.value ?? 0,
      displayScale: dataItem.curValue?.display_scale ?? "",
    })) ?? [];

  return <Box>{/* <DataDisplay data={items} title="通期業績予測" /> */}</Box>;
};
export default Forecast;
