import { FinancialSummaryService } from "@/client";
import {
  Box,
  FormatNumber,
  Stack,
  Table,
  Text,
  VStack,
} from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { StackDirection } from "node_modules/@chakra-ui/react/dist/types/components/stack/get-separator-style";
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
    gcTime: 30 * 24 * 60 * 60 * 1000, // 30 days
    staleTime: 30 * 24 * 60 * 60 * 1000, // 30 days
  });
  const FormatValue = (item: any, direction: StackDirection | undefined) => {
    const value = item?.value;
    const scale = item?.display_scale;
    if (value === null || value === undefined) {
      return <Text>-</Text>;
    }
    return (
      <Stack gap={{ base: 0, md: 2 }} direction={direction} alignItems="center">
        <FormatNumber value={value} />
        <Text fontSize={"8px"}>{scale ? ` ${scale}` : ""}</Text>
      </Stack>
    );
  };
  return (
    <>
      <Table.Root size={{ base: "sm", md: "md" }}>
        <Table.ColumnGroup>
          <Table.Column htmlWidth="5%" />
          {Array.from({ length: 4 }, (_, index) => {
            return <Table.Column key={`column-${index}`} htmlWidth="20%" />;
          })}
        </Table.ColumnGroup>
        <Table.Header>
          <Table.Row>
            <Table.ColumnHeader textAlign="center">期間</Table.ColumnHeader>
            {data.data?.map((item, index) => {
              if (index > 3) return null;
              return (
                <Table.ColumnHeader
                  key={`header-${index}`}
                  textAlign="center"
                  // w={`${100 / count + 1}%`}
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
              if (key > 3) return null;
              return (
                <Table.Cell w="22%" key={`cell-${key}`}>
                  <VStack>
                    <Box
                      key={`curValue-${key}`}
                      textAlign="center"
                      display="flex"
                      flexDirection="column"
                      alignItems="center"
                      justifyContent="center"
                    >
                      {FormatValue(item.result?.curValue, "column")}
                    </Box>
                    <Box
                      key={`result3-${key}`}
                      textAlign="center"
                      display="flex"
                      flexDirection="column"
                      alignItems="center"
                      justifyContent="center"
                    >
                      {FormatValue(item.result?.curChange, "row")}
                    </Box>
                  </VStack>
                </Table.Cell>
              );
            })}
          </Table.Row>
          <Table.Row>
            <Table.ColumnHeader textAlign="center">前期実績</Table.ColumnHeader>
            {data.data?.map((item, index) => {
              if (index > 3) return null;
              return (
                <Table.Cell key={`cell3-${index}`}>
                  <Box
                    key={`result3-${index}`}
                    textAlign="center"
                    display="flex"
                    flexDirection="column"
                    alignItems="center"
                    justifyContent="center"
                  >
                    {FormatValue(item.result?.preValue, "column")}
                  </Box>
                  <Box
                    key={`result4-${index}`}
                    textAlign="center"
                    display="flex"
                    flexDirection="column"
                    alignItems="center"
                    justifyContent="center"
                  >
                    {FormatValue(item.result?.preChange, "row")}
                  </Box>
                </Table.Cell>
              );
            })}
          </Table.Row>
        </Table.Body>
      </Table.Root>
    </>
  );
};
export default BusinessResultTable;
