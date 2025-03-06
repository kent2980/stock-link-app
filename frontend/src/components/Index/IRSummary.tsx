import { Box } from "@chakra-ui/react";
import { Suspense } from "react";
import OperatingResult from "./IRSummary/OperatingResult";

interface IXSummaryProps {
  head_item_key: string;
}

function IRSummary({ head_item_key }: IXSummaryProps) {
  return (
    <Box>
      <Suspense fallback={<div>Loading...</div>}>
        <OperatingResult head_item_key={head_item_key} />
      </Suspense>
    </Box>
  );
}

export default IRSummary;
