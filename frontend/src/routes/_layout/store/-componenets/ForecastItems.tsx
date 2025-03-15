import { SummaryService } from "@/client";
import { Card, Flex, Heading } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { shortBusinessValue } from "../- utils/utils";
import BusinessResultItems from "./BusinessResultItems";
import BusinessResultRoot from "./BusinessResultRoot";

interface ForecastItemsProps {
  head_item_key: string;
}

const ForecastItems: React.FC<ForecastItemsProps> = ({ head_item_key }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["ForecastItems", head_item_key],
    queryFn: async () => {
      return await SummaryService.getForecasts({
        headItemKey: head_item_key,
      });
    },
  });

  return (
    <Card.Root>
      <Card.Body>
        <Flex direction="column" gap={1}>
          <Heading size="md">業績予想</Heading>
          <BusinessResultRoot>
            {data.data.map((items) =>
              items.forecast?.data?.map((item, key) => (
                <BusinessResultItems
                  key={key}
                  label={item.label}
                  curChange={shortBusinessValue(item.curChange?.value)}
                  preChange={shortBusinessValue(item.preChange?.value)}
                />
              ))
            )}
          </BusinessResultRoot>
        </Flex>
      </Card.Body>
    </Card.Root>
  );
};

export default ForecastItems;
