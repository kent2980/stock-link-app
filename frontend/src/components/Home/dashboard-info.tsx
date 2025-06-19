"use client";

import { InformationService, IxStockService } from "@/client";
import { Box, Card, HStack, Skeleton, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { ArrowDownIcon, ArrowUpIcon, FileText } from "lucide-react";
import { Suspense } from "react";

// Mock data - in a real app, this would come from an API
const MOCK_DATA = {
  totalReports: 12458,
  newReportsToday: 87,
  goodEarningsCount: 42,
  nikkeiAverage: {
    value: 38750.25,
    change: 325.48,
    percentChange: 0.85,
  },
  topix: {
    value: 2685.37,
    change: -12.64,
    percentChange: -0.47,
  },
};

export function DashboardInfo() {
  return (
    <Box>
      <Box maxW="container.xl" mx="auto" px={4}>
        {/* Stats grid */}
        <HStack gap={4}>
          {/* Nikkei Average */}
          <Card.Root>
            <Card.Body p={4}>
              <Box fontSize="sm" fontWeight="medium" color="gray.500">
                日経平均株価
              </Box>
              <Suspense fallback={<Skeleton height="30px" width="150px" />}>
                <NikkeiAverage />
              </Suspense>
            </Card.Body>
          </Card.Root>

          {/* New reports today */}
          <Card.Root>
            <Card.Body p={4}>
              <Box fontSize="sm" fontWeight="medium" color="gray.500">
                本日の新規報告書
              </Box>
              <Box mt={1} display="flex" alignItems="baseline">
                <Box fontSize="md" fontWeight="semibold" color="gray.900">
                  <Suspense fallback={<Skeleton height="20px" width="50px" />}>
                    <NewReportsToday />
                  </Suspense>
                </Box>
                <Box ml={2} fontSize="xs" color="gray.500">
                  件
                </Box>
              </Box>
              <Box mt={1}>
                <FileText style={{ height: 16, width: 16, color: "#059669" }} />
              </Box>
            </Card.Body>
          </Card.Root>

          {/* Date */}
          <Card.Root>
            <Card.Body
              display="flex"
              flexDirection="column"
              justifyContent="center"
              h="full"
              p={4}
            >
              <Box fontSize="sm" fontWeight="medium" color="gray.500">
                更新日時
              </Box>
              <Suspense fallback={<Skeleton height="30px" width="150px" />}>
                <InsertDate />
              </Suspense>
            </Card.Body>
          </Card.Root>
        </HStack>
      </Box>
    </Box>
  );
}

const NewReportsToday = () => {
  const { data } = useSuspenseQuery({
    queryKey: ["newReportsToday"],
    queryFn: async () => {
      return await InformationService.getDocumentCount({
        dateStr: new Date().toISOString().split("T")[0],
      });
    },
  });

  return <Text>{data}</Text>;
};

const InsertDate = () => {
  const { data } = useSuspenseQuery({
    queryKey: ["insertDate"],
    queryFn: async () => {
      return await InformationService.getUpdateTimestamp();
    },
  });

  const date = new Date(data);

  return (
    <>
      <Box mt={1} fontSize="sm" fontWeight="semibold" color="gray.900">
        {date.toLocaleDateString("ja-JP", {
          year: "numeric",
          month: "long",
          day: "numeric",
        })}
      </Box>
      <Box fontSize="sm" color="gray.500">
        {date.toLocaleTimeString("ja-JP", {
          hour: "2-digit",
          minute: "2-digit",
        })}
      </Box>
    </>
  );
};

const NikkeiAverage = () => {
  const { data } = useSuspenseQuery({
    queryKey: ["nikkeiAverage"],
    queryFn: async () => {
      return await IxStockService.getDailyStockPrice({
        stockCode: "^N225",
      });
    },
  });

  return (
    <>
      <Box mt={1} display="flex" alignItems="baseline">
        <Box fontSize="sm" fontWeight="semibold" color="gray.900">
          {data.close.toLocaleString()}
        </Box>
      </Box>
      <Box mt={1} display="flex" alignItems="center">
        {MOCK_DATA.nikkeiAverage.change > 0 ? (
          <Box display="flex" alignItems="center" color="emerald.600">
            <ArrowUpIcon style={{ marginRight: 4, height: 12, width: 12 }} />
            <Text fontSize="xs">
              {MOCK_DATA.nikkeiAverage.change.toLocaleString()} (
              {MOCK_DATA.nikkeiAverage.percentChange}%)
            </Text>
          </Box>
        ) : (
          <Box display="flex" alignItems="center" color="red.600">
            <ArrowDownIcon style={{ marginRight: 4, height: 12, width: 12 }} />
            <Text fontSize="xs">
              {Math.abs(MOCK_DATA.nikkeiAverage.change).toLocaleString()} (
              {Math.abs(MOCK_DATA.nikkeiAverage.percentChange)}%)
            </Text>
          </Box>
        )}
      </Box>
    </>
  );
};
