import Calender from "@/components/Category/Calender";
import Industry17 from "@/components/Category/Industry_17";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";
import "swiper/css";
import { Swiper, SwiperSlide } from "swiper/react";

export const Route = createFileRoute("/_layout/category")({
  component: Category,
});

function Category() {
  return (
    <Box>
      <Swiper loop={true}>
        <SwiperSlide>
          <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
            <Suspense fallback={<div>Loading...</div>}>
              <Calender />
            </Suspense>
          </ErrorBoundary>
        </SwiperSlide>
        <SwiperSlide>
          <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
            <Suspense fallback={<div>Loading...</div>}>
              <Industry17 />
            </Suspense>
          </ErrorBoundary>
        </SwiperSlide>
      </Swiper>
    </Box>
  );
}
