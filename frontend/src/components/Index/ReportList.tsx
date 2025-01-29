import {
  Badge,
  Box,
  BoxProps,
  Progress,
  Table,
  TableContainer,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
  useColorModeValue,
} from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { Suspense } from "react";
import { IxHeadTitlePublic, XbrlIxHeadService } from "../../client";

interface ReportContentsProps extends BoxProps {
  selectDate: string;
}
/**
 * コンテンツ表示用のコンポーネント
 * @param props  BoxProps
 */
const ReportContents: React.FC<ReportContentsProps> = (props) => {
  const { selectDate } = props;
  const textColor = useColorModeValue("ui.dark", "ui.light");
  const borderColor = useColorModeValue("#d1d9e0", "#ffffff29");
  // IxHeadTitlePublicのデータを取得
  const { data } = useSuspenseQuery({
    queryKey: ["xbrlIxHead", selectDate],
    queryFn: () =>
      XbrlIxHeadService.selectIxHeadTitleItems({
        dateStr: selectDate,
      }),
    // staleTime: 1000 * 60 * 60 * 24,
    gcTime: 1000 * 60 * 60 * 24,
  });

  return (
    <Box color={textColor} {...props}>
      <Box
        display={{ base: "block", md: "block" }}
        border="1px solid"
        borderColor={borderColor}
        borderRadius={6}
      >
        <TableContainer>
          <Table size="sm">
            <Thead>
              <Tr>
                <Th>種別</Th>
                <Th>コード</Th>
                <Th maxW={10}>企業名</Th>
                <Th colSpan={2}>進捗率</Th>
              </Tr>
            </Thead>
            <Tbody>
              {data.data.map((item: IxHeadTitlePublic, key) => (
                <ReportItem item={item} key={key} />
              ))}
            </Tbody>
          </Table>
        </TableContainer>
      </Box>
    </Box>
  );
};

interface ReportItemProps {
  item: IxHeadTitlePublic | null;
  key: number;
}

const ReportItem: React.FC<ReportItemProps> = ({ item, key }) => {
  const hoverColor = useColorModeValue("#99aebc32", "#ffffff18");
  const getReportTypeLabel = (value: string | null | undefined): string => {
    if (value === null || value === undefined) {
      return "";
    } else if (value.startsWith("ed")) {
      return "決算短信";
    } else if (value === "rvfc") {
      return "業績修正";
    }
    return "";
  };

  // const getPeriodLabel = (value: string | null | undefined): string | null => {
  //   if (value === null || value === undefined) {
  //     return "";
  //   } else if (value === "HY") {
  //     return "中間期";
  //   } else if (value === "FY") {
  //     return "通期";
  //   } else if (value.startsWith("Q")) {
  //     const periodNumber = value.slice(1, 2);
  //     return `第${periodNumber}四半期`;
  //   } else {
  //     return "";
  //   }
  // };

  // const getResultWord = (item: IxHeadTitlePublic): string => {
  //   let salesComment = "";
  //   let incomeComment = "";
  //   if (item?.change_in_net_sales && item.change_in_net_sales > 0) {
  //     salesComment = "増収";
  //   } else if (item.change_in_net_sales && item.change_in_net_sales < 0) {
  //     salesComment = "減収";
  //   }
  //   if (item?.change_in_net_income && item.change_in_net_income > 0) {
  //     incomeComment = "増益";
  //   } else if (item.change_in_net_income && item.change_in_net_income < 0) {
  //     incomeComment = "減益";
  //   }
  //   return `${salesComment}${incomeComment}`;
  // };

  // const geiRevisionComment = (item: IxHeadTitlePublic): string => {
  //   const commonComment = "また、上記の経営成績を勘案した結果、";
  //   let comment = "";
  //   if (item?.is_div_rev === true && item.is_fcst_rev === true) {
  //     comment = commonComment + "配当金予想と業績予想が修正されました。";
  //   } else if (item.is_div_rev === true) {
  //     comment = commonComment + "配当金予想が修正されました。";
  //   } else if (item.is_fcst_rev === true) {
  //     comment = commonComment + "業績予想が修正されました。";
  //   }
  //   return comment;
  // };

  const getProgressColor = (item: IxHeadTitlePublic): string => {
    if (item?.current_period) {
      const period = item.current_period as keyof typeof period_map;
      const period_map = { Q1: 25, Q2: 50, Q3: 75, Q4: 100, HY: 50, FY: 100 };
      if (item.oi_prog_rt && item.oi_prog_rt >= period_map[period]) {
        return "green";
      } else {
        return "pink";
      }
    }
    return "";
  };

  return (
    <Tr key={key} _hover={{ background: hoverColor }}>
      <Td fontSize={10} maxW="10vw" whiteSpace="nowrap">
        <Badge>{getReportTypeLabel(item?.report_type)}</Badge>
      </Td>
      <Td whiteSpace="nowrap">{item?.securities_code}</Td>
      <Td maxW="20vw" whiteSpace={"normal"}>
        {item?.company_name}
      </Td>
      <Td maxW="10vw" fontSize={10} fontWeight={600}>
        {item?.oi_prog_rt ? item.oi_prog_rt + "%" : ""}
      </Td>
      <Td maxW="10vw">
        <Progress
          value={item?.oi_prog_rt ?? 0}
          size={"xs"}
          hasStripe
          colorScheme={getProgressColor(item as IxHeadTitlePublic)}
        />
      </Td>
    </Tr>
  );
};

interface ReportListProps extends BoxProps {
  selectDate?: string;
}

const ReportList: React.FC<ReportListProps> = (props) => {
  const { selectDate } = props;
  const today = new Date().toISOString().split("T")[0];
  return (
    <Box {...props}>
      <Suspense
        fallback={
          <TableContainer>
            <Table>
              <Thead>
                <Tr>
                  <Th>企業名</Th>
                </Tr>
              </Thead>
              <Tbody>
                {Array.from({ length: 10 }).map((_, key) => (
                  <ReportItem item={null} key={key} />
                ))}
              </Tbody>
            </Table>
          </TableContainer>
        }
      >
        <ReportContents selectDate={selectDate ? selectDate : today} />
      </Suspense>
    </Box>
  );
};

export default ReportList;
