import {
  Box,
  Divider,
  Flex,
  Grid,
  Heading,
  keyframes,
  SimpleGrid,
  Text,
} from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import { useStore } from "@tanstack/react-store";
import React from "react";
import { AiFillCaretDown, AiFillCaretRight } from "react-icons/ai";
import {
  edjp_FinancialReportSummary_Con_Q2,
  SummaryService,
} from "../../client";
import { SummaryStore } from "../../Store/Store";

interface ContentsProps {
  head_item_key: string;
}

const Contents: React.FC<ContentsProps> = ({ head_item_key }) => {
  const { data, isPending, isError } = useQuery({
    queryKey: ["nonFraction", head_item_key],
    queryFn: () =>
      SummaryService.getSummaryNonFractionItemsHeadItemKey({
        headItemKey: head_item_key,
      }),
    staleTime: 1000 * 60 * 60 * 24,
    gcTime: 1000 * 60 * 60 * 24,
  });

  if (isError) {
    return <div>Error</div>;
  }

  function isSecondQuarter(
    data: any
  ): data is edjp_FinancialReportSummary_Con_Q2 {
    return data?.type === "edjp_FinancialReportSummary_Con_Q2";
  }

  const { year, prevYear, period } = useStore(
    SummaryStore,
    (state) => state[head_item_key] ?? { year: "", prevYear: "", period: "" }
  );
  const blink = keyframes`
  0% { opacity: 1; }
  50% { opacity: 0; }
  100% { opacity: 1; }
`;

  const blinkAnimation = `${blink} 1.2s infinite`;
  return (
    <Flex gap={4} direction="column">
      <SimpleGrid columns={2}>
        <Heading as="h2" size="lg">
          {prevYear}
          {period}
        </Heading>
        <Heading as="h2" size="lg">
          {year}
          {period}
        </Heading>
      </SimpleGrid>
      <Divider />
      {isSecondQuarter(data) && (
        <Flex gap={10} direction="column">
          <SummaryItem
            label="売上高"
            prevData={
              data.net_sales
                ?.prior_accumulated_q2_duration_consolidated_member_result_member
            }
            changePrevData={
              data.change_in_net_sales
                ?.prior_accumulated_q2_duration_consolidated_member_result_member
            }
            currentData={
              data.net_sales
                ?.current_accumulated_q2_duration_consolidated_member_result_member
            }
            changeCurrentData={
              data.change_in_net_sales
                ?.current_accumulated_q2_duration_consolidated_member_result_member
            }
          />
          <Divider />
          <SummaryItem
            label="営業利益"
            prevData={
              data.operating_income
                ?.prior_accumulated_q2_duration_consolidated_member_result_member
            }
            changePrevData={
              data.change_in_operating_income
                ?.prior_accumulated_q2_duration_consolidated_member_result_member
            }
            currentData={
              data.operating_income
                ?.current_accumulated_q2_duration_consolidated_member_result_member
            }
            changeCurrentData={
              data.change_in_operating_income
                ?.current_accumulated_q2_duration_consolidated_member_result_member
            }
          />
          <Divider />
          <SummaryItem
            label="経常利益"
            prevData={
              data.ordinary_income
                ?.prior_accumulated_q2_duration_consolidated_member_result_member
            }
            changePrevData={
              data.change_in_ordinary_income
                ?.prior_accumulated_q2_duration_consolidated_member_result_member
            }
            currentData={
              data.ordinary_income
                ?.current_accumulated_q2_duration_consolidated_member_result_member
            }
            changeCurrentData={
              data.change_in_ordinary_income
                ?.current_accumulated_q2_duration_consolidated_member_result_member
            }
          />
        </Flex>
      )}
    </Flex>
  );
};

export default Contents;

interface summaryItemProps {
  label: string;
  prevData: any;
  changePrevData: any;
  currentData: any;
  changeCurrentData: any;
}

const SummaryItem: React.FC<summaryItemProps> = ({
  label,
  prevData,
  changePrevData,
  currentData,
  changeCurrentData,
}) => {
  return (
    <Box p={2}>
      <Heading as="h3" size="md">
        {label}
      </Heading>
      <Grid gridTemplateColumns={"45% 10% 45%"}>
        <Flex direction="column" alignItems="center">
          <Flex direction="row" gap={2} fontSize="30px" fontWeight="800">
            <Text>{prevData?.display_numeric}</Text>
            <Text>{prevData?.display_scale}</Text>
          </Flex>
          <Flex direction="row" fontSize="30px">
            <Text>{changePrevData?.display_numeric}</Text>
            <Text>{changePrevData?.display_scale}</Text>
          </Flex>
        </Flex>
        <Flex direction="row" justifyContent="center">
          <AiFillCaretRight size="50px" />
        </Flex>
        <Flex direction="column" alignItems="center">
          <Flex direction="row" fontSize="30px" fontWeight="800" gap={2}>
            <Text>{currentData?.display_numeric}</Text>
            <Text>{currentData?.display_scale}</Text>
          </Flex>
          <Flex direction="row" fontSize="30px">
            <AiFillCaretDown size="40px" color="#299edd" />
            <Text>{changeCurrentData?.display_numeric}</Text>
            <Text>{changeCurrentData?.display_scale}</Text>
          </Flex>
        </Flex>
      </Grid>
    </Box>
  );
};
