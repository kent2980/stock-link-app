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
      display="flex"
      flexDirection="column"
      className="stock-list-item"
      {...props}
      px={4}
      borderBottom="solid 1px"
      borderColor="gray.200"
      p={2}
      gap={2}
    >
      <Header item={item} />
      <Suspense fallback={<Skeleton height="600px" width="100%" />}>
        {/* 経営成績 */}
        <Heading as="h3" fontSize="md" fontWeight="bold">
          経営成績
        </Heading>
        <VStack gap={2}>
          <ErrorBoundary
            FallbackComponent={() => <Box>データが見つかりません。</Box>}
          >
            <BusinessResult headItemKey={item.head_item_key} />
          </ErrorBoundary>
          <ErrorBoundary
            FallbackComponent={() => <Box>データが見つかりません。</Box>}
          >
            <BusinessResultTable HeadItemKey={item.head_item_key} />
          </ErrorBoundary>
        </VStack>
        {/* 業績予想 */}
        <Heading as="h3" fontSize="md" fontWeight="bold">
          業績予想
        </Heading>
        <ErrorBoundary
          FallbackComponent={() => <Box>データが見つかりません。</Box>}
        >
          <ForecastTable HeadItemKey={item.head_item_key} />
        </ErrorBoundary>
        {/* 配当 */}
        <Heading as="h3" fontSize="md" fontWeight="bold">
          配当
        </Heading>
        <ErrorBoundary
          FallbackComponent={() => <Box>データが見つかりません。</Box>}
        >
          <DividendTable HeadItemKey={item.head_item_key} />
        </ErrorBoundary>
      </Suspense>
    </Box>
  );
};

export default StockListItem;
