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
  const scaleTime = () => {
    // selectDateを日付型に変換
    const date = new Date(selectDate);
    const today = new Date();
    if (date.getTime() === today.getTime()) {
      return 0;
    } else {
      // 7日間の秒数
      return 7 * 24 * 60 * 60 * 1000;
    }
  };
  const gcTime = scaleTime();
  // IR報告書タイプごとの件数データを取得
  const { data, status } = useQuery({
    queryKey: ["stock_list", selectDate],
    queryFn: () =>
      XbrlIxHeadService.selectIxHeadTitleItems({ dateStr: selectDate }),
    staleTime: scaleTime(),
    gcTime: gcTime,
  });

  // スクロール位置を保持するためのRef
  const StockListRef = useRef<HTMLDivElement>(null);

  // ルーティング用のフック
  const navigate = useNavigate({ from: "/menu" });

  // スワイプイベントのハンドラ
  const handlers = useSwipeable({
    // 左スワイプイベントのハンドラ
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
    // 右スワイプイベントのハンドラ
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

  // スクロール位置をStoreから取得
  const scrollPosition = useStore(
    StockListStore,
    (state) => state[selectDate]?.scrollPosition ?? 0
  );

  // スクロール位置の記憶・復元処理 ※selectDateが変更された場合のみ実行
  useEffect(() => {
    // スクロール位置を設定
    if (StockListRef.current) {
      console.log("set scroll position", scrollPosition);
      StockListRef.current.scrollTop = scrollPosition;
    }
    // スクロールイベントのハンドラ
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
    // スクロールイベントのリスナーを登録
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

  if (status === "pending") {
    return <Box />;
  }

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
            <Link
              to="/summary/$head_item_key"
              params={{ head_item_key: item.item_key }}
              key={item.item_key}
            >
              <Box
                key={item.item_key}
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
