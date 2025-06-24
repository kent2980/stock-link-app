import { JpxService } from "@/client";
import { Badge, Box } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";
import "swiper/css";
import "swiper/css/navigation";
import { Pagination } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/react";
import DisclosurePage from "./Disclosure";

const DisclosureIndex: React.FC = () => {
  const { data } = useSuspenseQuery({
    queryKey: ["disclosureIndex", 17],
    queryFn: async () => {
      return await JpxService.readIndustryCount({
        type: 17,
      });
    },
  });

  return (
    <>
      <Swiper
        pagination={true}
        modules={[Pagination]}
        className="mySwiper"
        loop={true}
      >
        {data.data.map((item) => (
          <SwiperSlide key={item.code}>
            <Box height="100vh" display="flex" flexDirection="column">
              <Badge
                colorPalette="green"
                textAlign="center"
                fontSize="md"
                h="40px"
                display="flex"
                justifyContent="center"
                alignItems="center"
              >
                {item.name}
              </Badge>
              <Box>
                <DisclosurePage code_17={item.code} />
              </Box>
            </Box>
          </SwiperSlide>
        ))}
      </Swiper>
    </>
  );
};

export default DisclosureIndex;
