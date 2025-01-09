import React from "react";
import { edjp_FinancialReportSummary_Con_FY } from "../../../../client";
import { SummaryProps } from "../../Props/SummaryProps";
import { DividendPerShare } from "../../Table/DividendTable";
import { IssuedSharesTableProp } from "../../Table/IssuedSharesTable";
import SummaryContents from "../SummaryContents";

const ConFYSummary: React.FC<{
  data: edjp_FinancialReportSummary_Con_FY;
}> = ({ data }) => {
  const opeInfos: SummaryProps[] = [
    {
      title: "売上高",
      value: {
        cur: data.net_sales?.cur_dur_cons_res?.display_numeric ?? "",
        pri: data.net_sales?.pri_dur_cons_res?.display_numeric ?? "",
      },
      changeValue: {
        cur: data.change_in_net_sales?.cur_dur_cons_res?.numeric ?? 0,
        pri: data.change_in_net_sales?.pri_dur_cons_res?.numeric ?? 0,
      },
      valueScale: data.net_sales?.cur_dur_cons_res?.display_scale ?? "",
    },
    {
      title: "営業利益",
      value: {
        cur: data.operating_income?.cur_dur_cons_res?.display_numeric ?? "",
        pri: data.operating_income?.pri_dur_cons_res?.display_numeric ?? "",
      },
      changeValue: {
        cur: data.change_in_operating_income?.cur_dur_cons_res?.numeric ?? 0,
        pri: data.change_in_operating_income?.pri_dur_cons_res?.numeric ?? 0,
      },
      valueScale: data.operating_income?.cur_dur_cons_res?.display_scale ?? "",
    },
    {
      title: "経常利益",
      value: {
        cur: data.ordinary_income?.cur_dur_cons_res?.display_numeric ?? "",
        pri: data.ordinary_income?.pri_dur_cons_res?.display_numeric ?? "",
      },
      changeValue: {
        cur: data.change_in_ordinary_income?.cur_dur_cons_res?.numeric ?? 0,
        pri: data.change_in_ordinary_income?.pri_dur_cons_res?.numeric ?? 0,
      },
      valueScale: data.ordinary_income?.cur_dur_cons_res?.display_scale ?? "",
    },
    {
      title: "当期純利益",
      value: {
        cur: data.net_income?.cur_dur_non_cons_res?.display_numeric ?? "",
        pri: data.net_income?.pri_dur_non_cons_res?.display_numeric ?? "",
      },
      changeValue: {
        cur: data.change_in_net_income?.cur_dur_non_cons_res?.numeric ?? 0,
        pri: data.change_in_net_income?.pri_dur_non_cons_res?.numeric ?? 0,
      },
      valueScale: data.net_income?.cur_dur_non_cons_res?.display_scale ?? "",
    },
  ];

  const finInfos: SummaryProps[] = [
    {
      title: "総資産",
      value: {
        cur: data.total_assets?.cur_instant_cons_res?.display_numeric ?? "",
        pri: data.total_assets?.pri_instant_cons_res?.display_numeric ?? "",
      },
      valueScale: data.net_income?.cur_dur_non_cons_res?.display_scale ?? "",
    },
    {
      title: "自己資本",
      value: {
        cur: data.owners_equity?.cur_instant_cons_res?.display_numeric ?? "",
        pri: data.owners_equity?.pri_instant_cons_res?.display_numeric ?? "",
      },
      valueScale: data.owners_equity?.cur_instant_cons_res?.display_scale ?? "",
    },
    {
      title: "自己資本比率",
      value: {
        cur:
          data.net_income_to_shareholders_equity_ratio?.cur_dur_cons_res
            ?.display_numeric ?? "",
        pri:
          data.net_income_to_shareholders_equity_ratio?.pri_dur_cons_res
            ?.display_numeric ?? "",
      },
      valueScale:
        data.net_income_to_shareholders_equity_ratio?.cur_dur_cons_res
          ?.display_scale ?? "",
    },
  ];

  let dividends: DividendPerShare[] = [
    {
      label: "第1四半期末",
      resultValue:
        data.dividend_per_share?.cur_dur_first_quarter_non_cons_res
          ?.display_numeric ?? "",
      priResultValue:
        data.dividend_per_share?.pri_dur_first_quarter_non_cons_res
          ?.display_numeric ?? "",
      forValue:
        data.dividend_per_share?.next_dur_first_quarter_non_cons_fore
          ?.display_numeric ?? "",
    },
    {
      label: "第2四半期末",
      resultValue:
        data.dividend_per_share?.cur_dur_second_quarter_non_cons_res
          ?.display_numeric ?? "",
      priResultValue:
        data.dividend_per_share?.pri_dur_second_quarter_non_cons_res
          ?.display_numeric ?? "",
      forValue: "",
    },
    {
      label: "第3四半期末",
      resultValue:
        data.dividend_per_share?.cur_dur_third_quarter_non_cons_res
          ?.display_numeric ?? "",
      priResultValue:
        data.dividend_per_share?.pri_dur_third_quarter_non_cons_res
          ?.display_numeric ?? "",
      forValue:
        data.dividend_per_share?.next_dur_third_quarter_non_cons_fore
          ?.display_numeric ?? "",
    },
    {
      label: "第4四半期末",
      resultValue: "",
      priResultValue:
        data.dividend_per_share?.pri_dur_annual_non_cons_res?.display_numeric ??
        "",
      forValue:
        data.dividend_per_share?.next_dur_end_non_cons_fore?.display_numeric ??
        "",
    },
    {
      label: "通期",
      resultValue: "",
      priResultValue:
        data.dividend_per_share?.pri_dur_annual_non_cons_res?.display_numeric ??
        "",
      forValue:
        data.dividend_per_share?.next_dur_annual_non_cons_fore
          ?.display_numeric ?? "",
    },
  ];

  const forecasts: SummaryProps[] = [
    {
      title: "売上高",
      value: {
        cur: data.net_sales?.next_dur_cons_fore?.display_numeric ?? "",
      },
      changeValue: {
        cur: data.change_in_net_sales?.next_dur_cons_fore?.numeric ?? 0,
      },
      valueScale: data.net_sales?.next_dur_cons_fore?.display_scale ?? "",
    },
    {
      title: "営業利益",
      value: {
        cur: data.operating_income?.next_dur_cons_fore?.display_numeric ?? "",
      },
      changeValue: {
        cur: data.change_in_operating_income?.next_dur_cons_fore?.numeric ?? 0,
      },
      valueScale:
        data.operating_income?.next_dur_cons_fore?.display_scale ?? "",
    },
    {
      title: "経常利益",
      value: {
        cur: data.ordinary_income?.next_dur_cons_fore?.display_numeric ?? "",
      },
      changeValue: {
        cur: data.change_in_ordinary_income?.next_dur_cons_fore?.numeric ?? 0,
      },
      valueScale: data.ordinary_income?.next_dur_cons_fore?.display_scale ?? "",
    },
    {
      title: "当期純利益",
      value: {
        cur:
          data.profit_attributable_to_owners_of_parent?.next_dur_cons_fore
            ?.display_numeric ?? "",
      },
      changeValue: {
        cur:
          data.change_in_profit_attributable_to_owners_of_parent
            ?.next_dur_cons_fore?.numeric ?? 0,
      },
      valueScale:
        data.profit_attributable_to_owners_of_parent?.cur_dur_cons_res
          ?.display_scale ?? "",
    },
  ];

  const issuedShares: IssuedSharesTableProp = {
    issuedSharesEnd: {
      cur:
        data
          .number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock
          ?.cur_instant_non_cons_res?.display_numeric ?? "",
      pri:
        data
          .number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock
          ?.pri_instant_non_cons_res?.display_numeric ?? "",
      scale:
        data
          .number_of_issued_and_outstanding_shares_at_the_end_of_fiscal_year_including_treasury_stock
          ?.cur_instant_non_cons_res?.display_scale ?? "",
    },
    treasurySharesEnd: {
      cur:
        data.number_of_treasury_stock_at_the_end_of_fiscal_year
          ?.cur_instant_non_cons_res?.display_numeric ?? "",
      pri:
        data.number_of_treasury_stock_at_the_end_of_fiscal_year
          ?.pri_instant_non_cons_res?.display_numeric ?? "",
      scale:
        data.number_of_treasury_stock_at_the_end_of_fiscal_year
          ?.cur_instant_non_cons_res?.display_scale ?? "",
    },
    avgSharesEnd: {
      cur:
        data.average_number_of_shares?.cur_dur_non_cons_res?.display_numeric ??
        "",
      pri:
        data.average_number_of_shares?.pri_dur_non_cons_res?.display_numeric ??
        "",
      scale:
        data.average_number_of_shares?.cur_dur_non_cons_res?.display_scale ??
        "",
    },
  };

  const items = {
    opeInfos: opeInfos,
    finInfos: finInfos,
    dividends: dividends,
    forecasts: forecasts,
    issuedShares: issuedShares,
  };

  return <SummaryContents items={items} />;
};

export default ConFYSummary;
