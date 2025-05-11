import { FinancialSummaryService, FinValueBase } from "@/client";
import { Box, Table } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";

interface DividendTableProps {
  HeadItemKey: string;
}
const DividendTable: React.FC<DividendTableProps> = ({ HeadItemKey }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["Dividend", HeadItemKey],
    queryFn: async () => {
      return await FinancialSummaryService.getDividends({
        headItemKey: HeadItemKey,
      });
    },
  });
  const value = data.data;
  const first = value?.FirstQuarterMember;
  const second = value?.SecondQuarterMember;
  const third = value?.ThirdQuarterMember;
  const yearEnd = value?.YearEndMember;
  const annual = value?.AnnualMember;

  const getFormatValue = (item: FinValueBase | null | undefined) => {
    const value = item?.value;
    const scale = item?.display_scale;
    if (value === null || value === undefined) {
      return "-";
    }
    return value?.toString() + (scale ? ` ${scale}` : "");
  };

  return (
    <Box>
      <Table.Root size={"sm"}>
        <Table.Header>
          <Table.Row>
            <Table.ColumnHeader textAlign="center" width="16.66%">
              期間
            </Table.ColumnHeader>
            <Table.ColumnHeader textAlign="center" width="16.66%">
              {first?.label}
            </Table.ColumnHeader>
            <Table.ColumnHeader textAlign="center" width="16.66%">
              {second?.label}
            </Table.ColumnHeader>
            <Table.ColumnHeader textAlign="center" width="16.66%">
              {third?.label}
            </Table.ColumnHeader>
            <Table.ColumnHeader textAlign="center" width="16.66%">
              {yearEnd?.label}
            </Table.ColumnHeader>
            <Table.ColumnHeader textAlign="center" width="16.66%">
              {annual?.label}
            </Table.ColumnHeader>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          <Table.Row>
            <Table.Cell textAlign="center" width="16.66%">
              昨年度
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(first?.result?.preValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(second?.result?.preValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(third?.result?.preValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(yearEnd?.result?.preValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(annual?.result?.preValue)}
            </Table.Cell>
          </Table.Row>
          <Table.Row>
            <Table.Cell textAlign="center" width="16.66%">
              今期実績
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(first?.result?.curValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(second?.result?.curValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(third?.result?.curValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(yearEnd?.result?.curValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(annual?.result?.curValue)}
            </Table.Cell>
          </Table.Row>
          <Table.Row>
            <Table.Cell textAlign="center" width="16.66%">
              今期予想
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(first?.forecast?.curValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(second?.forecast?.curValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(third?.forecast?.curValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(yearEnd?.forecast?.curValue)}
            </Table.Cell>
            <Table.Cell textAlign="center" width="16.66%">
              {getFormatValue(annual?.forecast?.curValue)}
            </Table.Cell>
          </Table.Row>
        </Table.Body>
      </Table.Root>
    </Box>
  );
};
export default DividendTable;
