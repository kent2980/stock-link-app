import { Box } from "@chakra-ui/react";
import React from "react";
import { edjp_FinancialReportSummary_Con_FY } from "../../../../client";

const ConFYSummary: React.FC<{
  data: edjp_FinancialReportSummary_Con_FY;
}> = ({ data }) => {
  return (
    <Box>
      <h1>ConFYSummary</h1>
      <Box>{data.net_sales?.cur_dur_cons_res?.display_numeric}</Box>
      <Box>{data.net_sales?.next_dur_cons_fore?.display_numeric}</Box>
    </Box>
  );
};

export default ConFYSummary;
