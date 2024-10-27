import { Badge, Box, BoxProps, HStack, VStack } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import { useNavigate } from "@tanstack/react-router";
import dayjs from "dayjs";
import React from "react";
import { useSwipeable } from "react-swipeable";
import { XbrlIxHeadService } from "../../client";

interface StockListProps extends BoxProps {
  selectDate: string;
}

const StockList: React.FC<StockListProps> = ({ selectDate, ...props }) => {
  const navigate = useNavigate({ from: "/menu" });
  const handlers = useSwipeable({
    onSwipedLeft: () => {
      // 1日後の日付を取得
      const nextDate = dayjs(selectDate).add(1, "day").format("YYYY-MM-DD");
      navigate({
        to: "/menu/$selectedDate",
        params: { selectedDate: nextDate },
        replace: true,
      });
    },
    onSwipedRight: () => {
      // 1日前の日付を取得
      const prevDate = dayjs(selectDate)
        .subtract(1, "day")
        .format("YYYY-MM-DD");
      navigate({
        to: "/menu/$selectedDate",
        params: { selectedDate: prevDate },
        replace: true,
      });
    },
  });
  const { data } = useQuery({
    queryKey: ["stock_list", selectDate],
    queryFn: () =>
      XbrlIxHeadService.selectIxHeadTitleItems({ dateStr: selectDate }),
    staleTime: 1000 * 60 * 60 * 24,
    gcTime: 1000 * 60 * 60 * 24,
  });
  return (
    <Box {...props} {...handlers} w="100vw" overflowY="scroll">
      <Box h="40px" />
      {data?.data?.map((item) => {
        const code = item.securities_code; // 銘柄コード
        const name = item.company_name; // 企業名
        const report_type = () => {
          if (item?.report_type?.startsWith("ed")) {
            return "決算短信";
          } else if (item?.report_type === "rvdf") {
            return "業績予想の修正";
          } else if (item?.report_type === "rvfc") {
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

        const year = item.fiscal_year_end; // 決算期
        return (
          <Box
            key={item.xbrl_id}
            w="100%"
            borderBottom="1px"
            borderColor="gray.200"
            display="flex"
            alignItems="center"
            justifyContent="space-between"
            p={2}
            _hover={{ cursor: "pointer", bgColor: "gray.100" }}
            onClick={() =>
              navigate({
                to: "/summary/$xbrl_id",
                params: { xbrl_id: item.xbrl_id },
              })
            }
          >
            <VStack m={2} w="100%">
              <HStack justify="flex-start" w="100%">
                <Box>{code}</Box>
                <Box>{name}</Box>
              </HStack>
              <HStack justify="flex-start" w="100%">
                <Badge>{dayjs(year).format("YYYY年M月期")}</Badge>
                <Badge display={period() === "" ? "none" : "block"}>
                  {period()}
                </Badge>
                <Badge>{report_type()}</Badge>
              </HStack>
            </VStack>
          </Box>
        );
      })}
      {/* 最後尾に空白行を追加 */}
      <Box h="40px" />
    </Box>
  );
};

export default StockList;
