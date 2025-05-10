import Calender from "@/components/Category/Calender";
import Industry33 from "@/components/Category/Industry_33";
import CustomSpinner from "@/components/Spinner/CustomSpinner";
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
    <Box
      data-state="open"
      _open={{
        animation: "fade-in 500ms ease-out",
      }}
    >
      <Swiper loop={true}>
        <SwiperSlide>
          <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
            <Suspense fallback={<CustomSpinner />}>
              <Calender />
            </Suspense>
          </ErrorBoundary>
        </SwiperSlide>
        <SwiperSlide>
          <ErrorBoundary fallback={<div>表示するデータがありません。</div>}>
            <Suspense fallback={<CustomSpinner />}>
              <Industry33 />
            </Suspense>
          </ErrorBoundary>
        </SwiperSlide>
      </Swiper>
    </Box>
  );
}
