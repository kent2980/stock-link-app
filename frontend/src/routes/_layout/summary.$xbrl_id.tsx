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

export const Route = createFileRoute("/_layout/summary/$xbrl_id")({
  component: Summary,
});

function Summary() {
  const { xbrl_id } = Route.useParams();
  // const { data: item, status } = useQuery({
  //   queryKey: ["head", xbrl_id],
  //   queryFn: () =>
  //     XbrlViewService.readHeadItem({
  //       xbrlId: xbrl_id,
  //     }),
  // });

  // if (status === "error") {
  //   return <Box>Error</Box>;
  // }

  // if (status === "pending") {
  //   return (
  //     <Box
  //       display="flex"
  //       justifyContent="center"
  //       alignItems="center"
  //       height="100vh"
  //       width="100%"
  //     >
  //       <Spinner
  //         size="xl"
  //         thickness="10px"
  //         speed="1s"
  //         emptyColor="gray.200"
  //         color="blue.500"
  //       />
  //     </Box>
  //   );
  // }

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
