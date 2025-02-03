import { Box, Container, Flex, Spinner, VStack } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense, useEffect, useState } from "react";
import DocumentList from "../../components/StockIndex/DocumentList";
import StockInfo from "../../components/StockIndex/StockInfo";
import Summary from "../../components/StockIndex/Summary";
import { HeaderAddressItem, HeaderStore } from "../../Store/HeaderStore";

export const Route = createFileRoute("/_layout/StockIndex/$code")({
  component: StockIndex,
});

function StockIndex() {
  const { code } = Route.useParams();
  const items: HeaderAddressItem[] = [
    {
      label: "Top",
      href: "/",
    },
    {
      label: "業種別",
      href: "/industries",
    },
    {
      label: code,
      href: "",
    },
  ];
  useEffect(() => {
    HeaderStore.setState((state) => {
      return {
        ...state,
        HeaderAddressItems: items,
      };
    });
  }, []);
  const [isSummary, setIsSummary] = useState(false);
  const handleSummaryClick = () => {
    setIsSummary(true);
  };
  const handlePerformanceClick = () => {
    setIsSummary(false);
  };
  return (
    <Container maxW="container.xl" p={4}>
      <VStack spacing={4}>
        <Suspense fallback={<div>Loading...</div>}>
          <StockInfo code={code} />
        </Suspense>
        <Flex gap={4}>
          <Box
            color={isSummary ? "gray.500" : "black"}
            fontWeight={isSummary ? 500 : 800}
            onClick={handlePerformanceClick}
            cursor="pointer"
          >
            業績推移
          </Box>
          <Box
            color={isSummary ? "black" : "gray.500"}
            fontWeight={isSummary ? 800 : 500}
            onClick={handleSummaryClick}
            cursor="pointer"
          >
            決算サマリ
          </Box>
        </Flex>
        <Suspense fallback={<Spinner />}>
          {isSummary ? (
            <>
              <DocumentList code={code} />
              <Summary />
            </>
          ) : (
            <Box></Box>
          )}
        </Suspense>
      </VStack>
    </Container>
  );
}
