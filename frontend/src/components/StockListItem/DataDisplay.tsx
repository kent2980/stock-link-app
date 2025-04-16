import { Box, FormatNumber, Table, Text } from "@chakra-ui/react";
import React from "react";

export interface DataItem {
  name: string;
  currentValue: number;
  previousValue?: number;
  changeRate: number;
  previousChangeRate?: number;
  displayScale: string;
}

interface DataDisplayProps {
  title?: string;
  data?: DataItem[];
}

const DataDisplay: React.FC<DataDisplayProps> = ({
  title = "経営成績",
  data = [
    {
      name: "売上高",
      currentValue: 67,
      previousValue: 64,
      changeRate: 4.7,
      previousChangeRate: 3.2,
      displayScale: "億円",
    },
    {
      name: "純利益",
      currentValue: 600,
      previousValue: 360,
      changeRate: 66.7,
      previousChangeRate: 20.0,
      displayScale: "億円",
    },
    {
      name: "営業利益",
      currentValue: 30,
      previousValue: 27,
      changeRate: 11.1,
      previousChangeRate: 8.0,
      displayScale: "億円",
    },
    {
      name: "経常利益",
      currentValue: 40,
      previousValue: 35,
      changeRate: 14.3,
      previousChangeRate: 5.0,
      displayScale: "億円",
    },
  ],
}) => {
  const GetShortLabel = (label: string) => {
    switch (label) {
      case "売上高":
        return "売上";
      case "当期純利益":
        return "純利";
      case "営業収益":
        return "売上";
      case "親会社株主に帰属する当期純利益":
        return "純利";
      case "売上収益":
        return "売上";
      case "税引前利益":
        return "経利";
      case "当期利益":
        return "純利";
      case "営業利益":
        return "営利";
      case "経常利益":
        return "経利";
      case "親会社の所有者に帰属する当期利益":
        return "所純利";
      default:
        return label;
    }
  };

  return (
    <Box my={4}>
      <Text
        color="gray.600"
        fontSize="16px"
        fontWeight="semibold"
        textAlign="left"
      >
        {title}
      </Text>
      <Table.Root size="sm">
        <Table.Header>
          <Table.Row>
            <Table.ColumnHeader>項目</Table.ColumnHeader>
            {data.slice(0, 4).map((item, index) => (
              <Table.ColumnHeader key={index}>
                {GetShortLabel(item.name)}
              </Table.ColumnHeader>
            ))}
          </Table.Row>
        </Table.Header>
        <Table.Body>
          <Table.Row>
            <Table.Cell>今期実績</Table.Cell>
            {data.slice(0, 4).map((item, index) => (
              <>
                <Table.Cell key={index}>
                  <FormatNumber
                    value={item.changeRate / 100}
                    style="percent"
                    maximumFractionDigits={2}
                    minimumFractionDigits={1}
                  />
                </Table.Cell>
              </>
            ))}
          </Table.Row>
          <Table.Row>
            <Table.Cell>前期実績</Table.Cell>
            {data.slice(0, 4).map((item, index) => (
              <>
                {item.previousChangeRate && (
                  <Table.Cell key={index}>
                    <FormatNumber
                      value={item.previousChangeRate / 100}
                      style="percent"
                      maximumFractionDigits={2}
                      minimumFractionDigits={1}
                    />
                  </Table.Cell>
                )}
              </>
            ))}
          </Table.Row>
        </Table.Body>
      </Table.Root>
    </Box>
  );
};

export default DataDisplay;
