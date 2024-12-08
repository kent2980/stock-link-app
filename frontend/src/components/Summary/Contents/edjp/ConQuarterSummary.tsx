import { Heading, SimpleGrid } from "@chakra-ui/react";
import dayjs from "dayjs";
import React from "react";
import {
  edjp,
  edjp_FinancialReportSummary_Con_Q1,
  edjp_FinancialReportSummary_Con_Q2,
  edjp_FinancialReportSummary_Con_Q3,
} from "../../../../client";
import DividendTable, { DividendPerShare } from "../../Table/DividendTable";
import SummaryGrid, { SummaryGridItemProps } from "../../Table/SummaryGrid";

const ConQuarterSummary: React.FC<{
  data:
    | edjp_FinancialReportSummary_Con_Q1
    | edjp_FinancialReportSummary_Con_Q2
    | edjp_FinancialReportSummary_Con_Q3;
  fracData: edjp;
}> = ({ data, fracData }) => {
  function isFirstQuarter(
    data:
      | edjp_FinancialReportSummary_Con_Q1
      | edjp_FinancialReportSummary_Con_Q2
      | edjp_FinancialReportSummary_Con_Q3
  ): data is edjp_FinancialReportSummary_Con_Q1 {
    return data.type === "edjp_FinancialReportSummary_Con_Q1";
  }

  function isSecondQuarter(
    data:
      | edjp_FinancialReportSummary_Con_Q1
      | edjp_FinancialReportSummary_Con_Q2
      | edjp_FinancialReportSummary_Con_Q3
  ): data is edjp_FinancialReportSummary_Con_Q2 {
    return data.type === "edjp_FinancialReportSummary_Con_Q2";
  }

  function isThirdQuarter(
    data:
      | edjp_FinancialReportSummary_Con_Q1
      | edjp_FinancialReportSummary_Con_Q2
      | edjp_FinancialReportSummary_Con_Q3
  ): data is edjp_FinancialReportSummary_Con_Q3 {
    return data.type === "edjp_FinancialReportSummary_Con_Q3";
  }

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

  const OpeSummaries: SummaryGridItemProps[] = [
    {
      title: "売上高",
      itemTitle: getQuarterTitle(fracData),
      value: data.net_sales?.cur_dur_cons_res?.display_numeric ?? "",
      changeValue:
        data.change_in_net_sales?.cur_dur_cons_res?.display_numeric ?? "",
      priValue: data.net_sales?.pri_dur_cons_res?.display_numeric ?? "",
      priChangeValue:
        data.change_in_net_sales?.pri_dur_cons_res?.display_numeric ?? "",
      isChange: true,
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
      isChange: true,
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
      isChange: true,
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
      isChange: true,
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
      isChange: true,
    },
    {
      title: "１株当たり純利益",
      itemTitle: getQuarterTitle(fracData),
      value: data.net_income_per_share?.cur_dur_cons_res?.display_numeric ?? "",
      changeValue: "",
      priValue:
        data.net_income_per_share?.pri_dur_cons_res?.display_numeric ?? "",
      priChangeValue: "",
      isChange: false,
    },
    {
      title: "潜在株式調整後１株当たり純利益",
      itemTitle: getQuarterTitle(fracData),
      value:
        data.diluted_net_income_per_share?.cur_dur_cons_res?.display_numeric ??
        "",
      changeValue: "",
      priValue:
        data.diluted_net_income_per_share?.pri_dur_cons_res?.display_numeric ??
        "",
      priChangeValue: "",
      isChange: false,
    },
  ];

  const finStatus: SummaryGridItemProps[] = [
    {
      title: "総資産",
      itemTitle: getQuarterTitle(fracData),
      value: data.total_assets?.cur_instant_cons_res?.display_numeric ?? "",
      changeValue: "",
      priValue: data.total_assets?.pri_instant_cons_res?.display_numeric ?? "",
      priChangeValue: "",
      isChange: false,
    },
    {
      title: "純資産",
      itemTitle: getQuarterTitle(fracData),
      value: data.net_assets?.cur_instant_cons_res?.display_numeric ?? "",
      changeValue: "",
      priValue: data.net_assets?.pri_instant_cons_res?.display_numeric ?? "",
      priChangeValue: "",
      isChange: false,
    },
    {
      title: "自己資本比率",
      itemTitle: getQuarterTitle(fracData),
      value: "",
      changeValue:
        data.capital_adequacy_ratio?.cur_instant_cons_res?.display_numeric ??
        "",
      priValue: "",
      priChangeValue:
        data.capital_adequacy_ratio?.pri_instant_cons_res?.display_numeric ??
        "",
      isChange: true,
    },
  ];

  let dividends: DividendPerShare[] = [];
  if (isFirstQuarter(data)) {
    dividends = [
      {
        label: "第一四半期末",
        resultValue:
          data.dividend_per_share?.cur_dur_first_quarter_non_cons_res
            ?.display_numeric ?? "",
        priResultValue:
          data.dividend_per_share?.pri_dur_first_quarter_non_cons_res
            ?.display_numeric ?? "",
        forValue: "",
      },
    ];
  } else if (isSecondQuarter(data)) {
    dividends = [
      {
        label: "1Q期末",
        resultValue:
          data.dividend_per_share?.cur_dur_first_quarter_non_cons_res
            ?.display_numeric ?? "",
        priResultValue:
          data.dividend_per_share?.pri_dur_first_quarter_non_cons_res
            ?.display_numeric ?? "",
        forValue: "",
      },
      {
        label: "2Q期末",
        resultValue:
          data.dividend_per_share?.cur_dur_second_quarter_non_cons_res
            ?.display_numeric ?? "",
        priResultValue:
          data.dividend_per_share?.pri_dur_second_quarter_non_cons_res
            ?.display_numeric ?? "",
        forValue: "",
      },
      {
        label: "3Q期末",
        resultValue: "",
        priResultValue:
          data.dividend_per_share?.pri_dur_third_quarter_non_cons_res
            ?.display_numeric ?? "",
        forValue:
          data.dividend_per_share?.cur_dur_third_quarter_non_cons_fore
            ?.display_numeric ?? "",
      },
      {
        label: "4Q期末",
        resultValue: "",
        priResultValue:
          data.dividend_per_share?.pri_dur_end_non_cons_res?.display_numeric ??
          "",
        forValue:
          data.dividend_per_share?.cur_dur_end_non_cons_fore?.display_numeric ??
          "",
      },
      {
        label: "通期",
        resultValue: "",
        priResultValue:
          data.dividend_per_share?.pri_dur_annual_non_cons_res
            ?.display_numeric ?? "",
        forValue:
          data.dividend_per_share?.cur_dur_annual_non_cons_fore
            ?.display_numeric ?? "",
      },
    ];
  }

  return (
    <SimpleGrid gap={3} px={2} py={4}>
      <Heading as="h2" size="sm" alignSelf="flex-start" p={2}>
        1. 経営成績
      </Heading>
      <SummaryGrid summaries={OpeSummaries} />
      <Heading as="h2" size="sm" alignSelf="flex-start" p={2}>
        2. 財政状態
      </Heading>
      <SummaryGrid summaries={finStatus} />
      {dividends.length > 0 && (
        <>
          <Heading as="h2" size="sm" alignSelf="flex-start" p={2}>
            3. 配当の状況
          </Heading>
          <DividendTable dividends={dividends} />
        </>
      )}
    </SimpleGrid>
  );
};

export default ConQuarterSummary;
