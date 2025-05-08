import { FinValueBase } from "@/client";
import {
  Badge,
  FormatNumber,
  Stat,
  StatRootProps,
  Text,
  VStack,
} from "@chakra-ui/react";
import React from "react";

interface FinStructUpperAndLowerWrapItemProps extends StatRootProps {
  label: string;
  downValue?: number | null | undefined;
  downValueScale?: string | null | undefined;
  downChangeValue?: FinValueBase | null | undefined;
  upValue?: number | null | undefined;
  upValueScale?: string | null | undefined;
  upChangeValue?: FinValueBase | null | undefined;
}
const FinStructUpperAndLowerWrapItem: React.FC<
  FinStructUpperAndLowerWrapItemProps
> = ({
  label,
  downValue,
  downValueScale,
  downChangeValue,
  upValue,
  upValueScale,
  upChangeValue,
  ...props
}) => {
  return (
    <Stat.Root borderWidth="1px" borderRadius="lg" p={4} bg="white" {...props}>
      <Stat.Label>{label}</Stat.Label>
      <VStack>
        <Stat.ValueText>
          {upValue && upValueScale && (
            <>
              <FormatNumber value={upValue} style="currency" currency="JPY" />
              <Text fontSize="12px">{upValueScale}</Text>
            </>
          )}
        </Stat.ValueText>
        {upChangeValue !== null &&
          upChangeValue !== undefined &&
          (upChangeValue.value !== null ? (
            <>
              <Badge
                colorPalette={upChangeValue.value > 0 ? "green" : "red"}
                gap="0"
              >
                {upChangeValue.value > 0 ? (
                  <Stat.UpIndicator />
                ) : (
                  <Stat.DownIndicator />
                )}
                <FormatNumber
                  value={upChangeValue.value / 100}
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

export default FinStructUpperAndLowerWrapItem;
