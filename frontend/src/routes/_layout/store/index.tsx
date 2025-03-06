import { Center } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { Suspense } from "react";
import StoreTable from "./-componenets/StoreTable";
export const Route = createFileRoute("/_layout/store/")({
  component: Index,
});

function Index() {
  return (
    <Center gap={2} direction="column">
      {/* <Icon size="md" color="gray.500">
        <VscError />
      </Icon>
      <Text>表示するデータがありません。</Text> */}
      <Suspense fallback={<div>Loading...</div>}>
        <StoreTable />
      </Suspense>
    </Center>
  );
}
