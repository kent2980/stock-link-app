import { DocumentListPublic } from "@/client";
import { Box, BoxProps, Skeleton } from "@chakra-ui/react";
import React, { Suspense } from "react";
import BusinessResult from "./DataDisplay/BusinessResult";
import Header from "./Header";

interface StockListItemProps extends BoxProps {
  item: DocumentListPublic;
}

const StockListItem: React.FC<StockListItemProps> = ({ item, ...props }) => {
  const { company_name, securities_code, head_item_key, current_period } = item;
  const title = () => {
    if (current_period === "Q1") {
      return "第1四半期決算";
    } else if (current_period === "Q2") {
      return "第2四半期決算";
    } else if (current_period === "Q3") {
      return "第3四半期決算";
    } else if (current_period === "FY") {
      return "通期決算";
    } else if (current_period === "HY") {
      return "中間決算";
    }
  };
  return (
    <Box {...props} px={4}>
      <Header item={item} />
      <Suspense fallback={<Skeleton height="20px" width="100%" />}>
        <BusinessResult headItemKey={item.head_item_key} />
      </Suspense>
    </Box>
  );
};

export default StockListItem;
