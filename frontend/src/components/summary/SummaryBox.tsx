import { Box, BoxProps, Spinner, Stack } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import React from "react";
import { XbrlViewService } from "../../client";
import DividendGraphArea from "./graph/DividendGraphArea";
import OperatingGraphArea from "./graph/OperatingGraphArea";
import DividendTableArea from "./table/DividendTableArea";
import OperatingTableArea from "./table/OperatingTableArea";

interface SummaryBoxProps extends BoxProps {
  xbrl_id: string;
}
const SummaryBox: React.FC<SummaryBoxProps> = ({ xbrl_id, ...props }) => {
  const { data: items, status } = useQuery({
    queryKey: ["summary", xbrl_id],
    queryFn: () =>
      XbrlViewService.readSummaryItemByXbrlId({
        xbrlId: xbrl_id,
      }),
    staleTime: 1000 * 60 * 60 * 24 * 7,
    gcTime: 1000 * 60 * 60 * 24 * 30,
  });

  if (status === "error") {
    return <Box>Error</Box>;
  }

  if (status === "pending") {
    return (
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        height="100vh"
        width="100%"
      >
        <Spinner
          size="xl"
          thickness="10px"
          speed="1s"
          emptyColor="gray.200"
          color="blue.500"
        />
      </Box>
    );
  }

  const info = items.DocumentEntityInformation;
  const ope =
    items.OperatingResult?.OperatingResultsAbstract
      ?.IncomeStatementsInformationAbstract;
  const forecast = items.Forecasts;
  const dividend = items.Dividends;
  const assets = items.BusinessResultsFinancialPositions?.FinancialPositions;
  const stock =
    items.NotesNumberIssuedOutstandingSharesCommonStock
      ?.NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock
      ?.numeric ?? 0;

  return (
    <Box {...props}>
      <Stack
        direction={"column"}
        spacing={4}
        p={2}
        w="100%"
        maxW="720px"
        m="auto"
      >
        <OperatingTableArea
          label="経営成績"
          netSales={ope?.NetSales}
          operatingIncome={ope?.OperatingIncome}
          ordinaryIncome={ope?.OrdinaryIncome}
          profit={ope?.Profit}
        />
        <OperatingGraphArea
          netSales={ope?.NetSales?.ChangeIn?.numeric ?? 0}
          operatingIncome={ope?.OperatingIncome?.ChangeIn?.numeric ?? 0}
          ordinaryIncome={ope?.OrdinaryIncome?.ChangeIn?.numeric ?? 0}
          profit={ope?.Profit?.ChangeIn?.numeric ?? 0}
        />
        <DividendTableArea
          label="配当情報"
          quarter={info?.QuarterlyPeriod?.value ?? ""}
          dividend={dividend}
        />
        <DividendGraphArea
          asset={assets}
          dividend={dividend}
          stock={stock}
          quarter={info?.QuarterlyPeriod?.value ?? ""}
        />
        <OperatingTableArea
          label="業績予想"
          netSales={forecast?.NetSales}
          operatingIncome={forecast?.OperatingIncome}
          ordinaryIncome={forecast?.OrdinaryIncome}
          profit={forecast?.ProfitAttributableToOwnersOfParent}
        />
        <OperatingGraphArea
          netSales={forecast?.NetSales?.ChangeIn?.numeric ?? 0}
          operatingIncome={forecast?.OperatingIncome?.ChangeIn?.numeric ?? 0}
          ordinaryIncome={forecast?.OrdinaryIncome?.ChangeIn?.numeric ?? 0}
          profit={
            forecast?.ProfitAttributableToOwnersOfParent?.ChangeIn?.numeric ?? 0
          }
        />
      </Stack>
    </Box>
  );
};

export default SummaryBox;
