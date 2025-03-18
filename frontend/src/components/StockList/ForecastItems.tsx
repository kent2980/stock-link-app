import { SummaryService } from "@/client";
import { useSuspenseQueries } from "@tanstack/react-query";
import {
  curValue,
  shortBusinessChange,
} from "../../routes/_layout/store/- utils/utils";
import BusinessResultHeader from "./BusinessResultHeader";
import BusinessResultItems from "./BusinessResultItems";
import BusinessResultRoot from "./BusinessResultRoot";

interface ForecastItemsProps {
  head_item_key: string;
  value: string;
}

const ForecastItems: React.FC<ForecastItemsProps> = ({
  head_item_key,
  value,
}) => {
  const [data1, data2] = useSuspenseQueries({
    queries: [
      {
        queryKey: ["ForecastItems", head_item_key],
        queryFn: async () => {
          return await SummaryService.getForecasts({
            headItemKey: head_item_key,
          });
        },
      },
      {
        queryKey: ["ForecastProgress", head_item_key],
        queryFn: async () => {
          return await SummaryService.getForecastProgressRate({
            headItemKey: head_item_key,
          });
        },
      },
    ],
  });

  const getSelectRate = (
    period: "forecast" | "upper" | "lower",
    item_name: string
  ) => {
    const periodDataMap = {
      forecast: data2.data.forecast,
      upper: data2.data.upper,
      lower: data2.data.lower,
    };
    console.log(item_name);
    console.log(data2.data);
    const periodData = periodDataMap[period];
    let select_item = null;
    if (periodData) {
      select_item = periodData
        .filter((item) => item.name === item_name)
        .map((item) => item.value)[0];
    }
    console.log(select_item);
    return select_item;
  };

  return (
    <BusinessResultRoot title="業績予想">
      <BusinessResultHeader
        columns={["予想値", "進捗率"]}
        widths={["50%", "50%"]}
      />
      {data1.data.data.map((items) =>
        items.forecast?.data?.map((item, key) => {
          const filter_name = item.curValue?.name;
          return (
            <BusinessResultItems
              key={key}
              label={item.label}
              curChange={curValue(item, value)}
              preChange={shortBusinessChange(
                getSelectRate("forecast", filter_name ?? "") ?? null
              )}
            />
          );
        })
      )}
    </BusinessResultRoot>
  );
};

export default ForecastItems;
