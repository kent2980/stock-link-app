import {
  Badge,
  Skeleton,
  Table,
  TableContainer,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
} from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useNavigate } from "@tanstack/react-router";
import React, { Suspense } from "react";
import { JpxService, JpxStockInfoPublic } from "../../client";

interface ItemListProps {
  industry33Code: number[] | null;
  isItems: boolean;
}

const ItemList: React.FC<ItemListProps> = ({ industry33Code, isItems }) => {
  return (
    <TableContainer p={4}>
      <Table size={"sm"} variant={"striped"}>
        <Thead>
          <Tr>
            <Th textAlign="center" bg="blue.600" color={"white"}>
              コード
            </Th>
            <Th bg="blue.600" color={"white"}>
              名称
            </Th>
            <Th textAlign="center" bg="blue.600" color={"white"}>
              市場
            </Th>
            <Th textAlign="center" bg="blue.600" color={"white"}>
              業種
            </Th>
            <Th textAlign="center" bg="blue.600" color={"white"}>
              更新日
            </Th>
          </Tr>
        </Thead>
        <Suspense
          fallback={
            <Tbody>
              {Array(20).map((_, index) => (
                <Tr key={index}>
                  <Td colSpan={5}>
                    <Skeleton height="20px" />
                  </Td>
                </Tr>
              ))}
            </Tbody>
          }
        >
          <CustomTbody industry33Code={industry33Code} isItems={isItems} />
        </Suspense>
      </Table>
    </TableContainer>
  );
};

export default ItemList;

const CustomTbody: React.FC<ItemListProps> = ({ industry33Code, isItems }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["StockInfo", industry33Code, isItems],
    queryFn: async () => {
      return await JpxService.readJpxStockInfoItemsTcs({
        industry33Code: industry33Code,
        limit: 500,
        isItems: isItems,
      });
    },
  });
  return (
    <Tbody>
      {data?.data.map((item) => {
        return <ItemInfo key={item.code} item={item} />;
      })}
    </Tbody>
  );
};

const ItemInfo: React.FC<{ item: JpxStockInfoPublic }> = ({ item }) => {
  const market_dict: { [key: string]: string } = {
    プライム: "Prime",
    スタンダード: "Standard",
    グロース: "Growth",
  };
  function getBadgeColor(market: string) {
    switch (market) {
      case "Prime":
        return "blue";
      case "Standard":
        return "green";
      case "Growth":
        return "red";
      default:
        return "gray";
    }
  }
  const marketName = market_dict[item.market_or_type.replace("(内国株式)", "")];
  const navigate = useNavigate({ from: "/industries" });
  const handleRowClick = (code: string) => {
    navigate({ to: "/StockIndex/$code", params: { code: code } });
  };
  return (
    <Tr onClick={() => handleRowClick(item.code)} cursor="pointer">
      <Td textAlign="center">
        <Badge colorScheme="teal" variant="solid" fontWeight="800">
          {item.code}
        </Badge>
      </Td>
      <Td fontWeight="700" color="gray.700">
        {item.name}
      </Td>
      <Td textAlign="center">
        <Badge
          colorScheme={getBadgeColor(marketName)}
          variant="solid"
          minW={"80px"}
        >
          {marketName}
        </Badge>
      </Td>
      <Td textAlign="center" fontWeight="700" color="gray.600">
        {item.industry_33_name}
      </Td>
      <Td textAlign="center"></Td>
    </Tr>
  );
};
