import { VStack } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { useEffect, useRef, useState } from "react";
import "swiper/css";
import "swiper/css/pagination";
import Contents from "../../components/Index/Contents";
import Header from "../../components/Index/Header";
import ShortHeader from "../../components/Index/ShortHeader";
import "../../styles.css";

export const Route = createFileRoute("/_layout/")({
  component: Dashboard,
});

function Dashboard() {
  const headerRef = useRef<HTMLDivElement>(null);
  const [headerHidden, setHeaderHidden] = useState(true);

  useEffect(() => {
    const handleScroll = () => {
      if (headerRef.current) {
        setHeaderHidden(window.scrollY < headerRef.current.clientHeight);
      }
    };
    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);
  return (
    <VStack>
      <ShortHeader position="fixed" top="60px" left="0" hidden={headerHidden} />
      <Header ref={headerRef} />
      <Contents />
    </VStack>
  );
}
