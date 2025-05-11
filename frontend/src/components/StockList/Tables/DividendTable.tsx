import { FinancialSummaryService, FinValueBase } from "@/client";
import { Table, VStack } from "@chakra-ui/react";
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

  const period = data.period?.period;
  const value = data.data;
  const first = value?.FirstQuarterMember;
  const second = value?.SecondQuarterMember;
  const third = value?.ThirdQuarterMember;
  const yearEnd = value?.YearEndMember;
  const annual = value?.AnnualMember;
  const total = value?.TotalDividendPaidAnnual;
  const payRatio = value?.PayoutRatio;
  const netAssetDividendRate = value?.RatioTotalAmountOfDividendTotalNetAssets;

  const getFormatValue = (item: FinValueBase | null | undefined) => {
    const value = item?.value;
    const scale = item?.display_scale;
    if (value === null || value === undefined) {
      return "-";
    }
    return value?.toString() + (scale ? ` ${scale}` : "");
  };

  return (
    <VStack gap={3}>
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
              昨年度実績
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
              {period === "FY" ? "来季予想" : "今期予想"}
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
      {period === "FY" && (
        <Table.Root size={"sm"}>
          <Table.Header>
            <Table.Row>
              <Table.ColumnHeader textAlign="center">期間</Table.ColumnHeader>
              <Table.ColumnHeader textAlign="center">配当金</Table.ColumnHeader>
              <Table.ColumnHeader textAlign="center">
                配当性向
              </Table.ColumnHeader>
              <Table.ColumnHeader textAlign="center">
                純資産配当率
              </Table.ColumnHeader>
            </Table.Row>
          </Table.Header>
          <Table.Body>
            <Table.Row>
              <Table.Cell textAlign="center" width="16.66%">
                昨年実績
              </Table.Cell>
              <Table.Cell textAlign="center" width="16.66%">
                {getFormatValue(total?.result?.preValue)}
              </Table.Cell>
              <Table.Cell textAlign="center" width="16.66%">
                {getFormatValue(payRatio?.result?.preValue)}
              </Table.Cell>
              <Table.Cell textAlign="center" width="16.66%">
                {getFormatValue(netAssetDividendRate?.result?.preValue)}
              </Table.Cell>
            </Table.Row>
            <Table.Row>
              <Table.Cell textAlign="center" width="16.66%">
                今期実績
              </Table.Cell>
              <Table.Cell textAlign="center" width="16.66%">
                {getFormatValue(total?.result?.curValue)}
              </Table.Cell>
              <Table.Cell textAlign="center" width="16.66%">
                {getFormatValue(payRatio?.result?.curValue)}
              </Table.Cell>
              <Table.Cell textAlign="center" width="16.66%">
                {getFormatValue(netAssetDividendRate?.result?.curValue)}
              </Table.Cell>
            </Table.Row>
            <Table.Row>
              <Table.Cell textAlign="center" width="16.66%">
                {period === "FY" ? "来期予想" : "今期予想"}
              </Table.Cell>
              <Table.Cell textAlign="center" width="16.66%">
                {getFormatValue(total?.forecast?.curValue)}
              </Table.Cell>
              <Table.Cell textAlign="center" width="16.66%">
                {getFormatValue(payRatio?.forecast?.curValue)}
              </Table.Cell>
              <Table.Cell textAlign="center" width="16.66%">
                {getFormatValue(netAssetDividendRate?.forecast?.curValue)}
              </Table.Cell>
            </Table.Row>
          </Table.Body>
        </Table.Root>
      )}
    </VStack>
  );
};
export default DividendTable;
