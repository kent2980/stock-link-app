import { Box, BoxProps } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import { Link, useNavigate } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import dayjs from "dayjs";
import React, { useEffect, useRef } from "react";
import { useSwipeable } from "react-swipeable";
import { XbrlIxHeadService } from "../../client";
import { MenuStore } from "../../routes/_layout/menu.$selectedDate";
import { StockListStore } from "../../Store/Store";
import StockItem from "./StockItem";

interface StockListProps extends BoxProps {
  selectDate: string;
}

/**
 * StockListコンポーネントは、指定された日付の株式リストを表示します。
 *
 * @component
 * @example
 * <StockList selectDate="2021-09-30" />
 *
 * @param {StockListProps} props - プロパティの情報を持つオブジェクト
 * @param {string} props.selectDate - 表示する日付
 * @param {BoxProps} props - Boxコンポーネントに適用されるプロパティ
 *
 * @returns {React.FC<StockListProps>} 指定された日付の株式リストを表示するコンポーネント
 */
const StockList: React.FC<StockListProps> = ({ selectDate, ...props }) => {
  const StockListRef = useRef<HTMLDivElement>(null);
  const navigate = useNavigate({ from: "/menu" });
  const handlers = useSwipeable({
    onSwipedLeft: () => {
      console.log("swipe left");
      // 1日後の日付を取得
      const nextDate = dayjs(selectDate).add(1, "day").format("YYYY-MM-DD");
      navigate({
        to: "/menu/$selectedDate",
        params: { selectedDate: nextDate },
        replace: true,
      });
      MenuStore.setState((state) => {
        return {
          ...state,
          isLeftSwipe: true,
          isRightSwipe: false,
        };
      });
    },
    onSwipedRight: () => {
      console.log("swipe right");
      // 1日前の日付を取得
      const prevDate = dayjs(selectDate)
        .subtract(1, "day")
        .format("YYYY-MM-DD");
      navigate({
        to: "/menu/$selectedDate",
        params: { selectedDate: prevDate },
        replace: true,
      });
      MenuStore.setState((state) => {
        return {
          ...state,
          isRightSwipe: true,
          isLeftSwipe: false,
        };
      });
    },
  });
  const { data } = useQuery({
    queryKey: ["stock_list", selectDate],
    queryFn: () =>
      XbrlIxHeadService.selectIxHeadTitleItems({ dateStr: selectDate }),
  });

  const scrollPosition = useStore(
    StockListStore,
    (state) => state[selectDate]?.scrollPosition ?? 0
  );

  useEffect(() => {
    if (StockListRef.current) {
      console.log("set scroll position", scrollPosition);
      StockListRef.current.scrollTop = scrollPosition;
    }

    const handleScroll = () => {
      if (StockListRef.current) {
        StockListStore.setState((state) => {
          return {
            ...state,
            [selectDate]: {
              scrollPosition: StockListRef?.current?.scrollTop ?? 0,
            },
          };
        });
      }
    };

    const currentRef = StockListRef.current;
    if (currentRef) {
      currentRef.addEventListener("scroll", handleScroll);
    }

    // クリーンアップ関数
    return () => {
      if (currentRef) {
        currentRef.removeEventListener("scroll", handleScroll);
      }
    };
  }, [selectDate]);

  return (
    <Box {...props} {...handlers}>
      <Box
        w="100vw"
        height="calc(100vh - 210px)"
        overflowY="scroll"
        ref={StockListRef}
      >
        <Box h="40px" />
        {data?.data?.map((item) => {
          return (
            <Link to="/summary/$xbrl_id" params={{ xbrl_id: item.xbrl_id }}>
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
              >
                <StockItem item={item} />
              </Box>
            </Link>
          );
        })}
        {/* 最後尾に空白行を追加 */}
        <Box h="40px" />
      </Box>
    </Box>
  );
};

export default StockList;
