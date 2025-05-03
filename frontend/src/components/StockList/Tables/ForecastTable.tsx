import { FinancialSummaryService, FinValueBase } from "@/client";
import {
  Badge,
  Box,
  FormatNumber,
  Stat,
  Text,
  VStack,
  Wrap,
} from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";

interface ForecastTableProps {
  HeadItemKey: string;
}

const ForecastTable: React.FC<ForecastTableProps> = ({ HeadItemKey }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["forecastData", HeadItemKey],
    queryFn: async () => {
      return await FinancialSummaryService.getForecasts({
        headItemKey: HeadItemKey,
      });
    },
  });
  return (
    <Box>
      <Wrap>
        {data?.forecast?.data?.map((item, index) => (
          <ForecastItem
            key={index}
            label={item.label}
            value={item.curValue?.value}
            valueScale={item.curValue?.display_scale}
            changeValue={item.curChange}
          />
        ))}
      </Wrap>
    </Box>
  );
};
export default ForecastTable;

interface ForecastItemProps {
  label: string;
  value?: number | null | undefined;
  valueScale?: string | null | undefined;
  changeValue?: FinValueBase | null | undefined;
}
const ForecastItem: React.FC<ForecastItemProps> = ({
  label,
  value,
  valueScale,
  changeValue,
}) => {
  return (
    <Stat.Root minW="40vw" borderWidth="1px" borderRadius="lg" p={4} bg="white">
      <Stat.Label>{label}</Stat.Label>
      <VStack>
        <Stat.ValueText>
          {value && valueScale && (
            <>
              <FormatNumber value={value} style="currency" currency="JPY" />
              <Text fontSize="12px">{valueScale}</Text>
            </>
          )}
        </Stat.ValueText>
        {changeValue !== null &&
          changeValue !== undefined &&
          (changeValue.value !== null ? (
            <>
              <Badge
                colorPalette={changeValue.value > 0 ? "green" : "red"}
                gap="0"
              >
                {changeValue.value > 0 ? (
                  <Stat.UpIndicator />
                ) : (
                  <Stat.DownIndicator />
                )}
                <FormatNumber
                  value={changeValue.value / 100}
                  style="percent"
                  maximumFractionDigits={2}
                  minimumFractionDigits={1}
                />
              </Badge>
            </>
          ) : (
            <Badge
              colorPalette="gray"
              gap="0"
              minW="50px"
              justifyContent="center"
            >
              <Text fontSize="12px">-</Text>
            </Badge>
          ))}
      </VStack>
    </Stat.Root>
  );
};
