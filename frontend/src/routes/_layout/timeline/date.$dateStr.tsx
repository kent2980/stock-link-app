import CustomSpinner from "@/components/Spinner/CustomSpinner";
import DateStockList from "@/components/StockList/DateStockList";
import { HeaderStore } from "@/Store/Store";
import { Box, HStack, IconButton, Text } from "@chakra-ui/react";
import {
  createFileRoute,
  useNavigate,
  useParams,
} from "@tanstack/react-router";
import { Suspense, useEffect, useLayoutEffect } from "react";
import { ErrorBoundary } from "react-error-boundary";
import { GrCaretNext, GrCaretPrevious } from "react-icons/gr";
import { useSwipeable } from "react-swipeable";

export const Route = createFileRoute("/_layout/timeline/date/$dateStr")({
  component: Index,
});

function Index() {
  // urlパラメータから日付を取得
  const { dateStr } = useParams({ from: "/_layout/timeline/date/$dateStr" });
  console.log("dateStr", dateStr);
  // Storeを更新
  HeaderStore.setState((state) => ({
    ...state,
    SelectDateStr: dateStr,
    CurrentCategory: null,
  }));

  // スワイプ操作のための関数を定義
  const navigate = useNavigate({
    from: "/_layout/index/date/$dateStr",
  });

  const handleClick = (dateStr: string) => {
    navigate({
      to: "/timeline/date/$dateStr",
      params: {
        dateStr: dateStr,
      },
    });
  };

  const prevDate = () => {
    const date = new Date(dateStr);
    date.setDate(date.getDate() - 1);
    return date.toISOString().split("T")[0];
  };

  const nextDate = () => {
    const date = new Date(dateStr);
    date.setDate(date.getDate() + 1);
    return date.toISOString().split("T")[0];
  };

  // スワイプ操作のハンドラを定義
  const swipeHandlers = useSwipeable({
    onSwipedLeft: () => handleClick(prevDate()), // 左スワイプで次の日
    onSwipedRight: () => handleClick(nextDate()), // 右スワイプで前日
  });

  // スクロール位置の復元と永続化
  // スクロール位置のキーを日付ごとに分ける
  const scrollKey = `scroll-position-${dateStr}`;

  // ページ読み込み時にスクロール位置を復元
  useLayoutEffect(() => {
    const saved = localStorage.getItem(scrollKey);
    if (saved) {
      window.scrollTo(0, Number(saved));
    } else {
      window.scrollTo(0, 0);
    }
  }, [scrollKey]);

  // ページ離脱時にスクロール位置を保存
  useEffect(() => {
    const saveScroll = () => {
      localStorage.setItem(scrollKey, String(window.scrollY));
    };
    window.addEventListener("beforeunload", saveScroll);
    return () => {
      saveScroll();
      window.removeEventListener("beforeunload", saveScroll);
    };
  }, [scrollKey]);

  return (
    <Box overflow="hidden" {...swipeHandlers}>
      <Box minH="100vh">
        <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
          <Suspense fallback={<CustomSpinner />}>
            <DateStockList dateStr={dateStr} />
          </Suspense>
        </ErrorBoundary>
      </Box>
      {/* 次の日と前日に移動するリンクを配置 */}
      <PageLinkArea dateStr={dateStr} />
    </Box>
  );
}

interface PageLinkAreaProps {
  dateStr: string;
}

const PageLinkArea: React.FC<PageLinkAreaProps> = ({ dateStr }) => {
  // 画面遷移のための関数を定義
  const navigate = useNavigate({
    from: "/_layout/index/date/$dateStr",
  });
  const handleClick = (dateStr: string) => {
    navigate({
      to: "/timeline/date/$dateStr",
      params: {
        dateStr: dateStr,
      },
    });
  };

  // 日付の前日、翌日を取得する関数を定義
  const prevDate = () => {
    const date = new Date(dateStr);
    date.setDate(date.getDate() - 1);
    const prevDateStr = date.toISOString().split("T")[0];
    return prevDateStr;
  };

  const nextDate = () => {
    const date = new Date(dateStr);
    date.setDate(date.getDate() + 1);
    const nextDateStr = date.toISOString().split("T")[0];
    return nextDateStr;
  };

  return (
    <>
      {/* 次の日と前日に移動するリンクを配置 */}
      <HStack justifyContent={"center"} p={4} bg="white" gap={20}>
        <HStack>
          <IconButton
            aria-label="Next Day"
            onClick={() => handleClick(nextDate())}
            variant="subtle"
            colorScheme="gray"
            size="sm"
            cursor="pointer"
          >
            <GrCaretPrevious />
          </IconButton>
          <Text
            fontSize="12px"
            onClick={() => handleClick(nextDate())}
            cursor="pointer"
          >
            Next Day
          </Text>
        </HStack>
        <HStack>
          <Text
            fontSize="12px"
            onClick={() => handleClick(prevDate())}
            cursor="pointer"
          >
            Prev Day
          </Text>
          <IconButton
            aria-label="Previous Day"
            onClick={() => handleClick(prevDate())}
            variant="subtle"
            colorScheme="gray"
            size="sm"
            cursor="pointer"
          >
            <GrCaretNext />
          </IconButton>
        </HStack>
      </HStack>
    </>
  );
};
