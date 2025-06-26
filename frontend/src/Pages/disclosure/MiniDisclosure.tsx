import {
  FinancialSummaryService,
  FinItemsResponse,
  FinValueFinance,
} from "@/client";
import {
  Box,
  Flex,
  Heading,
  HStack,
  List,
  Skeleton,
  Text,
} from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
// Import Swiper React components
import { Swiper, SwiperSlide } from "swiper/react";

// Import Swiper styles
import "swiper/css";
import "swiper/css/pagination";

// import required modules
import { Pagination } from "swiper/modules";

interface MiniDisclosureProps {
  code_17?: number;
}

export default function MiniDisclosure(props: MiniDisclosureProps) {
  // コード17をpropsから取得
  const { code_17 } = props;
  const { data, isLoading } = useSuspenseQuery({
    queryKey: ["disclosureItems", code_17],
    queryFn: async () => {
      return await FinancialSummaryService.getDisclosureItems({
        page: 1,
        limit: 20,
        code17: code_17,
      });
    },
    gcTime: 24 * 60 * 60 * 1000, // 24時間後にガーベジコレクション
    staleTime: 10 * 60 * 1000, // 10分間のステールタイム
    retry: false,
  });

  if (isLoading) {
    return <LoadingItems length={20} />;
  } else if (!data) {
    return (
      <Box p={4} h="100vh">
        No data available
      </Box>
    );
  }

  // const handleLinkClick = (itemId: string) => {
  //   // クリックされたアイテムの詳細ページへ遷移
  //   navigate({ to: `/disclosure/page/${itemId}` });
  // };

  return (
    <>
      <Swiper
        direction="vertical"
        pagination={{
          clickable: true,
        }}
        modules={[Pagination]}
        className="mySwiper"
        navigation={true}
      >
        {data.data?.map((item, key) => {
          // const ope = item?.operating_result;
          // const forecast = item?.forecast;
          // const cashflow = item?.cashflow;
          return (
            <SwiperSlide>
              <Box h="50vh">
                <Box>{key.toString() + item.code}</Box>
                <ValueList
                  items={item.operating_result}
                  type="operating_result"
                />
              </Box>
            </SwiperSlide>
          );
        })}
      </Swiper>
    </>
  );
}

interface ValueListProps {
  items: FinItemsResponse | null | undefined;
  type: string;
}

function ValueList({ items, type }: ValueListProps) {
  const itemValue = (item: FinValueFinance) => {
    switch (type) {
      case "operating_result":
        return item.result?.curChange?.value != null &&
          item.result?.curChange?.display_scale != null
          ? `${item.result.curChange.value.toFixed(1).toString().replace("-", "△")} ${item.result.curChange.display_scale}`
          : " - ";
      case "forecast":
        // curValue?.unitが"JPYPerShare"の場合はcurValue?.valueを表示
        if (
          item.forecast?.curValue?.unit === "JPYPerShares" &&
          item.forecast?.curValue?.value != null
        ) {
          return `${item.forecast.curValue.value.toString().replace("-", "△")} ${item.forecast.curValue.display_scale}`;
        }
        return item.forecast?.curChange?.value != null &&
          item.forecast?.curChange?.display_scale != null
          ? `${item.forecast.curChange.value.toFixed(1).toString().replace("-", "△")} ${item.forecast.curChange.display_scale}`
          : " - ";
      case "cashflow":
        return item.result?.curValue?.value != null &&
          item.result?.curValue?.display_scale != null
          ? `${item.result.curValue.value.toString().replace("-", "△")} ${item.result.curValue.display_scale}`
          : " - ";
      default:
        return " - ";
    }
  };
  const itemPreValue = (item: FinValueFinance) => {
    switch (type) {
      case "operating_result":
        return item.result?.preChange?.value != null &&
          item.result?.preChange?.display_scale != null
          ? `${item.result.preChange.value.toFixed(1).toString().replace("-", "△")} ${item.result.preChange.display_scale}`
          : " - ";
      case "forecast":
        return null;
      case "cashflow":
        return item.result?.preValue?.value != null &&
          item.result?.preValue?.display_scale != null
          ? `${item.result.preValue.value.toString().replace("-", "△")} ${item.result.preValue.display_scale}`
          : " - ";
      default:
        return " - ";
    }
  };
  const headingLabel = (type: string) => {
    switch (type) {
      case "operating_result":
        return "経営成績";
      case "forecast":
        return "業績予想";
      case "cashflow":
        return "キャッシュフロー";
      default:
        return "その他";
    }
  };
  console.log("ValueList items:", items);
  return (
    <Box w="100%" display={items ? "block" : "none"}>
      <Heading
        as="h4"
        size="xs"
        mb={2}
        px={4}
        py={1}
        color="green.600"
        borderY="1px solid"
        borderColor="gray.200"
      >
        {headingLabel(type)}
      </Heading>
      <List.Root listStyle="none">
        {items?.data?.map((item, index) => (
          <List.Item
            key={index}
            borderBottom={
              index !== (items.data?.length ?? 0) - 1 ? "1px solid" : undefined
            }
            borderColor={
              index !== (items.data?.length ?? 0) - 1 ? "gray.200" : undefined
            }
          >
            <HStack justify="space-between">
              <Text className="label">
                {item.label?.replace("によるキャッシュ・フロー", "CF")}
              </Text>
              <HStack>
                <Text className="value">{itemValue(item)}</Text>
                <Text
                  className="pre-value"
                  color="gray.500"
                  textAlign="right"
                  display={itemPreValue(item) ? "block" : "none"}
                >
                  ({itemPreValue(item)})
                </Text>
              </HStack>
            </HStack>
          </List.Item>
        ))}
      </List.Root>
    </Box>
  );
}

function LoadingItems({ length = 20 }: { length?: number }) {
  return (
    <>
      {Array.from({ length: length }).map((_, index: number) => (
        <Box key={index} p={3} bg="white" boxShadow="sm" m={3} h="60vh">
          <Flex direction="column" gap={2}>
            <Skeleton h="20vh" />
          </Flex>
        </Box>
      ))}
    </>
  );
}
