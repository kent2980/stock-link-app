import { Box, Stack } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { EffectCube, Navigation, Pagination, Scrollbar } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/react";
import SummaryBox from "../../components/summary/SummaryBox";
import SummaryHeader from "../../components/summary/SummaryHeader";
import SummaryQualitative from "../../components/summary/SummaryQualitative";

import "swiper/css";
import "swiper/css/effect-cube";
import "swiper/css/navigation";
import "swiper/css/pagination";
import "swiper/css/scrollbar";
import { XbrlViewService } from "../../client";

function queryOptions(xbrl_id: string) {
  return {
    queryKey: ["summary", xbrl_id],
    queryFn: () =>
      XbrlViewService.readSummaryItemByXbrlId({
        xbrlId: xbrl_id,
      }),
  };
}

export const Route = createFileRoute("/_layout/summary/$xbrl_id")({
  loader: async ({ context: { queryClient }, params: { xbrl_id } }) => {
    return queryClient.ensureQueryData(queryOptions(xbrl_id));
  },
  component: Summary,
  pendingComponent: () => <Box>Loading...</Box>,
  notFoundComponent: () => <Box>Not found</Box>,
  errorComponent: () => <Box>Error</Box>,
});

function Summary() {
  const { xbrl_id } = Route.useParams();
  // モバイルの場合
  if (window.innerWidth < 768) {
    return (
      <>
        <SummaryHeader xbrl_id={xbrl_id} height="80px" />
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
            <SummaryBox xbrl_id={xbrl_id} className="swiper-child" />
          </SwiperSlide>
          <SwiperSlide>
            <SummaryQualitative xbrl_id={xbrl_id} className="swiper-child" />
          </SwiperSlide>
        </Swiper>
      </>
    );
  } else {
    return (
      <Box>
        <SummaryHeader xbrl_id={xbrl_id} />
        <Stack direction={"row"} marginTop={24} alignItems="flex-start">
          <SummaryBox xbrl_id={xbrl_id} width="32%" />
          <SummaryQualitative xbrl_id={xbrl_id} width="66%" />
        </Stack>
      </Box>
    );
  }
}
