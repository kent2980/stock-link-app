import { DisclosureItem } from "@/client";
import { Badge, Box, Flex, HStack, Text } from "@chakra-ui/react";

export interface StockCardProps {
  item: DisclosureItem;
}

const StockCard: React.FC<StockCardProps> = ({ item }) => {
  const ope = item.operating_result;
  const forecast = item.forecast;
  const currentProfitIndex = ope?.data?.findIndex((data) =>
    /.*当期純利益$|当期利益/.test(data.label ?? "")
  );
  const formatPercent = (value: number | null | undefined) => {
    if (typeof value === "number") {
      if (value === 0) return "0%";
      if (value < 0)
        return (
          <Badge colorPalette="red" variant="solid" px={1}>
            -{Math.abs(value)}%
          </Badge>
        );
      return (
        <Badge colorPalette="green" variant="solid" px={1}>
          +{Math.abs(value)}%
        </Badge>
      );
    }
    return "-";
  };
  const filOpeResult = ope?.data?.[currentProfitIndex ?? 0 + 1]?.result;
  const filForecastResult =
    forecast?.data?.[currentProfitIndex ?? 0 + 1]?.forecast;
  return (
    <Box px={2} borderBottom="0.5px solid" borderColor="#545458">
      <HStack pt={5} pb={3} gap={4}>
        {/* 銘柄コード */}
        <Box bg="#4eec88" color="black" rounded={10} p={1.5} fontWeight={600}>
          <Text>{item.code}</Text>
        </Box>
        {/* 会社名・銘柄情報 */}
        <Box w={{ base: "40vw", md: "300px" }}>
          <Text fontWeight={600} fontSize="13px">
            {item.company.replace(/株式会社|有限会社/g, "")}
          </Text>
          <Text fontSize="12px" color="#b8b8b8">
            {item.category}
          </Text>
        </Box>
        {/* 実績EPS伸び率 */}
        <Box flex="1" textAlign="center">
          {formatPercent(filOpeResult?.curChange?.value)}
        </Box>
        {/* 予想EPS伸び率 */}
        <Box flex="1" textAlign="center">
          {formatPercent(filForecastResult?.curChange?.value)}
        </Box>
      </HStack>
      <Flex direction="row" justify="flex-end" px={2} py={1}>
        {/* 更新日時 */}
        <Text fontSize="11px" color="#b8b8b8">
          {new Date(item.insert_date).toLocaleString("ja-JP", {
            year: "numeric",
            month: "2-digit",
            day: "2-digit",
            hour: "2-digit",
            minute: "2-digit",
          })}
        </Text>
      </Flex>
    </Box>
  );
};

export default StockCard;
