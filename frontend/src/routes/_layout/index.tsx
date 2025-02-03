import { Container } from "@chakra-ui/react";
import { createFileRoute, Link } from "@tanstack/react-router";
import { useEffect } from "react";
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
      <Link to="/industries">Industries</Link>
    </Container>
  );
}
