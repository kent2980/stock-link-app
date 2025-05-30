import { FinancialSummaryService } from "@/client";
import { Box, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import {
  BarElement,
  CategoryScale,
  Chart as ChartJS,
  Legend,
  LinearScale,
  Tooltip,
} from "chart.js";
import React from "react";
import { Bar } from "react-chartjs-2";

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

interface CashFlowProps {
  code: string;
}

const CashFlow: React.FC<CashFlowProps> = ({ code }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["CashFlow", code],
    queryFn: async () => {
      return await FinancialSummaryService.getCashFlows({
        code: code,
      });
    },
    gcTime: 30 * 24 * 60 * 60 * 1000, // 30 days
    staleTime: 30 * 24 * 60 * 60 * 1000, // 30 days
  });

  const chartData = {
    labels: data?.data?.map(
      (dataItem) =>
        dataItem.label ??
        ""
          .replace("によるキャッシュ・フロー", "CS")
          .replace("現金及び現金同等物期末残高", "現金")
    ),
    datasets: [
      {
        label: "金額",
        data: data?.data?.map(
          (dataItem) => dataItem.result?.curValue?.value ?? 0
        ),
        backgroundColor: (context: any) =>
          context.raw >= 0 ? "rgba(54, 162, 235, 1)" : "rgba(255, 99, 132, 1)", // プラスは青、マイナスは赤
        borderColor: (context: any) =>
          context.raw >= 0 ? "rgba(54, 162, 235, 1)" : "rgba(255, 99, 132, 1)", // プラスは青、マイナスは赤
        borderWidth: 1,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        callbacks: {
          label: (context: any) =>
            `${context.raw.toLocaleString()} ${data?.data?.[context.dataIndex]?.result?.curValue?.display_scale ?? ""}`,
        },
      },
    },
    scales: {
      x: {
        ticks: {
          maxRotation: 90,
          minRotation: 45,
        },
      },
      y: {
        beginAtZero: true,
      },
    },
  };

  return (
    <Box>
      <Text fontWeight="bold" mb={4}>
        キャッシュフロー
      </Text>
      <Bar data={chartData} options={options} />
    </Box>
  );
};

export default CashFlow;
