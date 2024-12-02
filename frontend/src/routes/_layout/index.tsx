import { VStack } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import "swiper/css";
import "swiper/css/pagination";
import Contents from "../../components/Index/Contents";
import Header from "../../components/Index/Header";
import "../../styles.css";

export const Route = createFileRoute("/_layout/")({
  component: Dashboard,
});

function Dashboard() {
  return (
    <VStack>
      <Header />
      <Contents />
    </VStack>
  );
}
