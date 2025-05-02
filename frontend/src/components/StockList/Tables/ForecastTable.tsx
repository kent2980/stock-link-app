import { FinancialSummaryService } from "@/client";
import {
  Badge,
  Box,
  FormatNumber,
  Heading,
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
      <Heading as="h3" fontSize="md" fontWeight="bold" mb={4}>
        業績予想
      </Heading>
      <Wrap>
        {data?.forecast?.data?.map((item, index) => (
          <ForecastItem
            key={index}
            label={item.label}
            value={item.curValue?.value}
            valueScale={item.curValue?.display_scale}
            changeValue={item.curChange?.value}
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
  changeValue?: number | null | undefined;
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
        {changeValue ? (
          <>
            <Badge colorPalette={changeValue > 0 ? "green" : "red"} gap="0">
              {changeValue > 0 ? <Stat.UpIndicator /> : <Stat.DownIndicator />}
              <FormatNumber
                value={changeValue / 100}
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
        )}
      </VStack>
    </Stat.Root>
  );
};
