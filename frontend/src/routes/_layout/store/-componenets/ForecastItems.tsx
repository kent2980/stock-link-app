import { SummaryService } from "@/client";
import { useSuspenseQuery } from "@tanstack/react-query";
import { curValue } from "../- utils/utils";
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
  const { data } = useSuspenseQuery({
    queryKey: ["ForecastItems", head_item_key],
    queryFn: async () => {
      return await SummaryService.getForecasts({
        headItemKey: head_item_key,
      });
    },
  });

  return (
    <BusinessResultRoot title="業績予想">
      <BusinessResultHeader />
      {data.data.map((items) =>
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
