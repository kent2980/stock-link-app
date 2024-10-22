import { Box, BoxProps, Heading } from "@chakra-ui/react";
import { ResponsiveBar } from "@nivo/bar";
import React from "react";

interface OperatingGraphAreaProps extends BoxProps {
  netSales: number;
  operatingIncome: number;
  ordinaryIncome: number;
  profit: number;
}

const OperatingGraphArea: React.FC<OperatingGraphAreaProps> = ({
  netSales,
  operatingIncome,
  ordinaryIncome,
  profit,
  ...props
}) => {
  const data = [
    {
      label: "売上高",
      value: netSales,
    },
    {
      label: "営業利益",
      value: operatingIncome,
    },
    {
      label: "経常利益",
      value: ordinaryIncome,
    },
    {
      label: "純利益",
      value: profit,
    },
  ];

  const getColor = (bar: any) => {
    switch (bar.data.label) {
      case "売上高":
        return "#4caf4fb8";
      case "営業利益":
        return "#2195f3b4";
      case "経常利益":
        return "#ff9900b8";
      case "純利益":
        return "#e91e62b0";
      default:
        return "#9E9E9E";
    }
  };

  return (
    <Box h="200px" bg="gray.100" p={2} id="operating-result-graph" {...props}>
      <Box bg="white" h="180px" m={0}>
        <Heading as="h2" fontSize="10px" mx={8} mb={1} p={2}>
          経営成績(前年比増益率)
        </Heading>
        <ResponsiveBar
          data={data}
          keys={["value"]}
          indexBy="label"
          margin={{ top: 0, right: 0, bottom: 60, left: 60 }}
          padding={0.4}
          valueScale={{ type: "linear" }}
          indexScale={{ type: "band", round: true }}
          colors={getColor}
          borderColor={{
            from: "color",
            modifiers: [["darker", 1.6]],
          }}
          axisTop={null}
          axisRight={null}
          axisBottom={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legendPosition: "middle",
            legendOffset: 32,
          }}
          axisLeft={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "増益率(%)",
            legendPosition: "middle",
            legendOffset: -40,
            tickValues: 2,
          }}
          gridYValues={2}
          labelSkipWidth={12}
          labelSkipHeight={12}
          labelTextColor="#ffffff"
          role="application"
          ariaLabel="Nivo bar chart demo"
          layout="vertical"
          enableGridY={false}
        />
      </Box>
    </Box>
  );
};

export default OperatingGraphArea;
