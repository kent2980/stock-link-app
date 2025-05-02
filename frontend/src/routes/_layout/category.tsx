import Calender from "@/components/Category/Calender";
import Industry33 from "@/components/Category/Industry_33";
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
    <>
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
              <Industry33 />
            </Suspense>
          </ErrorBoundary>
        </SwiperSlide>
      </Swiper>
    </>
  );
}
