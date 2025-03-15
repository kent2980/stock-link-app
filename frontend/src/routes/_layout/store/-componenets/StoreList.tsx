import { IxService } from "@/client";
import { HeaderStore } from "@/Store/HeaderStore";
import { Box, Flex, List, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useVirtualizer } from "@tanstack/react-virtual";
import React, { Suspense, useEffect, useRef } from "react";
import { ErrorBoundary } from "react-error-boundary";
import FinancialSummary from "./FinancialSummary";
import Header from "./Header";
import StockWiki from "./StockWiki";

interface StoreListProps {}

export const StoreList: React.FC<StoreListProps> = () => {
  const { data } = useSuspenseQuery({
    queryKey: ["store"],
    queryFn: async () => {
      return await IxService.getDocumentList();
    },
  });
  const parentRef = useRef<Element | null>(null);

  const rowVirtualizer = useVirtualizer({
    count: data.count,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 1400,
    overscan: 3,
  });

  useEffect(() => {
    const handleScroll = (event: Event) => {
      const target = event.target as HTMLElement;
      console.log("Scroll position:", target.scrollTop);
      if (59 < target.scrollTop) {
        HeaderStore.setState((state) => ({
          ...state,
          height: 0,
        }));
        // id="header"の要素を取得
        const header = document.getElementById("header");
        // headerのdisplayをnoneにする
        if (header) {
          header.style.display = "none";
        }
      }
      if (target.scrollTop < 59) {
        HeaderStore.setState((state) => ({
          ...state,
          height: 59,
        }));
        const header = document.getElementById("header");
        if (header) {
          header.style.display = "block";
        }
      }
    };

    const scrollElement = parentRef.current;
    if (scrollElement) {
      scrollElement.addEventListener("scroll", handleScroll);
    }

    return () => {
      if (scrollElement) {
        scrollElement.removeEventListener("scroll", handleScroll);
      }
    };
  }, []);
  return (
    <>
      <Box ref={parentRef} w="100%" overflow="auto" height="100vh">
        <List.Root
          height={`${rowVirtualizer.getTotalSize()}px`}
          w="100%"
          position="relative"
          bg="white"
          fontSize={{ base: 12, md: 16 }}
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
                <Box>
                  <Flex
                    direction="column"
                    gap={3}
                    w="100%"
                    p={6}
                    justifyContent="center"
                    alignItems="center"
                  >
                    <Header item={item} />

                    <Suspense fallback={<Box>Loading...</Box>}>
                      <ErrorBoundary
                        FallbackComponent={({ error }) => (
                          <Box
                            bg="gray.100"
                            p={2}
                            borderRadius={8}
                            minW={{ base: "100%", md: "60%" }}
                            minH="60px"
                            boxShadow="md"
                            textAlign="center"
                            display="flex"
                            alignItems="center"
                            justifyContent="center"
                          >
                            <Text color="red.500">
                              企業概要が存在しません: {error.message}
                            </Text>
                          </Box>
                        )}
                      >
                        <StockWiki code={item.securities_code} />
                      </ErrorBoundary>
                    </Suspense>
                  </Flex>
                  <Flex direction="column" gap={5} p={2} alignItems="center">
                    {item.report_type.startsWith("ed") ? (
                      <FinancialSummary item={item} />
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
