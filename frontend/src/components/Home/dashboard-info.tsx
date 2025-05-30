"use client";

import { InformationService, IxStockService } from "@/client";
import { Box, Card, Flex, Skeleton, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import {
  ArrowDownIcon,
  ArrowUpIcon,
  BarChart3,
  FileText,
  TrendingUp,
} from "lucide-react";
import { Suspense, useEffect, useState } from "react";

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
  todaysHeadlines: [
    "トヨタ自動車、第2四半期営業利益が予想を上回る",
    "ソニーグループ、半導体部門の好調で通期見通しを上方修正",
    "任天堂、新型ゲーム機の発売を来年に延期と発表",
    "三菱UFJ、デジタル戦略強化で収益増加",
    "ソフトバンクグループ、AI投資で大幅増益",
  ],
};

export function DashboardInfo() {
  const [currentHeadline, setCurrentHeadline] = useState(0);

  // Rotate through headlines
  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentHeadline(
        (prev) => (prev + 1) % MOCK_DATA.todaysHeadlines.length
      );
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <Box>
      <Box maxW="container.xl" mx="auto" px={4}>
        {/* Headline ticker */}
        <Box mb={6} overflow="hidden" rounded="lg" bg="green.50" p={4}>
          <Box display="flex" alignItems="center">
            <BarChart3
              style={{
                marginRight: 12,
                height: 20,
                width: 20,
                color: "#059669",
              }}
            />
            <Box overflow="hidden">
              <Flex
                direction="row"
                whiteSpace={{ base: "normal", md: "nowrap" }}
                color="green.800"
                h={10}
                alignItems="center"
              >
                <Text as="span" fontWeight="medium">
                  {MOCK_DATA.todaysHeadlines[currentHeadline]}
                </Text>
              </Flex>
            </Box>
          </Box>
        </Box>

        {/* Stats grid */}
        <Box
          display="grid"
          gridTemplateColumns={{
            base: "repeat(2, 1fr)",
            md: "repeat(3, 1fr)",
            lg: "repeat(6, 1fr)",
          }}
          gap={4}
        >
          {/* Total reports */}
          <Card.Root>
            <Card.Body p={4}>
              <Box fontSize="sm" fontWeight="medium" color="gray.500">
                全報告書件数
              </Box>
              <Box mt={1} display="flex" alignItems="baseline">
                <Box fontSize="2xl" fontWeight="semibold" color="gray.900">
                  <Suspense fallback={<Skeleton height="20px" width="50px" />}>
                    <TotalReports />
                  </Suspense>
                </Box>
                <Box ml={2} fontSize="xs" color="gray.500">
                  件
                </Box>
              </Box>
              <Box mt={1}>
                <FileText style={{ height: 16, width: 16, color: "#9CA3AF" }} />
              </Box>
            </Card.Body>
          </Card.Root>

          {/* New reports today */}
          <Card.Root>
            <Card.Body p={4}>
              <Box fontSize="sm" fontWeight="medium" color="gray.500">
                本日の新規報告書
              </Box>
              <Box mt={1} display="flex" alignItems="baseline">
                <Box fontSize="2xl" fontWeight="semibold" color="gray.900">
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

          {/* Good earnings count */}
          <Card.Root>
            <Card.Body p={4}>
              <Box fontSize="sm" fontWeight="medium" color="gray.500">
                好決算件数
              </Box>
              <Box mt={1} display="flex" alignItems="baseline">
                <Box fontSize="2xl" fontWeight="semibold" color="emerald.600">
                  {MOCK_DATA.goodEarningsCount.toLocaleString()}
                </Box>
                <Box ml={2} fontSize="xs" color="gray.500">
                  件
                </Box>
              </Box>
              <Box mt={1}>
                <TrendingUp
                  style={{ height: 16, width: 16, color: "#059669" }}
                />
              </Box>
            </Card.Body>
          </Card.Root>

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

          {/* TOPIX */}
          <Card.Root>
            <Card.Body p={4}>
              <Box fontSize="sm" fontWeight="medium" color="gray.500">
                TOPIX
              </Box>
              <Box mt={1} display="flex" alignItems="baseline">
                <Box fontSize="2xl" fontWeight="semibold" color="gray.900">
                  {MOCK_DATA.topix.value.toLocaleString()}
                </Box>
              </Box>
              <Box mt={1} display="flex" alignItems="center">
                {MOCK_DATA.topix.change > 0 ? (
                  <Box display="flex" alignItems="center" color="emerald.600">
                    <ArrowUpIcon
                      style={{ marginRight: 4, height: 12, width: 12 }}
                    />
                    <Text fontSize="xs">
                      {MOCK_DATA.topix.change.toLocaleString()} (
                      {MOCK_DATA.topix.percentChange}%)
                    </Text>
                  </Box>
                ) : (
                  <Box display="flex" alignItems="center" color="red.600">
                    <ArrowDownIcon
                      style={{ marginRight: 4, height: 12, width: 12 }}
                    />
                    <Text fontSize="xs">
                      {Math.abs(MOCK_DATA.topix.change).toLocaleString()} (
                      {Math.abs(MOCK_DATA.topix.percentChange)}%)
                    </Text>
                  </Box>
                )}
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
        </Box>
      </Box>
    </Box>
  );
}

const TotalReports = () => {
  const { data } = useSuspenseQuery({
    queryKey: ["totalReports"],
    queryFn: async () => {
      return await InformationService.getDocumentCount();
    },
  });

  return <Text>{data}</Text>;
};

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
      <Box mt={1} fontSize="lg" fontWeight="semibold" color="gray.900">
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
        <Box fontSize="2xl" fontWeight="semibold" color="gray.900">
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
