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

interface FinStructWrapItemProps extends StatRootProps {
  label: string;
  value?: number | null | undefined;
  valueScale?: string | null | undefined;
  changeValue?: FinValueBase | null | undefined;
}
const FinStructWrapItem: React.FC<FinStructWrapItemProps> = ({
  label,
  value,
  valueScale,
  changeValue,
  ...props
}) => {
  return (
    <Stat.Root borderWidth="1px" borderRadius="lg" p={4} bg="white" {...props}>
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

export default FinStructWrapItem;
