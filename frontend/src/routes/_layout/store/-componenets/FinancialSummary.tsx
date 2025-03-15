import { DocumentListPublic } from "@/client";
import { Box, Flex, SegmentGroup, Text } from "@chakra-ui/react";
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
      <Text textAlign="center" w="100%">
        {item.document_short_name}
      </Text>
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
            <SegmentGroup.ItemText>増減</SegmentGroup.ItemText>
            <SegmentGroup.ItemHiddenInput />
          </SegmentGroup.Item>
          <SegmentGroup.Item value="value" w="50%">
            <SegmentGroup.ItemText>金額</SegmentGroup.ItemText>
            <SegmentGroup.ItemHiddenInput />
          </SegmentGroup.Item>
        </SegmentGroup.Root>
        <Flex alignItems="center" justifyContent="center">
          <Text color="gray.700" fontSize={{ base: 12, md: 14 }}>
            ※()内は昨年度の数値です。
          </Text>
        </Flex>
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
