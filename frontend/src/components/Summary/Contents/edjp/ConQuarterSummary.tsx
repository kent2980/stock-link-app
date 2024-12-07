import { Grid, Heading, SimpleGrid } from "@chakra-ui/react";
import dayjs from "dayjs";
import React from "react";
import {
  edjp,
  edjp_FinancialReportSummary_Con_Q1,
  edjp_FinancialReportSummary_Con_Q2,
  edjp_FinancialReportSummary_Con_Q3,
} from "../../../../client";
import SummaryGridItem from "../../Table/SummaryGridItem";

const ConQuarterSummary: React.FC<{
  data:
    | edjp_FinancialReportSummary_Con_Q1
    | edjp_FinancialReportSummary_Con_Q2
    | edjp_FinancialReportSummary_Con_Q3;
  fracData: edjp;
}> = ({ data, fracData }) => {
  function getQuarterTitle(data: edjp) {
    const fiscal = data.fiscal_year_end?.value;
    const fiscal_jp_str = dayjs(fiscal).format("YYYY年M月期");
    const period = data.type_of_current_period_dei?.value;
    if (period === "Q1") {
      return `${fiscal_jp_str}第1四半期`;
    } else if (period === "Q2") {
      return `${fiscal_jp_str}第2四半期`;
    } else if (period === "Q3") {
      return `${fiscal_jp_str}第3四半期`;
    } else if (period === "HY") {
      return `${fiscal_jp_str}中間期`;
    } else {
      return `${fiscal_jp_str}通期`;
    }
  }

  const summaries = [
    {
      title: "売上高",
      itemTitle: getQuarterTitle(fracData),
      value: data.net_sales?.cur_dur_cons_res?.display_numeric ?? "",
      changeValue:
        data.change_in_net_sales?.cur_dur_cons_res?.display_numeric ?? "",
      priValue: data.net_sales?.pri_dur_cons_res?.display_numeric ?? "",
      priChangeValue:
        data.change_in_net_sales?.pri_dur_cons_res?.display_numeric ?? "",
    },
    {
      title: "営業利益",
      itemTitle: getQuarterTitle(fracData),
      value: data.operating_income?.cur_dur_cons_res?.display_numeric ?? "",
      changeValue:
        data.change_in_operating_income?.cur_dur_cons_res?.display_numeric ??
        "",
      priValue: data.operating_income?.pri_dur_cons_res?.display_numeric ?? "",
      priChangeValue:
        data.change_in_operating_income?.pri_dur_cons_res?.display_numeric ??
        "",
    },
    {
      title: "経常利益",
      itemTitle: getQuarterTitle(fracData),
      value: data.ordinary_income?.cur_dur_cons_res?.display_numeric ?? "",
      changeValue:
        data.change_in_ordinary_income?.cur_dur_cons_res?.display_numeric ?? "",
      priValue: data.ordinary_income?.pri_dur_cons_res?.display_numeric ?? "",
      priChangeValue:
        data.change_in_ordinary_income?.pri_dur_cons_res?.display_numeric ?? "",
    },
    {
      title: "当期純利益",
      itemTitle: getQuarterTitle(fracData),
      value:
        data.profit_attributable_to_owners_of_parent?.cur_dur_cons_res
          ?.display_numeric ?? "",
      changeValue:
        data.change_in_profit_attributable_to_owners_of_parent?.cur_dur_cons_res
          ?.display_numeric ?? "",
      priValue:
        data.profit_attributable_to_owners_of_parent?.pri_dur_cons_res
          ?.display_numeric ?? "",
      priChangeValue:
        data.change_in_profit_attributable_to_owners_of_parent?.pri_dur_cons_res
          ?.display_numeric ?? "",
    },
    {
      title: "包括利益",
      itemTitle: getQuarterTitle(fracData),
      value: data.comprehensive_income?.cur_dur_cons_res?.display_numeric ?? "",
      changeValue:
        data.change_in_comprehensive_income?.cur_dur_cons_res
          ?.display_numeric ?? "",
      priValue:
        data.comprehensive_income?.pri_dur_cons_res?.display_numeric ?? "",
      priChangeValue:
        data.change_in_comprehensive_income?.pri_dur_cons_res
          ?.display_numeric ?? "",
    },
  ];
  return (
    <SimpleGrid gap={3} px={2} py={4}>
      <Heading as="h2" size="sm" alignSelf="flex-start">
        1. 経営成績
      </Heading>
      <Grid
        templateColumns="repeat(2,1fr)"
        templateRows="auto"
        fontWeight={1000}
        bg="ui.dim"
        gap={4}
      >
        {summaries.map((summary, index) => (
          <SummaryGridItem
            key={index}
            title={summary.title}
            itemTitle={summary.itemTitle}
            value={summary.value}
            changeValue={summary.changeValue}
            priValue={summary.priValue}
            priChangeValue={summary.priChangeValue}
          />
        ))}
      </Grid>
    </SimpleGrid>
  );
};

export default ConQuarterSummary;
