import { Box, HStack } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import { useEffect, useState } from "react";
import CustomCheckboxArea from "../../components/Industries/CustomCheckboxArea";
import Sidebar from "../../components/Industries/Sidebar";
import { HeaderAddressItem, HeaderStore } from "../../Store/HeaderStore";
import { IndustriesStore } from "../../Store/IndustriesStore";

export const Route = createFileRoute("/_layout/industries")({
  component: Industries,
});

function Industries() {
  const items: HeaderAddressItem[] = [
    {
      label: "Top",
      href: "/",
    },
    {
      label: "業種別",
      href: "/industries",
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
  const { industry33Code } = useStore(IndustriesStore, (state) => state);
  const { height } = useStore(HeaderStore, (state) => state);
  const [isItems, setIsItems] = useState(true);
  useEffect(() => {
    if (industry33Code) {
      if (industry33Code.length > 0) {
        setIsItems(true);
      } else {
        setIsItems(false);
      }
    }
  }, [industry33Code]);
  return (
    <Box>
      <HStack alignItems="flex-start">
        <Sidebar
          position="fixed"
          top={height}
          left="0"
          h="100vh"
          w="20%"
          overflowY="auto"
          css={{
            "&::-webkit-scrollbar": {
              display: "none",
            },
            msOverflowStyle: "none",
            scrollbarWidth: "none",
          }}
        />
        <Box flex="1" ml="20%">
          <CustomCheckboxArea />
          {/* <ItemList industry33Code={industry33Code} isItems={isItems} /> */}
        </Box>
      </HStack>
    </Box>
  );
}
