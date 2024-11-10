import { Box, HStack, Text, VStack } from "@chakra-ui/react";
import { createFileRoute, Link } from "@tanstack/react-router";
import { Store } from "@tanstack/react-store";
import dayjs from "dayjs";
import "dayjs/locale/ja"; // 日本語ロケールをインポート
import { useEffect, useRef, useState } from "react";
import SelectItem from "../../components/Menu/SelectItem";

dayjs.locale("ja"); // 日本語ロケールを設定

export const Route = createFileRoute("/_layout/menu/$selectedDate")({
  component: Menu,
});

export const MenuStore = new Store({
  isLeftSwipe: false,
  isRightSwipe: false,
});

function Menu() {
  const { selectedDate } = Route.useParams();
  const dateGroupRef = useRef<HTMLDivElement>(null);

  let scrollPoint = 0;

  const generateDates = () => {
    const dates = [];
    for (let i = 0; i < 365; i++) {
      dates.push(dayjs().subtract(i, "day").format("YYYY-MM-DD"));
      if (selectedDate === dayjs().subtract(i, "day").format("YYYY-MM-DD")) {
        scrollPoint = i * 76 + 76 * 3 + 16;
      }
    }
    return dates;
  };

  const dates = generateDates();

  const [isSwipeHandled, setIsSwipeHandled] = useState(false);

  useEffect(() => {
    if (dateGroupRef.current) {
      console.log("else");
      dateGroupRef.current.scrollLeft =
        dateGroupRef.current.scrollWidth - scrollPoint;
    }
  }, []);

  useEffect(() => {
    if (isSwipeHandled) {
      MenuStore.setState((state) => ({
        ...state,
        isLeftSwipe: false,
        isRightSwipe: false,
      }));
      setIsSwipeHandled(false);
    }
  }, [isSwipeHandled]);

  return (
    <VStack spacing={0}>
      <SelectItem selectDate={selectedDate} height="calc(100vh - 100px)" />
      <HStack
        overflowX="scroll"
        spacing={4}
        width="100vw"
        id="date-group"
        ref={dateGroupRef}
        height="100px"
        p={2}
      >
        {dates
          .map((date) => (
            <Link
              to="/menu/$selectedDate"
              params={{ selectedDate: date }}
              replace
              key={date}
            >
              <Box
                className="date-box"
                _hover={
                  selectedDate === date
                    ? { cursor: "pointer", bgColor: "blue.500" }
                    : { cursor: "pointer", bgColor: "gray.100" }
                }
                bgColor={selectedDate === date ? "blue.500" : "white"}
                textAlign="center"
                padding="4px"
                border="1px solid #ccc"
                borderRadius="4px"
                width="60px"
                flexShrink={0}
                height="full"
                boxShadow="0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08)"
              >
                <Box
                  color={
                    selectedDate === date
                      ? "white"
                      : dayjs(date).day() === 0
                        ? "red.500"
                        : dayjs(date).day() === 6
                          ? "blue.500"
                          : "gray.500"
                  }
                  fontWeight={selectedDate === date ? "bold" : "normal"}
                  fontFamily="monospace"
                  display="flex"
                  flexDirection="column"
                  justifyContent="space-between"
                  height="100%"
                >
                  <Text fontSize="14px">{dayjs(date).format("MM/DD")}</Text>{" "}
                  {/* 日付を表示 */}
                  <Text fontSize="13px" textAlign="center" mb={2}>
                    {dayjs(date).format("dd")}
                  </Text>{" "}
                  {/* 曜日を日本語で表示 */}
                </Box>
              </Box>
            </Link>
          ))
          .reverse()}
      </HStack>
    </VStack>
  );
}
