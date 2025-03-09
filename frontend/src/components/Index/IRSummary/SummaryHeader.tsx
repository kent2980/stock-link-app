import { DocumentListPublic } from "@/client";
import { Box, Flex, Text } from "@chakra-ui/react";
import {
  differenceInDays,
  differenceInHours,
  format,
  parseISO,
} from "date-fns";
import { ja } from "date-fns/locale";

interface SummaryHeaderProps {
  item: DocumentListPublic;
}

const SummaryHeader: React.FC<SummaryHeaderProps> = ({ item }) => {
  const date_str = item.insert_date; // 日付の取得
  const date = parseISO(date_str); // 日付のパース
  const today = new Date(); // 今日の日付
  const diff = differenceInDays(today, date); // 日付の差分
  const diff_hour = differenceInHours(today, date); // 時間の差分
  const japanDate_str = format(date, "yyyy.MM.dd", {
    // 日本の日付フォーマット
    locale: ja,
  });
  return (
    <Flex gap={4} direction="row" w="100%">
      {/* 投稿日 */}
      <Box color="gray.500">
        {diff < 1 && <Text>{diff_hour}時間前</Text>}
        {diff >= 1 && 7 >= diff && <Text>{diff}日前</Text>}
        {diff > 7 && <Text>{japanDate_str}</Text>}
      </Box>
      {/* 銘柄コード */}
      <Box>
        <Text>{item.securities_code}</Text>
      </Box>
      {/* 銘柄名 */}
      <Box>
        <Text>{item.company_name}</Text>
      </Box>
      {/* 報告書タイトル */}
      <Box>
        <Text>{item.document_short_name}</Text>
      </Box>
    </Flex>
  );
};

export default SummaryHeader;
