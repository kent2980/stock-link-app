import { FinValueAbstractBase } from "@/client";
import { Stat, Text } from "@chakra-ui/react";

const shortBusinessChange = (value: number | null | undefined) => {
  if (value == null) {
    return <Text>-</Text>;
  }

  const item = (
    <Stat.Root size="sm">
      <Stat.ValueText alignItems="baseline" fontSize={{ base: 14, md: "md" }}>
        {value.toFixed(1).replace("-", "▲")}
        <Stat.ValueUnit fontSize={{ base: 10, md: 12 }}>%</Stat.ValueUnit>
      </Stat.ValueText>
    </Stat.Root>
  );

  return item;
};

const shortBusinessValue = (
  value: number | null | undefined,
  scale: string | null | undefined
) => {
  if (value == null) {
    return <Text>-</Text>;
  }

  // valueを桁区切り
  const formatValue = value.toLocaleString("ja-JP", {
    maximumFractionDigits: 0,
  });

  return (
    <Stat.Root size="sm">
      <Stat.ValueText alignItems="baseline" fontSize={{ base: 14, md: "md" }}>
        {formatValue}
        <Stat.ValueUnit fontSize={{ base: 10, md: 12 }}>{scale}</Stat.ValueUnit>
      </Stat.ValueText>
    </Stat.Root>
  );
};

export const curValue = (item: FinValueAbstractBase, value: string) => {
  if (value === "change") {
    return shortBusinessChange(item.curChange?.value);
  } else {
    return shortBusinessValue(
      item.curValue?.value,
      item.curValue?.display_scale
    );
  }
};

export const preValue = (item: FinValueAbstractBase, value: string) => {
  if (value === "change") {
    return shortBusinessChange(item.preChange?.value);
  } else {
    return shortBusinessValue(
      item.preValue?.value,
      item.preValue?.display_scale
    );
  }
};
