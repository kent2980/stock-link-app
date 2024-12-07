import { Box } from "@chakra-ui/react";
import React from "react";
import {
  edjp_FinancialReportSummary_NonCon_Q1,
  edjp_FinancialReportSummary_NonCon_Q2,
} from "../../../../client";

const NonConQuarterSummary: React.FC<{
  data:
    | edjp_FinancialReportSummary_NonCon_Q1
    | edjp_FinancialReportSummary_NonCon_Q2;
}> = ({ data }) => {
  return (
    <Box>
      <h1>NonConQuarterSummary</h1>
    </Box>
  );
};

export default NonConQuarterSummary;
