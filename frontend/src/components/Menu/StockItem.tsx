import { Badge, Box, Heading, HStack, Text, VStack } from "@chakra-ui/react";
import dayjs from "dayjs";
import { IxHeadTitlePublic } from "../../client";

interface StockItemProps {
  item: IxHeadTitlePublic;
}

/**
 * StockItemコンポーネントは、株式リストの各項目を表示します。
 *
 * @component
 * @example
 * <StockItem item={item} />
 *
 * @param {StockItemProps} props - プロパティの情報を持つオブジェクト
 * @param {IxHeadTitlePublic} props.item - 株式リストの各種情報を持つオブジェクト
 *
 * @returns {React.FC<StockItemProps>} 株式リストの各項目を表示するコンポーネント
 */
const StockItem: React.FC<StockItemProps> = ({ item }) => {
  const code = item.securities_code; // 銘柄コード
  const name = item.company_name; // 企業名
  const report_type = () => {
    if (item?.report_type?.startsWith("ed")) {
      return "決算短信";
    } else if (item?.report_type === "rvfc") {
      return "業績予想の修正";
    } else if (item?.report_type === "rvdf") {
      return "配当予想の修正";
    }
    return "";
  };
  const period = () => {
    if (item?.current_period == "Q1") {
      return "第1四半期";
    } else if (item?.current_period == "Q2") {
      return "第2四半期";
    } else if (item?.current_period == "Q3") {
      return "第3四半期";
    }
    return "";
  };
  const year = item.fy_year_end; // 決算期
  return (
    <VStack m={2} w="100%" spacing={5} height="600px">
      <HStack justify="flex-start" w="100%">
        <Box>
          <Text px="2" py="1" rounded="10%" bg="gray.200" color="black">
            {code}
          </Text>
        </Box>
        <Box>
          <Heading
            as="h2"
            size="sm"
            borderBottom="4px solid"
            borderRadius="sm"
            borderBottomColor="gray.300"
          >
            {name}
          </Heading>
        </Box>
      </HStack>
      <HStack justify="flex-start" w="100%">
        <Badge>{dayjs(year).format("YYYY年M月期")}</Badge>
        <Badge display={period() === "" ? "none" : "block"}>{period()}</Badge>
        <Badge>{report_type()}</Badge>
      </HStack>
    </VStack>
  );
};

export default StockItem;
