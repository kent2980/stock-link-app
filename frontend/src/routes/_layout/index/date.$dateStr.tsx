import StockList from "@/components/StockList/StockList";
import { HeaderStore } from "@/Store/Store";
import { Box, HStack, IconButton, Text } from "@chakra-ui/react";
import {
  createFileRoute,
  useNavigate,
  useParams,
} from "@tanstack/react-router";
import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";
import { GrCaretNext, GrCaretPrevious } from "react-icons/gr";

export const Route = createFileRoute("/_layout/index/date/$dateStr")({
  component: Index,
});

function Index() {
  // urlパラメータから日付を取得
  const { dateStr } = useParams({ from: "/_layout/index/date/$dateStr" });

  // Storeを更新
  HeaderStore.setState((state) => ({
    ...state,
    SelectDateStr: dateStr,
    CurrentCategory: null,
  }));

  return (
    <Box overflow="hidden">
      {/* 次の日と前日に移動するリンクを配置 */}
      <PageLinkArea dateStr={dateStr} />
      <Box display={{ base: "block", md: "none" }}>
        <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
          <Suspense fallback={<div>Loading...</div>}>
            <StockList dateStr={dateStr} />
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
      to: "/index/date/$dateStr",
      search: {
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
