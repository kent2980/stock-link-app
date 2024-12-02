import { Box, Table, Td, Th, Thead, Tr } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import React from "react";
import { edif, edjp, SummaryService } from "../../client";
import { SummaryStore } from "../../Store/Store";

interface HeaderProps {
  head_item_key: string;
}

const Header: React.FC<HeaderProps> = ({ head_item_key }) => {
  const { data, isPending, isError } = useQuery({
    queryKey: ["NonNumericItem", head_item_key],
    queryFn: () =>
      SummaryService.getSummaryNonNumericItemsHeadItemKey({
        headItemKey: head_item_key,
      }),
    staleTime: 1000 * 60 * 60 * 24,
    gcTime: 1000 * 60 * 60 * 24,
  });

  if (isError) {
    return <div>Error</div>;
  }

  function isEd(data: any): data is edjp | edif {
    return data?.type === "edjp" || data?.type === "edif";
  }

  const summaryData = isEd(data) ? data : null;

  SummaryStore.setState((state) => {
    return {
      ...state,
      [head_item_key]: {
        year: summaryData?.fiscal_year_end?.value ?? "",
        prevYear: summaryData?.previous_fiscal_year_end_date_dei?.value ?? "",
        period: summaryData?.type_of_current_period_dei?.value ?? "",
      },
    };
  });

  return (
    <Box fontSize="14px">
      <Table size="xs" variant="unstyled">
        <Thead>
          <Tr fontSize="10px">
            <Th>証券コード</Th>
            <Th>企業名</Th>
            <Th>提出書類名</Th>
            <Th>決算期</Th>
            <Th>電話番号</Th>
            <Th>URL</Th>
          </Tr>
        </Thead>
        <Tr fontSize="14px">
          <Td>{summaryData?.securities_code?.value}</Td>
          <Td>{summaryData?.company_name?.value}</Td>
          <Td>{summaryData?.document_name?.value}</Td>
          <Td>{summaryData?.fiscal_year_end?.value}</Td>
          <Td>{summaryData?.tel?.value}</Td>
          <Td>{summaryData?.URL?.value}</Td>
        </Tr>
      </Table>
    </Box>
  );
};

export default Header;
