import { DisclosureItem } from "@/client";
import { Box, HStack, Text } from "@chakra-ui/react";

export interface StockCardProps {
  item: DisclosureItem;
}

const StockCard: React.FC<StockCardProps> = ({ item }) => {
  const ope = item.operating_result;
  const forecast = item.forecast;
  const currentProfitIndex = ope?.data?.findIndex((data) =>
    /.*当期純利益$|当期利益/.test(data.label ?? "")
  );
  return (
    <Box py={5} px={2} borderBottom="0.5px solid" borderColor="#545458">
      <HStack gap={4}>
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
          {typeof ope?.data?.[currentProfitIndex ?? 0 + 1]?.result?.curChange
            ?.value === "number"
            ? `${ope.data[currentProfitIndex ?? 0 + 1].result?.curChange?.value}%`
            : "-"}
        </Box>
        {/* 予想EPS伸び率 */}
        <Box flex="1" textAlign="center">
          {typeof forecast?.data?.[currentProfitIndex ?? 0 + 1]?.forecast
            ?.curChange?.value === "number"
            ? `${forecast.data[currentProfitIndex ?? 0 + 1].forecast?.curChange?.value}%`
            : "-"}
        </Box>
      </HStack>
    </Box>
  );
};

export default StockCard;
