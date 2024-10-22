import { Box, Spinner, Stack } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";
import { Swiper, SwiperSlide } from "swiper/react";
import { XbrlViewService } from "../../client";
import StockSummary from "../../components/summary/StockSummary";
import SummaryBox from "../../components/summary/SummaryBox";
import SummaryHeader from "../../components/summary/SummaryHeader";
import SummaryQualitative from "../../components/summary/SummaryQualitative";

export const Route = createFileRoute("/_layout/summary/$xbrl_id")({
  component: Summary,
});

function Summary() {
  const { xbrl_id } = Route.useParams();
  const { data: item, status } = useQuery({
    queryKey: ["head", xbrl_id],
    queryFn: () =>
      XbrlViewService.readHeadItem({
        xbrlId: xbrl_id,
      }),
  });

  if (status === "error") {
    return <Box>Error</Box>;
  }

  if (status === "pending") {
    return (
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        height="100vh"
        width="100%"
      >
        <Spinner
          size="xl"
          thickness="10px"
          speed="1s"
          emptyColor="gray.200"
          color="blue.500"
        />
      </Box>
    );
  }

  // モバイルの場合
  if (window.innerWidth < 768) {
    return (
      <>
        <SummaryHeader xbrl_id={xbrl_id} />
        <Swiper
          spaceBetween={50}
          slidesPerView={1}
          loop={true}
          onSwiper={(swiper) => console.log(swiper)}
          onSlideChange={() => console.log("slide change")}
        >
          <SwiperSlide>
            <SummaryBox xbrl_id={xbrl_id} className="swiper-child" />
          </SwiperSlide>
          <SwiperSlide>
            <SummaryQualitative xbrl_id={xbrl_id} className="swiper-child" />
          </SwiperSlide>
          <SwiperSlide>
            <StockSummary
              code={item.securities_code}
              className="swiper-child"
            />
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
