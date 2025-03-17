import { SummaryService } from "@/client";
import { useSuspenseQuery } from "@tanstack/react-query";
import { curValue, preValue } from "../../routes/_layout/store/- utils/utils";
import BusinessResultHeader from "./BusinessResultHeader";
import BusinessResultItems from "./BusinessResultItems";
import BusinessResultRoot from "./BusinessResultRoot";

interface OperatingResultItemsProps {
  head_item_key: string;
  value: string;
}

const OperatingResultItems: React.FC<OperatingResultItemsProps> = ({
  head_item_key,
  value,
}) => {
  const { data } = useSuspenseQuery({
    queryKey: ["BusinessPerformance", head_item_key],
    queryFn: async () => {
      return await SummaryService.getOperatingResults({
        headItemKey: head_item_key,
      });
    },
  });

  return (
    <BusinessResultRoot title="経営成績">
      <BusinessResultHeader preChange={true} />
      {data.data.map((items) =>
        items.result?.data?.map((item, key) => (
          <BusinessResultItems
            key={key}
            label={item.label}
            curChange={curValue(item, value)}
            preChange={preValue(item, value)}
          />
        ))
      )}
    </BusinessResultRoot>
  );
};

export default OperatingResultItems;
