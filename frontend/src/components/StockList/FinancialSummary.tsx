import { DocumentListPublic } from "@/client";
import { Box, Flex, SegmentGroup, Steps, Text } from "@chakra-ui/react";
import { Suspense, useState } from "react";
import ForecastItems from "./ForecastItems";
import OperatingResultItems from "./OperatingResultItems";

interface FinancialSummaryProps {
  item: DocumentListPublic;
}

const FinancialSummary: React.FC<FinancialSummaryProps> = ({
  item,
}: FinancialSummaryProps) => {
  const [value, setValue] = useState("change");
  return (
    <>
      <Text textAlign="center" w="100%" fontSize={{ base: 16, md: 18 }}>
        {item.document_short_name}
      </Text>
      <Box>
        <Steps.Root defaultStep={item.period_index ?? 0} count={4} size="xs">
          <Steps.List>
            {Array.from({ length: 4 }).map((_, index) => (
              <Steps.Item key={index} index={index} title={index.toString()}>
                <Steps.Indicator />
                <Steps.Separator />
              </Steps.Item>
            ))}
          </Steps.List>
        </Steps.Root>
      </Box>
      <Flex
        align="flex-start"
        w={{ base: "100%", md: "70%" }}
        direction="row"
        gap={5}
      >
        <SegmentGroup.Root
          size="sm"
          value={value}
          onValueChange={(e) => setValue(e.value)}
          w={{ base: "50%", md: "30%" }}
        >
          <SegmentGroup.Indicator />
          <SegmentGroup.Item value="change" w="50%">
            <SegmentGroup.ItemText>増減率</SegmentGroup.ItemText>
            <SegmentGroup.ItemHiddenInput />
          </SegmentGroup.Item>
          <SegmentGroup.Item value="value" w="50%">
            <SegmentGroup.ItemText>金額</SegmentGroup.ItemText>
            <SegmentGroup.ItemHiddenInput />
          </SegmentGroup.Item>
        </SegmentGroup.Root>
      </Flex>
      <Suspense fallback={<Box>Loading...</Box>}>
        <OperatingResultItems
          head_item_key={item.head_item_key}
          value={value}
        />
      </Suspense>
      <Suspense fallback={<Box>Loading...</Box>}>
        <ForecastItems head_item_key={item.head_item_key} value={value} />
      </Suspense>
    </>
  );
};

export default FinancialSummary;
