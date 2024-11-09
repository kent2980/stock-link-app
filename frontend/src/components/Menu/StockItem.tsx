import {
  Badge,
  Box,
  Heading,
  Highlight,
  HStack,
  Table,
  Td,
  Text,
  Th,
  Thead,
  Tr,
  VStack,
} from "@chakra-ui/react";
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
  const isDividendRevision = () => {
    if (item.is_div_rev) {
      return (
        <Text>
          <Highlight
            query="有"
            styles={{
              px: "2",
              py: "1",
              rounded: "md",
              bg: "red.400",
              color: "white",
            }}
          >
            有
          </Highlight>
        </Text>
      );
    } else {
      return <Text textAlign="center">無</Text>;
    }
  };
  const dividendIncreaseRate = item.div_inc_rt; // 配当増加率
  const isEarningsForecastRevision = () => {
    if (item.is_fcst_rev) {
      return (
        <Text>
          <Highlight
            query="有"
            styles={{
              px: "2",
              py: "1",
              rounded: "md",
              bg: "red.400",
              color: "white",
            }}
          >
            有
          </Highlight>
        </Text>
      );
    } else {
      return <Text textAlign="center">無</Text>;
    }
  };
  const forecastOrdinaryIncomeGrowthRate = item.fcst_oi_gr_rt; // 営業利益増加率
  return (
    <VStack m={2} w="100%" spacing={5}>
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
      <HStack>
        {item.report_type?.startsWith("ed") ? (
          <Table variant={"simple"} size="sm">
            <Thead>
              <Tr>
                <Th>項目</Th>
                <Th>修正</Th>
                <Th>前回</Th>
                <Th>修正値</Th>
                <Th>増減</Th>
              </Tr>
            </Thead>
            <Tr>
              <Th>配当予想の修正</Th>
              <Td>{isDividendRevision()}</Td>
              <Td></Td>
              <Td></Td>
              <Td>{dividendIncreaseRate}</Td>
            </Tr>
            <Tr>
              <Th>経常利益の修正</Th>
              <Td>{isEarningsForecastRevision()}</Td>
              <Td></Td>
              <Td></Td>
              <Td>{forecastOrdinaryIncomeGrowthRate}</Td>
            </Tr>
          </Table>
        ) : null}
      </HStack>
    </VStack>
  );
};

export default StockItem;
