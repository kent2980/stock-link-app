import { FinancialSummaryService } from "@/client";
import { Table } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";

interface BusinessResultTableProps {
  HeadItemKey: string;
}

const BusinessResultTable: React.FC<BusinessResultTableProps> = ({
  HeadItemKey,
}) => {
  const { data } = useSuspenseQuery({
    queryKey: ["BusinessResult", HeadItemKey],
    queryFn: async () => {
      return await FinancialSummaryService.getOperatingResults({
        headItemKey: HeadItemKey,
      });
    },
  });
  const count = data.data?.length ?? 0;
  return (
    <>
      <Table.Root size={{ base: "sm", md: "md" }} minW="100%" maxW={"100%"}>
        <Table.Header>
          <Table.Row>
            <Table.ColumnHeader textAlign="center" minW="70px">
              期間
            </Table.ColumnHeader>
            {data.data?.map((item, key) => {
              return (
                <Table.ColumnHeader
                  key={key}
                  textAlign="center"
                  w={`${100 / count + 1}%`}
                  colSpan={2}
                >
                  {item.label}
                </Table.ColumnHeader>
              );
            })}
          </Table.Row>
        </Table.Header>
        <Table.Body>
          <Table.Row>
            <Table.ColumnHeader textAlign="center">今期実績</Table.ColumnHeader>
            {data.data?.map((item, key) => {
              return (
                <>
                  <Table.Cell
                    key={key}
                    textAlign="center"
                    fontSize={{ base: "12px", md: "14px" }}
                  >
                    {item.result?.curValue?.value}
                  </Table.Cell>
                  <Table.Cell
                    key={key}
                    textAlign="center"
                    fontSize={{ base: "12px", md: "14px" }}
                  >
                    {item.result?.curChange?.value}
                  </Table.Cell>
                </>
              );
            })}
          </Table.Row>
          <Table.Row>
            <Table.ColumnHeader textAlign="center">前期実績</Table.ColumnHeader>
            {data.data?.map((item, key) => {
              return (
                <>
                  <Table.Cell
                    key={key}
                    textAlign="center"
                    fontSize={{ base: "12px", md: "14px" }}
                  >
                    {item.result?.preValue?.value}
                  </Table.Cell>
                  <Table.Cell
                    key={key}
                    textAlign="center"
                    fontSize={{ base: "12px", md: "14px" }}
                  >
                    {item.result?.preChange?.value}
                  </Table.Cell>
                </>
              );
            })}
          </Table.Row>
        </Table.Body>
      </Table.Root>
    </>
  );
};
export default BusinessResultTable;
