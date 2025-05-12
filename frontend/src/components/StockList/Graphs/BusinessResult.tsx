import { FinancialSummaryService } from "@/client";
import { Chart, useChart } from "@chakra-ui/charts";
import { BoxProps } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  LabelList,
  Legend,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

interface BusinessResultProps extends BoxProps {
  headItemKey: string;
}
const BusinessResult: React.FC<BusinessResultProps> = ({ headItemKey }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["BusinessResult", headItemKey],
    queryFn: async () => {
      return await FinancialSummaryService.getOperatingResults({
        headItemKey: headItemKey,
      });
    },
  });

  const items =
    data?.data?.map((dataItem) => ({
      type: dataItem.label,
      value: dataItem.result?.curChange?.value ?? 0,
      preValue: dataItem.result?.preChange?.value ?? 0,
    })) ?? [];

  const chart = useChart({
    data: items,
    series: [
      { name: "preValue", color: "#939393d1" },
      { name: "value", color: "ui.main" },
    ],
  });

  return (
    <>
      <Chart.Root
        chart={chart}
        h="150px"
        fontSize={"10px"}
        bg="#ffffffff"
        borderWidth="1px"
        borderStyle={"solid"}
        borderColor={chart.color("border")}
      >
        <BarChart
          barSize={100}
          data={chart.data}
          margin={{ top: 20, right: 10, left: -20, bottom: 5 }}
        >
          <CartesianGrid vertical={false} strokeDasharray="3 3" />
          <XAxis
            dataKey={chart.key("type")}
            axisLine={false}
            tickLine={false}
            tickFormatter={(value) => value.slice(0, 6)}
            stroke={chart.color("border")}
          />
          <YAxis
            axisLine={false}
            tickLine={false}
            stroke={chart.color("border")}
          />
          <Tooltip
            formatter={(value: number, name: string) => {
              const translatedName = name === "value" ? "今期" : "昨期"; // 項目名を日本語に変更
              return [`${value}%`, translatedName]; // 値に単位「%」を追加
            }}
          />
          <Legend
            verticalAlign="top"
            wrapperStyle={{ lineHeight: "40px" }}
            formatter={(name: string) => {
              const translatedName = name === "value" ? "今期" : "昨期"; // 項目名を日本語に変更
              return <span>{translatedName}</span>; // 値に単位「%」を追加
            }}
          />
          {chart.series.map((item) => (
            <Bar
              key={item.name}
              dataKey={chart.key(item.name)}
              fill={chart.color(item.color)}
              isAnimationActive={false}
            >
              {item.name === "value" && (
                <LabelList
                  dataKey={chart.key("value")}
                  position="middle"
                  style={{ fontWeight: "800", fill: chart.color("fg") }}
                />
              )}
              {item.name === "preValue" && (
                <LabelList
                  dataKey={chart.key("preValue")}
                  position="middle"
                  style={{ fontWeight: "800", fill: chart.color("fg") }}
                />
              )}
            </Bar>
          ))}
        </BarChart>
      </Chart.Root>
    </>
  );
};
export default BusinessResult;
