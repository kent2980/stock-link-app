import { IxService } from "@/client";
import { Box, Flex, List, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useVirtualizer } from "@tanstack/react-virtual";
import React, { Suspense, useRef } from "react";
import { ErrorBoundary } from "react-error-boundary";
import ForecastItems from "./ForecastItems";
import Header from "./Header";
import OperatingResultItems from "./OperatingResultItems";
import StockWiki from "./StockWiki";

interface StoreListProps {}

export const StoreList: React.FC<StoreListProps> = () => {
  const { data } = useSuspenseQuery({
    queryKey: ["store"],
    queryFn: async () => {
      return await IxService.getDocumentList();
    },
  });
  const parentRef = useRef<HTMLDivElement>(null);

  console.log(window.innerWidth);
  const size = () => {
    if (window.innerWidth < 768) {
      return 1200;
    }
    return 800;
  };
  const rowVirtualizer = useVirtualizer({
    count: data.count,
    getScrollElement: () => parentRef.current,
    estimateSize: () => size(),
    overscan: 5,
  });

  return (
    <>
      <Box ref={parentRef} w="100%">
        <List.Root
          height={`${rowVirtualizer.getTotalSize()}px`}
          w="100%"
          position="relative"
          bg="white"
        >
          {rowVirtualizer.getVirtualItems().map((virtualRow) => {
            const item = data.data[virtualRow.index];
            return (
              <List.Item
                key={virtualRow.index}
                height={`${virtualRow.size}px`}
                position="absolute"
                top={0}
                left={0}
                right={0}
                transform={`translateY(${virtualRow.start}px)`}
                // リストの点を削除
                listStyleType="none"
                p={4}
                borderBottom="1px solid"
                borderColor="gray.200"
              >
                <Box
                  display={{ base: "box", md: "flex" }}
                  direction={{ base: "column", md: "row" }}
                  gap={2}
                  justifyContent={{ base: "center", md: "flex-start" }}
                  alignItems={{ base: "center", md: "flex-start" }}
                >
                  <Flex
                    direction="column"
                    gap={3}
                    w={{ base: "100%", md: "35%" }}
                    p={6}
                    justifyContent={{ base: "center", md: "flex-start" }}
                    alignItems={{ base: "center", md: "flex-start" }}
                  >
                    <Header item={item} />
                    <ErrorBoundary
                      FallbackComponent={({ error }) => (
                        <Text>企業概要が存在しません</Text>
                      )}
                    >
                      <Suspense fallback={<Box>Loading...</Box>}>
                        <StockWiki code={item.securities_code} />
                      </Suspense>
                    </ErrorBoundary>
                  </Flex>
                  <Flex direction="column" gap={5} p={2}>
                    {item.report_type.startsWith("ed") ? (
                      <>
                        <Text textAlign="center" w="100%">
                          {item.document_short_name}
                        </Text>
                        <Text textAlign="center" color="gray.700" fontSize={12}>
                          ※()内は昨年度の増減率です。
                        </Text>
                        <Suspense fallback={<Box>Loading...</Box>}>
                          <OperatingResultItems
                            head_item_key={item.head_item_key}
                          />
                        </Suspense>
                        <Suspense fallback={<Box>Loading...</Box>}>
                          <ForecastItems head_item_key={item.head_item_key} />
                        </Suspense>
                      </>
                    ) : (
                      <Text fontSize={10} color="gray.700">
                        {item.report_type}
                      </Text>
                    )}
                  </Flex>
                </Box>
              </List.Item>
            );
          })}
        </List.Root>
      </Box>
    </>
  );
};

export default StoreList;
