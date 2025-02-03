import { Box, BoxProps, Skeleton, Text, VStack } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useStore } from "@tanstack/react-store";
import { Suspense } from "react";
import { IndustriesStore } from "../../Store/IndustriesStore";
import { JpxService } from "../../client";

function Sidebar(props: BoxProps) {
  return (
    <Box {...props} bg="gray.100" boxShadow="md" borderRadius="xl">
      <VStack spacing={0} m={2}>
        <Suspense
          fallback={Array(18).map((_, index) => (
            <Skeleton key={index} h="20px" w="100px" />
          ))}
        >
          <SidebarItems />
        </Suspense>
      </VStack>
    </Box>
  );
}

export default Sidebar;

const SidebarItems: React.FC = () => {
  const { data: industry } = useSuspenseQuery({
    queryKey: ["Industries_17"],
    queryFn: async () => {
      return await JpxService.readJpxStockInfoIndustryNames({
        type: 17,
      });
    },
    staleTime: 1000 * 60 * 60 * 24 * 30, // 30 days
    gcTime: 1000 * 60 * 60 * 24 * 30, // 30 days
  });

  const { industry17Code: code } = useStore(IndustriesStore, (state) => state);
  return (
    <>
      {/* 先頭のサイドバーアイテム */}
      <SidebarItem key={0} selectedCode={code} code={0}>
        全て
      </SidebarItem>
      {industry?.data.map((item) => {
        return (
          // itemから生成したサイドバーアイテム
          <SidebarItem key={item.code} code={item.code} selectedCode={code}>
            {item.name}
          </SidebarItem>
        );
      })}
    </>
  );
};

const SidebarItem: React.FC<{
  code: number;
  selectedCode: number | null;
  children: React.ReactNode;
}> = ({ code, selectedCode, children }) => {
  function handleClick(code: number) {
    IndustriesStore.setState((state) => {
      return {
        ...state,
        industry17Code: code,
      };
    });
  }

  return (
    <Box
      bg={selectedCode === code ? "blue.500" : "transparent"}
      color={selectedCode === code ? "white" : "black"}
      fontWeight={selectedCode === code ? "bold" : "normal"}
      cursor="pointer"
      onClick={() => handleClick(code)}
      w={"100%"}
      py={2}
      borderBottom={
        selectedCode === code ? "1px solid" : "1px solid transparent"
      }
      borderColor={selectedCode === code ? "blue.500" : "gray.400"}
    >
      <Text textAlign="center">{children}</Text>
    </Box>
  );
};
