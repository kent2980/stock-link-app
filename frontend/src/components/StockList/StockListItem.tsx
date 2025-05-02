import { DocumentListPublic } from "@/client";
import { Box, BoxProps, Skeleton } from "@chakra-ui/react";
import React, { Suspense } from "react";
import BusinessResult from "./Graphs/BusinessResult";
import Header from "./Header";
import ForecastTable from "./Tables/ForecastTable";

interface StockListItemProps extends BoxProps {
  item: DocumentListPublic;
}

const StockListItem: React.FC<StockListItemProps> = ({ item, ...props }) => {
  return (
    <Box
      {...props}
      px={4}
      borderBottom="solid 1px"
      borderColor="gray.200"
      p={2}
    >
      <Header item={item} />
      <Suspense fallback={<Skeleton height="150px" width="100%" />}>
        <BusinessResult headItemKey={item.head_item_key} />
      </Suspense>
      <Suspense fallback={<Skeleton height="150px" width="100%" />}>
        <ForecastTable HeadItemKey={item.head_item_key} />
      </Suspense>
    </Box>
  );
};

export default StockListItem;
