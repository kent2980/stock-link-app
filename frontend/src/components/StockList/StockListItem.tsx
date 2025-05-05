import { DocumentListPublic } from "@/client";
import { Box, BoxProps, Heading, Skeleton } from "@chakra-ui/react";
import React, { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";
import BusinessResult from "./Graphs/BusinessResult";
import Header from "./Header";
import BusinessResultTable from "./Tables/BusinessResultTable";
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
      {/* 経営成績 */}
      <Heading as="h3" fontSize="md" fontWeight="bold">
        経営成績
      </Heading>
      <ErrorBoundary fallback={<Box>表示するデータがありません。</Box>}>
        <Suspense fallback={<Skeleton height="300px" width="100%" />}>
          <BusinessResult headItemKey={item.head_item_key} />
          <BusinessResultTable HeadItemKey={item.head_item_key} />
        </Suspense>
      </ErrorBoundary>
      {/* 業績予想 */}
      <Heading as="h3" fontSize="md" fontWeight="bold">
        業績予想
      </Heading>
      <ErrorBoundary fallback={<Box>表示するデータがありません。</Box>}>
        <Suspense fallback={<Skeleton height="150px" width="100%" />}>
          <ForecastTable HeadItemKey={item.head_item_key} />
        </Suspense>
      </ErrorBoundary>
    </Box>
  );
};

export default StockListItem;
