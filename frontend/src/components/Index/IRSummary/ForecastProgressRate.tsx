import { SummaryService } from "@/client";
import { useSuspenseQuery } from "@tanstack/react-query";

interface ForecastProgressRateProps {
  head_item_key: string;
}

const ForecastProgressRate: React.FC<ForecastProgressRateProps> = ({
  head_item_key,
}) => {
  const { data } = useSuspenseQuery({
    queryKey: ["ForecastProgressRate", head_item_key],
    queryFn: async () => {
      return await SummaryService.getForecastProgressRate({
        headItemKey: head_item_key,
      });
    },
  });
  return (
    <div className="forecast-progress-rate">
      {data.forecast?.map((item, key) => (
        <div key={key}>
          <div>{item.label}</div>
          <div>{item.value}%</div>
        </div>
      ))}
    </div>
  );
};

export default ForecastProgressRate;
