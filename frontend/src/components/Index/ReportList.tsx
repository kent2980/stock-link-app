import {
  Box,
  BoxProps,
  CircularProgress,
  CircularProgressLabel,
  Flex,
  HStack,
  List,
  ListItem,
  Popover,
  PopoverArrow,
  PopoverContent,
  PopoverHeader,
  PopoverTrigger,
  Skeleton,
  SkeletonCircle,
  Tag,
  Text,
  useColorModeValue,
  VStack,
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
    staleTime: 1000 * 60 * 60 * 24,
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
        <List>
          {data.data.map((item: IxHeadTitlePublic, key) => (
            <ReportItem item={item} key={key} />
          ))}
        </List>
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
  const borderColor = useColorModeValue("#d1d9e0", "#ffffff29");
  const getReportTypeLabel = (value: string | null | undefined): string => {
    if (value === null || value === undefined) {
      return "";
    } else if (value.startsWith("ed")) {
      return "決算短信";
    } else if (value === "rvfc") {
      return "業績予想修正";
    }
    return "";
  };

  const getPeriodLabel = (value: string | null | undefined): string | null => {
    if (value === null || value === undefined) {
      return "";
    } else if (value === "HY") {
      return "中間期";
    } else if (value === "FY") {
      return "通期";
    } else if (value.startsWith("Q")) {
      const periodNumber = value.slice(1, 2);
      return `第${periodNumber}四半期`;
    } else {
      return "";
    }
  };

  const getResultWord = (item: IxHeadTitlePublic): string => {
    let salesComment = "";
    let incomeComment = "";
    if (item.change_in_net_sales && item.change_in_net_sales > 0) {
      salesComment = "増収";
    } else if (item.change_in_net_sales && item.change_in_net_sales < 0) {
      salesComment = "減収";
    }
    if (item.change_in_net_income && item.change_in_net_income > 0) {
      incomeComment = "増益";
    } else if (item.change_in_net_income && item.change_in_net_income < 0) {
      incomeComment = "減益";
    }
    return `${salesComment}${incomeComment}`;
  };

  const geiRevisionComment = (item: IxHeadTitlePublic): string => {
    const commonComment = "また、上記の経営成績を勘案した結果、";
    let comment = "";
    if (item.is_div_rev === true && item.is_fcst_rev === true) {
      comment = commonComment + "配当金予想と業績予想が修正されました。";
    } else if (item.is_div_rev === true) {
      comment = commonComment + "配当金予想が修正されました。";
    } else if (item.is_fcst_rev === true) {
      comment = commonComment + "業績予想が修正されました。";
    }
    return comment;
  };

  const getCircularProgressColor = (item: IxHeadTitlePublic): string => {
    if (item.current_period) {
      const period = item.current_period as keyof typeof period_map;
      const period_map = { Q1: 25, Q2: 50, Q3: 75, Q4: 100, HY: 50, FY: 100 };
      if (item.oi_prog_rt && item.oi_prog_rt >= period_map[period]) {
        return "green.400";
      } else {
        return "red.400";
      }
    }
    return "";
  };

  return (
    <ListItem
      key={key}
      p={4}
      _hover={{ bg: hoverColor }}
      borderBottomWidth="1px"
      borderColor={borderColor}
    >
      <Flex gap={{ base: 2, md: 4 }} fontSize={14}>
        <VStack width="100%">
          <HStack justifyContent="space-between" width="100%">
            <HStack gap={3}>
              {item ? (
                <Text border="0.8px solid" borderColor={borderColor} px={2}>
                  {item.securities_code}
                </Text>
              ) : (
                <Skeleton height="20px" width="50px" />
              )}
              {item ? (
                <Text fontSize={14} fontWeight={600}>
                  {item.company_name}
                </Text>
              ) : (
                <Skeleton height="20px" width="200px" />
              )}
            </HStack>
            <Box>
              <Popover>
                <PopoverTrigger>
                  {item ? (
                    <CircularProgress
                      value={
                        item.oi_prog_rt
                          ? item.oi_prog_rt < 0
                            ? 0
                            : item.oi_prog_rt
                          : 0
                      }
                      color={getCircularProgressColor(item)}
                      size="55px"
                      fontWeight={600}
                    >
                      <CircularProgressLabel>
                        {item.oi_prog_rt && item.oi_prog_rt + "%"}
                      </CircularProgressLabel>
                    </CircularProgress>
                  ) : (
                    <SkeletonCircle size="55px" />
                  )}
                </PopoverTrigger>
                <PopoverContent w="auto">
                  <PopoverArrow />
                  <PopoverHeader>経常利益進捗率</PopoverHeader>
                </PopoverContent>
              </Popover>
            </Box>
          </HStack>
          <Flex
            fontSize={10}
            color="black"
            alignSelf="flex-start"
            gap={2}
            height={4}
          >
            {item ? (
              item.current_period && (
                <Tag size="sm">{getPeriodLabel(item.current_period)}</Tag>
              )
            ) : (
              <Skeleton height="20px" width="50px" />
            )}
            {item ? (
              <Tag size="sm">{getReportTypeLabel(item.report_type)}</Tag>
            ) : (
              <Skeleton height="20px" width="50px" />
            )}
          </Flex>
          <Box alignSelf="flex-start">
            {item?.report_type && item.report_type.startsWith("ed") && (
              <Text fontSize={12}>
                {getPeriodLabel(item.current_period)}
                までの経営成績は{getResultWord(item)}、売上高の増減率は
                {item.change_in_net_sales ?? "-"}%、経常利益の増減率は
                {item.change_in_ordinary_income ?? "-"}%, 純利益の増減率は
                {item.change_in_net_income ?? "-"}%でした。
                <br />
                {geiRevisionComment(item)}
              </Text>
            )}
          </Box>
        </VStack>
      </Flex>
    </ListItem>
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
          <List>
            {Array.from({ length: 10 }).map((_, key) => (
              <ReportItem item={null} key={key} />
            ))}
          </List>
        }
      >
        <ReportContents selectDate={selectDate ? selectDate : today} />
      </Suspense>
    </Box>
  );
};

export default ReportList;
