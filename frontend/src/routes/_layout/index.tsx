import { Container } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import "swiper/css";
import "swiper/css/pagination";
import "../../styles.css";

import Home from "../../components/Index/Home";

export const Route = createFileRoute("/_layout/")({
  component: Dashboard,
});

function Dashboard() {
  return (
    <>
      <Container maxW="full" height="100vh">
        <Home />
      </Container>
    </>
  );
}
