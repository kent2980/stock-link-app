import { Box, Button } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

import "swiper/css";
// Import Swiper styles
import { Link as RouterLink } from "@tanstack/react-router";
import "swiper/css/effect-cube";
import "swiper/css/navigation";
import "swiper/css/pagination";
import "swiper/css/scrollbar";
import { EffectCube, Navigation, Pagination, Scrollbar } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/react";

export const Route = createFileRoute("/_layout/menu")({
  component: Menu,
});

function Menu() {
  return (
    <Swiper
      modules={[Navigation, Pagination, Scrollbar, EffectCube]}
      spaceBetween={0}
      slidesPerView={1}
      //   freeMode={{ enabled: true, sticky: true }}
      pagination={{ clickable: true }}
      scrollbar={{ draggable: true }}
      onSwiper={(swiper) => console.log(swiper)}
      onSlideChange={() => console.log("slide change")}
      effect="cube"
      cubeEffect={{
        shadow: false,
        slideShadows: true,
        shadowOffset: 20,
        shadowScale: 0.94,
      }}
    >
      <SwiperSlide>
        <Box width="100vw" height="100vh">
          <Button as={RouterLink} to="/navigate/">
            Go to Summary
          </Button>
        </Box>
      </SwiperSlide>
      <SwiperSlide>
        <Box width="100vw" height="100vh">
          Slide2
        </Box>
      </SwiperSlide>
      <SwiperSlide>
        <Box width="100vw" height="100vh">
          Slide3
        </Box>
      </SwiperSlide>
    </Swiper>
  );
}
