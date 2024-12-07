import { Box } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import { createFileRoute } from "@tanstack/react-router";
import {
  edjp,
  edjp_FinancialReportSummary_Con_FY,
  edjp_FinancialReportSummary_Con_HY_spec,
  edjp_FinancialReportSummary_Con_Q1,
  edjp_FinancialReportSummary_Con_Q2,
  edjp_FinancialReportSummary_Con_Q3,
  edjp_FinancialReportSummary_NonCon_FY,
  edjp_FinancialReportSummary_NonCon_Q1,
  edjp_FinancialReportSummary_NonCon_Q2,
  SummaryService,
} from "../../../../client";
import ConFYSummary from "../../../../components/Summary/Contents/edjp/ConFySummary";
import ConQuarterSpecSummary from "../../../../components/Summary/Contents/edjp/ConQuarterSpecSummary";
import ConQuarterSummary from "../../../../components/Summary/Contents/edjp/ConQuarterSummary";
import NonConFYSummary from "../../../../components/Summary/Contents/edjp/NonConFYSummary";
import NonConQuarterSummary from "../../../../components/Summary/Contents/edjp/NonConQuarterSummary";
export const Route = createFileRoute("/_layout/summary/$head_item_key/edjp")({
  component: () => <Summary />,
});

function Summary() {
  const { head_item_key } = Route.useParams();
  const { data, isPending, isError } = useQuery({
    queryKey: ["SummaryNonFraction", head_item_key],
    queryFn: async () => {
      return SummaryService.getSummaryNonFractionItemsHeadItemKey({
        headItemKey: head_item_key,
      });
    },
    gcTime: 1000 * 60 * 60 * 24,
    staleTime: 1000 * 60 * 60 * 24,
  });
  const {
    data: fracData,
    isPending: fracIsPending,
    isError: fracIsError,
  } = useQuery({
    queryKey: ["SummaryNonNumeric", head_item_key],
    queryFn: async () => {
      return SummaryService.getSummaryNonNumericItemsHeadItemKey({
        headItemKey: head_item_key,
      });
    },
    gcTime: 1000 * 60 * 60 * 24,
    staleTime: 1000 * 60 * 60 * 24,
  });

  if (isPending || fracIsPending) {
    return <Box>Loading...</Box>;
  }

  if (isError || fracIsError) {
    return <Box>Error</Box>;
  }

  /**
   *  連結四半期決算短信かどうか？
   * @param data
   * @returns
   */
  function isConQuarterSummary(
    data: any
  ): data is
    | edjp_FinancialReportSummary_Con_Q1
    | edjp_FinancialReportSummary_Con_Q2
    | edjp_FinancialReportSummary_Con_Q3 {
    return (
      data.type === "edjp_FinancialReportSummary_Con_Q1" ||
      data.type === "edjp_FinancialReportSummary_Con_Q2" ||
      data.type === "edjp_FinancialReportSummary_Con_Q3"
    );
  }

  /**
   * 非連結四半期決算短信かどうか？
   * @param data
   * @returns
   */
  function isNonConQuarterSummary(
    data: any
  ): data is
    | edjp_FinancialReportSummary_NonCon_Q1
    | edjp_FinancialReportSummary_NonCon_Q2 {
    return (
      data.type === "edjp_FinancialReportSummary_NonCon_Q1" ||
      data.type === "edjp_FinancialReportSummary_NonCon_Q2"
    );
  }

  /**
   * 特定事業の連結四半期決算短信かどうか？
   * @param data
   * @returns
   */
  function isConQuarterSpecSummary(
    data: any
  ): data is edjp_FinancialReportSummary_Con_HY_spec {
    return data.type === "edjp_FinancialReportSummary_Con_HY_spec";
  }

  /**
   * 連結年度決算短信かどうか？
   * @param data
   * @returns
   */
  function isConFYSummary(
    data: any
  ): data is edjp_FinancialReportSummary_Con_FY {
    return data.type === "edjp_FinancialReportSummary_Con_FY";
  }

  /**
   * 非連結年度決算短信かどうか？
   * @param data
   * @returns
   */
  function isNonConFYSummary(
    data: any
  ): data is edjp_FinancialReportSummary_NonCon_FY {
    return data.type === "edjp_FinancialReportSummary_NonCon_FY";
  }

  function isEdjoFraction(data: any): data is edjp {
    return data.type === "edjp";
  }

  if (isConQuarterSummary(data)) {
    return <ConQuarterSummary data={data} fracData={fracData} />;
  }

  if (isNonConQuarterSummary(data)) {
    return <NonConQuarterSummary data={data} />;
  }

  if (isConQuarterSpecSummary(data)) {
    return <ConQuarterSpecSummary data={data} />;
  }

  if (isConFYSummary(data)) {
    return <ConFYSummary data={data} />;
  }

  if (isNonConFYSummary(data)) {
    return <NonConFYSummary data={data} />;
  }

  return (
    <Box>
      <h1>Summary</h1>
    </Box>
  );
}
