import IRCard from "@/components/Index/IRCard";
import {
  Center,
  Container,
  Flex,
  IconButton,
  Input,
  Wrap,
} from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { useEffect } from "react";
import { BsSearch } from "react-icons/bs";
import { HeaderAddressItem, HeaderStore } from "../../Store/HeaderStore";

export const Route = createFileRoute("/_layout/")({
  component: Index,
});

function Index() {
  const items: HeaderAddressItem[] = [
    {
      label: "Top",
      href: "/",
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

  return (
    <Container>
      {/* 検索バー */}
      <Center>
        <Flex gap={2} mt={2}>
          <Input placeholder="Search..." />
          <IconButton aria-label="Search database">
            <BsSearch />
          </IconButton>
        </Flex>
      </Center>
      <Wrap gap={2} mt={4}>
        <IRCard select_date={null} />
      </Wrap>
    </Container>
  );
}
