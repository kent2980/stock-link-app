import { Box } from "@chakra-ui/react";
import React from "react";
import { edjp_FinancialReportSummary_Con_HY_spec } from "../../../../client";

const ConQuarterSpecSummary: React.FC<{
  data: edjp_FinancialReportSummary_Con_HY_spec;
}> = ({ data }) => {
  return (
    <Box>
      <h1>ConQuarterSpecSummary</h1>
    </Box>
  );
};

export default ConQuarterSpecSummary;
