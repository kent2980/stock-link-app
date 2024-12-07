import { Box } from "@chakra-ui/react";
import React from "react";
import { edjp_FinancialReportSummary_NonCon_FY } from "../../../../client";

const NonConFYSummary: React.FC<{
  data: edjp_FinancialReportSummary_NonCon_FY;
}> = ({ data }) => {
  return (
    <Box>
      <h1>NonConFYSummary</h1>
    </Box>
  );
};

export default NonConFYSummary;
