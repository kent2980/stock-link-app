import { Box, BoxProps } from "@chakra-ui/react";
import { ResponsiveRadialBar } from "@nivo/radial-bar";
import React from "react";
import { DividendsJp, FinancialPositionsAbstractJp } from "../../../client";

interface DividendGraphAreaProps extends BoxProps {
  asset: FinancialPositionsAbstractJp | undefined | null;
  dividend: DividendsJp | undefined | null;
  stock: number;
  quarter: string;
}

const DividendGraphArea: React.FC<DividendGraphAreaProps> = ({
  asset,
  dividend,
  stock,
  quarter,
  ...props
}) => {
  const perShare = dividend?.DividendPerShare;
  const calculateGrowthRate = () => {
    let result;
    let forecast;
    switch (quarter) {
      case "":
        result = perShare?.AnnualCurrentYearResults?.numeric ?? 0;
        forecast = perShare?.AnnualNextYearForecasts?.numeric ?? 0;
        break;
      default:
        result = perShare?.AnnualPriorYearResults?.numeric ?? 0;
        forecast = perShare?.AnnualCurrentYearForecasts?.numeric ?? 0;
        break;
    }
    if (result === 0) return 0;
    else if (result === 0 || forecast === 0) return 0;
    const growth = ((forecast - result) / result) * 100;
    return parseFloat(growth.toFixed(2));
  };

  const dividendRatio = dividend?.DividendPayoutRatioCurrentYear?.numeric ?? 0;
  const data = [
    {
      id: "増配率",
      data: [{ x: "増配率", y: calculateGrowthRate() }],
    },
    {
      id: "配当性向",
      data: [{ x: "減配率", y: dividendRatio }],
    },
  ];

  return (
    <Box h="260px" bg="gray.100" p={2} id="dividend-graph" {...props}>
      <Box bg="white" h="240px" py={5}>
        <ResponsiveRadialBar
          data={data}
          innerRadius={0.5}
          padding={0.1}
          cornerRadius={5}
          startAngle={0}
          endAngle={360}
          label={(bar) => bar.id}
          animate={true}
          maxValue={100}
        />
      </Box>
    </Box>
  );
};

export default DividendGraphArea;
