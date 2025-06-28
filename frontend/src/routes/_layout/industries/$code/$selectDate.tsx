import Disclosure33 from "@/Pages/disclosure/Disclosure33";
import { Box } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/industries/$code/$selectDate")({
  component: IndustriesCode,
});

function IndustriesCode() {
  const { code, selectDate } = Route.useParams();

  const IntCode = parseInt(code, 10);
  return (
    <Box>
      <Disclosure33 code_33={IntCode} select_date={selectDate} />
    </Box>
  );
}
