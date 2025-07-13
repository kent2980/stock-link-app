import { DisclosureItem, FinValueFinance } from "@/client";
import {
  Box,
  Flex,
  Heading,
  Table,
  TableCellProps,
  TableColumnHeaderProps,
  TableRowProps,
} from "@chakra-ui/react";
import React from "react";
import { DarkMode, useColorModeValue } from "../ui/color-mode";

/**
 * 指定されたラベル文字列から、正規表現リストに一致する部分文字列を空白に置換して返します。
 *
 * @param label - 変換対象となるラベル文字列
 * @returns 正規表現に一致する部分が除去されたラベル文字列
 */
const ShortLabel = (label: string) => {
  // 正規表現のリストを定義
  const regexList = ["親会社株主に帰属する"];
  // 正規表現を作成
  const regex = new RegExp(regexList.join("|"), "g");
  // 正規表現にマッチする部分を空白に置換
  const replacedLabel = label.replace(regex, "");
  // 置換後の文字列を返す
  return replacedLabel;
};

interface StockInfoProps {
  item: DisclosureItem | null;
}

const StockInfo: React.FC<StockInfoProps> = ({ item }) => {
  return (
    <Flex direction="column" maxW="100%" overflowX="hidden" p={2} gap={2}>
      {/* 経営成績テーブル */}
      <OperatingTable item={item} />
      {/* 業績予想テーブル */}
      <ForecastTable item={item} />
    </Flex>
  );
};

export default StockInfo;

const CustomTableRow: React.FC<TableRowProps> = ({ children, ...props }) => {
  /**
   * 背景色の設定値
   */
  const bg = useColorModeValue("#272429", "white");
  return (
    <Table.Row
      {...props}
      bg={bg}
      _hover={{ bg: useColorModeValue("gray.100", "gray.700") }}
      _focus={{ boxShadow: "outline" }}
    >
      {children}
    </Table.Row>
  );
};

const CustomTableColumnHeader: React.FC<TableColumnHeaderProps> = ({
  children,
  ...props
}) => {
  /**
   * ボーダー色の設定値
   */
  const borderColor = useColorModeValue("gray.600", "gray.400");
  return (
    <Table.ColumnHeader
      {...props}
      py={0}
      borderBottom="1px solid"
      borderColor={borderColor}
    >
      {children}
    </Table.ColumnHeader>
  );
};

const CustomTableCell: React.FC<TableCellProps> = ({ children, ...props }) => {
  /**
   * ボーダー色の設定値
   */
  const borderColor = useColorModeValue("gray.600", "gray.400");
  return (
    <Table.Cell
      {...props}
      py={0}
      borderBottom="1px solid"
      borderColor={borderColor}
    >
      {children}
    </Table.Cell>
  );
};

const OperatingTable: React.FC<StockInfoProps> = ({ item }) => {
  if (item == null) {
    return <Box>No data available</Box>;
  }

  const ope = item.operating_result;

  /**
   * 2025-07-13形式の文字列から１年前のの日付文字列を生成します。
   * @param dateStr 日付文字列
   * @returns １年前の日付文字列
   */
  const PreviewFiscalYear = (dateStr: string) => {
    const dateObj = new Date(dateStr);
    dateObj.setFullYear(dateObj.getFullYear() - 1);
    // フォーマットを維持して返す（例: 2024-07-13）
    const year = dateObj.getFullYear();
    const month = String(dateObj.getMonth() + 1).padStart(2, "0");
    const day = String(dateObj.getDate()).padStart(2, "0");
    return `${year}-${month}-${day}`;
  };

  /**
   * 日付文字列と会計期間から[2025年3月期通期]を生成します。
   * @param dateStr 日付文字列
   * @param period 会計期間(例Q1,FY1など)
   */
  const formatPeriodText = (dateStr: string, period: string) => {
    const dateObj = new Date(dateStr);
    const year = String(dateObj.getFullYear()).slice(-2); // 2桁表記
    const month = dateObj.getMonth() + 1;
    let periodText = "";

    switch (period) {
      case "通期":
      case "FY":
        periodText = `${year}.${month}-通期`;
        break;
      case "Q1":
        periodText = `${year}.${month}-Q1`;
        break;
      case "Q2":
        periodText = `${year}.${month}-Q2`;
        break;
      case "Q3":
        periodText = `${year}.${month}-Q3`;
        break;
      case "HY":
        periodText = `${year}.${month}-中間`;
        break;
      default:
        periodText = `${year}.${month}月期${period}`;
        break;
    }
    return periodText;
  };

  const SliceOpeItems = (items: FinValueFinance[]) => {
    const regex = /.*当期利益$|.*当期純利益$/;
    const index = items.findIndex(
      (item) => item.label && regex.test(item.label)
    );
    if (index !== -1) {
      return items.slice(0, index + 1);
    }
    return items;
  };
  return (
    <Flex direction="column" gap={1} id="OperatingTable">
      <Heading as={"h2"} size="xs">
        経営成績
      </Heading>
      <DarkMode>
        <Table.Root size="sm">
          <Table.Header>
            <CustomTableRow>
              <CustomTableColumnHeader>期間</CustomTableColumnHeader>
              {SliceOpeItems(ope?.data ?? []).map((data, index) => (
                <CustomTableColumnHeader
                  key={index}
                  maxW={"80px"}
                  fontSize={"10px"}
                >
                  {ShortLabel(data?.label ?? "")}
                </CustomTableColumnHeader>
              ))}
            </CustomTableRow>
          </Table.Header>
          <Table.Body>
            <CustomTableRow>
              <CustomTableCell>
                {formatPeriodText(
                  ope?.period?.fiscalYear ?? "",
                  ope?.period?.period ?? ""
                )}
              </CustomTableCell>
              {SliceOpeItems(ope?.data ?? []).map((data, index) => (
                <CustomTableCell key={index}>
                  {data.result?.curValue?.value}
                </CustomTableCell>
              ))}
            </CustomTableRow>
            <CustomTableRow>
              <CustomTableCell>
                {formatPeriodText(
                  PreviewFiscalYear(ope?.period?.fiscalYear ?? ""),
                  ope?.period?.period ?? ""
                )}
              </CustomTableCell>
              {SliceOpeItems(ope?.data ?? []).map((data, index) => (
                <CustomTableCell key={index}>
                  {data.result?.preValue?.value}
                </CustomTableCell>
              ))}
            </CustomTableRow>
          </Table.Body>
        </Table.Root>
      </DarkMode>
    </Flex>
  );
};

const ForecastTable: React.FC<StockInfoProps> = ({ item }) => {
  if (item == null) {
    return <Box>No data available</Box>;
  }

  const ope = item.forecast;

  const formatLabelText = (label: string) => {
    if (label == "1株当たり当期純利益") {
      return "EPS";
    } else {
      return label;
    }
  };

  const formatDateStr = (dateStr: string) => {
    const dateObj = new Date(dateStr);
    const year = dateObj.getFullYear().toString().slice(-2); // 2桁表記
    const month = String(dateObj.getMonth() + 1).padStart(2, "0");
    return `${year}.${month}-通期`;
  };

  return (
    <Flex direction="column" gap={1} id="ForecastTable">
      <Heading as={"h2"} size="xs">
        業績予想
      </Heading>
      <DarkMode>
        <Table.Root size="sm">
          <Table.Header>
            <CustomTableRow>
              <CustomTableColumnHeader>期間</CustomTableColumnHeader>
              {ope?.data?.map((data, index) => (
                <CustomTableColumnHeader key={index}>
                  {ShortLabel(formatLabelText(data?.label ?? ""))}
                </CustomTableColumnHeader>
              ))}
            </CustomTableRow>
          </Table.Header>
          <Table.Body>
            <CustomTableRow>
              <CustomTableCell>
                {formatDateStr(ope?.period?.fiscalYear ?? "")}
              </CustomTableCell>
              {ope?.data?.map((data, index) => (
                <CustomTableCell key={index}>
                  {data.forecast?.curValue?.value}
                </CustomTableCell>
              ))}
            </CustomTableRow>
          </Table.Body>
        </Table.Root>
      </DarkMode>
    </Flex>
  );
};
