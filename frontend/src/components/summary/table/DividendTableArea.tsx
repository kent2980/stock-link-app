import {
  Box,
  BoxProps,
  Heading,
  Table,
  Tbody,
  Td,
  Text,
  Th,
  Thead,
  Tr,
} from "@chakra-ui/react";
import React from "react";
import { DividendsJp } from "../../../client";

interface DividendTableAreaProps extends BoxProps {
  label: string;
  quarter: string;
  dividend: DividendsJp | null | undefined;
}

const DividendTableArea: React.FC<DividendTableAreaProps> = ({
  label,
  quarter,
  dividend,
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
    if (result === 0) return "-";
    else if (result === 0 || forecast === 0) return "-";
    const growth = ((forecast - result) / result) * 100;
    return growth.toFixed(2) + "%";
  };

  return (
    <Box borderWidth="1px" {...props}>
      <Heading as="h2" size="xs" p={2} bg="gray.100">
        {label}
      </Heading>
      <Table variant="dividend" size="sm">
        <Thead>
          <Tr>
            <Th>{quarter}</Th>
            <Th>1Q末</Th>
            <Th>
              <Text>中間</Text>
              <Text>期末</Text>
            </Th>
            <Th>3Q末</Th>
            <Th>期末</Th>
            <Th>合計</Th>
          </Tr>
        </Thead>
        <Tbody>
          <Tr>
            <Td>
              <Text>昨年</Text>
              <Text>実績</Text>
            </Td>
            <Td>{perShare?.FirstQuarterPriorYearResults?.value ?? "-"} </Td>
            <Td>{perShare?.SecondQuarterPriorYearResults?.value ?? "-"} </Td>
            <Td>{perShare?.ThirdQuarterPriorYearResults?.value ?? "-"} </Td>
            <Td>{perShare?.YearEndPriorYearResults?.value ?? "-"} </Td>
            <Td>{perShare?.AnnualPriorYearResults?.value ?? "-"} </Td>
          </Tr>
          <Tr>
            <Td>
              <Text>今期</Text>
              <Text>実績</Text>
            </Td>
            <Td>{perShare?.FirstQuarterCurrentYearResults?.value ?? "-"} </Td>
            <Td>{perShare?.SecondQuarterCurrentYearResults?.value ?? "-"} </Td>
            <Td>{perShare?.ThirdQuarterCurrentYearResults?.value ?? "-"} </Td>
            <Td>{perShare?.YearEndCurrentYearResults?.value ?? "-"} </Td>
            <Td>{perShare?.AnnualCurrentYearResults?.value ?? "-"} </Td>
          </Tr>
          <Tr display={quarter != "" ? "none" : ""}>
            <Td>
              <Text>来期</Text>
              <Text>予想</Text>
            </Td>
            <Td>{perShare?.FirstQuarterNextYearForecasts?.value ?? "-"} </Td>
            <Td>{perShare?.SecondQuarterNextYearForecasts?.value ?? "-"} </Td>
            <Td>{perShare?.ThirdQuarterNextYearForecasts?.value ?? "-"} </Td>
            <Td>{perShare?.YearEndNextYearForecasts?.value ?? "-"} </Td>
            <Td>{perShare?.AnnualNextYearForecasts?.value ?? "-"} </Td>
          </Tr>
          <Tr display={quarter === "" ? "none" : ""}>
            <Td>
              <Text>今期</Text>
              <Text>予想</Text>
            </Td>
            <Td>{perShare?.FirstQuarterCurrentYearForecasts?.value ?? "-"} </Td>
            <Td>
              {perShare?.SecondQuarterCurrentYearForecasts?.value ?? "-"}{" "}
            </Td>
            <Td>{perShare?.ThirdQuarterCurrentYearForecasts?.value ?? "-"} </Td>
            <Td>{perShare?.YearEndCurrentYearForecasts?.value ?? "-"} </Td>
            <Td>{perShare?.AnnualCurrentYearForecasts?.value ?? "-"} </Td>
          </Tr>
        </Tbody>
      </Table>
      <Table variant="dividend" size="sm">
        <Thead>
          <Tr>
            <Th>修正</Th>
            <Th>増配率</Th>
            <Th>配当性向</Th>
          </Tr>
        </Thead>
        <Tbody>
          <Tr>
            <Td>
              {(() => {
                if (dividend?.CorrectionOfDividendForecast?.value === "false")
                  return "無";
                else return "有";
              })()}
            </Td>
            <Td>{calculateGrowthRate()}</Td>
            <Td>{dividend?.DividendPayoutRatioCurrentYear?.value ?? "-"} </Td>
          </Tr>
        </Tbody>
      </Table>
    </Box>
  );
};

export default DividendTableArea;
