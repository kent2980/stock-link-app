import { DocumentListPublic } from "@/client";
import { Box, BoxProps, Heading, Skeleton, VStack } from "@chakra-ui/react";
import React, { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";
import BusinessResult from "./Graphs/BusinessResult";
import Header from "./Header";
import BusinessResultTable from "./Tables/BusinessResultTable";
import DividendTable from "./Tables/DividendTable";
import ForecastTable from "./Tables/ForecastTable";

interface StockListItemProps extends BoxProps {
  item: DocumentListPublic;
}

const StockListItem: React.FC<StockListItemProps> = ({ item, ...props }) => {
  return (
    <Box
      className="stock-list-item"
      {...props}
      px={4}
      borderBottom="solid 1px"
      borderColor="gray.200"
      p={2}
    >
      <Header item={item} />
      <ErrorBoundary fallback={<Box>表示するデータがありません。</Box>}>
        <Suspense fallback={<Skeleton height="600px" width="100%" />}>
          {/* 経営成績 */}
          <Heading as="h3" fontSize="md" fontWeight="bold">
            経営成績
          </Heading>
          <VStack gap={3}>
            <BusinessResult headItemKey={item.head_item_key} />
            <BusinessResultTable HeadItemKey={item.head_item_key} />
          </VStack>
          {/* 業績予想 */}
          <Heading as="h3" fontSize="md" fontWeight="bold">
            業績予想
          </Heading>
          <ForecastTable HeadItemKey={item.head_item_key} />
          {/* 配当 */}
          <Heading as="h3" fontSize="md" fontWeight="bold">
            配当
          </Heading>
          <DividendTable HeadItemKey={item.head_item_key} />
        </Suspense>
      </ErrorBoundary>
    </Box>
  );
};

export default StockListItem;
