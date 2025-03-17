import { SummaryService } from "@/client";
import { useSuspenseQueries } from "@tanstack/react-query";
import { curValue } from "../../routes/_layout/store/- utils/utils";
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

  const getSelectRate = (period: string, item_name: string) => {};

  return (
    <BusinessResultRoot title="業績予想">
      <BusinessResultHeader />
      {data1.data.data.map((items) =>
        items.forecast?.data?.map((item, key) => (
          <BusinessResultItems
            key={key}
            label={item.label}
            curChange={curValue(item, value)}
          />
        ))
      )}
    </BusinessResultRoot>
  );
};

export default ForecastItems;
