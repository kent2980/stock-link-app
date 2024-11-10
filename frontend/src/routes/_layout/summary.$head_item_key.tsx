import { Box, Spinner, Stack } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { EffectCube, Navigation, Pagination, Scrollbar } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/react";
import SummaryBox from "../../components/summary/SummaryBox";
import SummaryHeader from "../../components/summary/SummaryHeader";
import SummaryQualitative from "../../components/summary/SummaryQualitative";

import "swiper/css";
import "swiper/css/effect-cube";
import { XbrlViewService } from "../../client";

function queryOptions(head_item_key: string) {
  return {
    queryKey: ["summary", head_item_key],
    queryFn: () =>
      XbrlViewService.readSummaryItemByHeadItemKey({
        headItemKey: head_item_key,
      }),
  };
}

export const Route = createFileRoute("/_layout/summary/$head_item_key")({
  loader: async ({ context: { queryClient }, params: { head_item_key } }) => {
    return queryClient.ensureQueryData(queryOptions(head_item_key));
  },
  component: Summary,
  pendingComponent: () => (
    <Box>
      <Spinner
        size="xl"
        thickness="10px"
        speed="1s"
        emptyColor="gray.200"
        color="blue.500"
      />
    </Box>
  ),
  notFoundComponent: () => <Box>Not found</Box>,
  errorComponent: () => <Box>Error</Box>,
});

function Summary() {
  const { head_item_key } = Route.useParams();
  // モバイルの場合
  if (window.innerWidth < 768) {
    return (
      <>
        <SummaryHeader head_item_key={head_item_key} height="80px" />
        <Swiper
          modules={[EffectCube, Scrollbar, Navigation, Pagination]}
          spaceBetween={0}
          slidesPerView={1}
          loop={true}
          scrollbar={{ draggable: true }}
          pagination={{ clickable: true }}
          onSwiper={(swiper) => console.log(swiper)}
          onSlideChange={() => console.log("slide change")}
          effect="cube"
          cubeEffect={{
            shadow: false,
            slideShadows: true,
            shadowOffset: 2,
            shadowScale: 0.94,
          }}
        >
          <SwiperSlide>
            <SummaryBox
              head_item_key={head_item_key}
              className="swiper-child"
            />
          </SwiperSlide>
          <SwiperSlide>
            <SummaryQualitative
              head_item_key={head_item_key}
              className="swiper-child"
            />
          </SwiperSlide>
        </Swiper>
      </>
    );
  } else {
    return (
      <Box>
        <SummaryHeader head_item_key={head_item_key} />
        <Stack direction={"row"} marginTop={24} alignItems="flex-start">
          <SummaryBox head_item_key={head_item_key} width="32%" />
          <SummaryQualitative head_item_key={head_item_key} width="66%" />
        </Stack>
      </Box>
    );
  }
}
