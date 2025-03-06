import { IxService, SummaryService } from "@/client";
import { HeaderStore } from "@/Store/HeaderStore";
import { Box, Separator } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import { useVirtualizer } from "@tanstack/react-virtual";
import { Suspense, useRef } from "react";
export const Route = createFileRoute("/_layout/virtual")({
  component: VirtualParent,
});

function VirtualParent() {
  return (
    <Box>
      <Suspense fallback={<div>Loading...</div>}>
        <Virtual />
      </Suspense>
    </Box>
  );
}

function Virtual() {
  const { data } = useSuspenseQuery({
    queryKey: ["virtual"],
    queryFn: async () => {
      return IxService.getDocumentList({});
    },
  });

  const { height } = useStore(HeaderStore, (state) => state);

  const parentRef = useRef<Element | null>(null);

  const rowVirtualizer = useVirtualizer({
    count: data.count,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 500,
    overscan: 5,
  });

  return (
    <Box>
      <Box ref={parentRef} overflow="auto" height={`calc(100vh - ${height}px)`}>
        <Box
          h={`${rowVirtualizer.getTotalSize()}px`}
          w="100%"
          position="relative"
          maxW="calc(100vw - 250px)" // サイドバーの幅を考慮して最大幅を設定
          m="auto" // 中央に配置
        >
          {rowVirtualizer.getVirtualItems().map((virtualRow) => (
            <Box
              key={virtualRow.index}
              position="absolute"
              top={virtualRow.start}
              left={0}
              width="100%"
              height={virtualRow.size}
              display="flex"
              border="1px solid"
              borderColor="gray.200"
              bg={virtualRow.index % 2 === 0 ? "gray.50" : "white"}
              _hover={{
                bg: "gray.100",
              }}
            >
              {data.data[virtualRow.index].securities_code}
              <Separator
                borderColor="#e41a1a"
                border="1px solid"
                height={4}
                orientation="vertical"
              />
              {data.data[virtualRow.index].company_name}
              <Suspense fallback={<div>Loading...</div>}>
                <TestData code={data.data[virtualRow.index].securities_code} />
              </Suspense>
            </Box>
          ))}
        </Box>
      </Box>
    </Box>
  );
}

interface TestDataProps {
  code: string;
}

function TestData({ code }: TestDataProps) {
  const { data } = useSuspenseQuery({
    queryKey: ["testData", code],
    queryFn: async () => {
      return SummaryService.getOperatingResults({
        code: code,
      });
    },
  });
  return (
    <Box>
      {data.data.map((item) =>
        item.result?.data?.map((result, key) => (
          <Box key={key}>
            {result.label}
            {result.value?.value}
          </Box>
        ))
      )}
    </Box>
  );
}
