import { FinValueBase } from "@/client";
import {
  Badge,
  FormatNumber,
  HStack,
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
    <Stat.Root
      borderWidth="1px"
      borderRadius="lg"
      p={2}
      bg="#b2b2b221"
      boxShadow="sm"
      {...props}
    >
      <Stat.Label fontSize={10}>{label}</Stat.Label>
      <VStack>
        <Stat.ValueText>
          {upValue && upValueScale && downValue && (
            <VStack gap={0} fontSize={18}>
              <FormatNumber value={downValue} style="currency" currency="JPY" />
              <Text>〜</Text>
              <FormatNumber value={upValue} style="currency" currency="JPY" />
              <Text fontSize={10}>{upValueScale}</Text>
            </VStack>
          )}
        </Stat.ValueText>
        <HStack>
          {downChangeValue !== null &&
            downChangeValue !== undefined &&
            (downChangeValue.value !== null ? (
              <>
                <Badge
                  colorPalette={downChangeValue.value > 0 ? "green" : "red"}
                  gap="0"
                >
                  {downChangeValue.value > 0 ? (
                    <Stat.UpIndicator />
                  ) : (
                    <Stat.DownIndicator />
                  )}
                  <FormatNumber
                    value={downChangeValue.value / 100}
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
          <Text>〜</Text>
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
        </HStack>
      </VStack>
    </Stat.Root>
  );
};

export default FinStructUpperAndLowerWrapItem;
