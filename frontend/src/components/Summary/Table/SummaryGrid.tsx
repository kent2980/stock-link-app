import { Center, Grid, GridItem, Heading, Text } from "@chakra-ui/react";
import React from "react";

export interface SummaryGridItemProps {
  title: string | null | undefined;
  itemTitle: string | null | undefined;
  value: string | null | undefined;
  changeValue: string | null | undefined;
  priValue: string | null | undefined;
  priChangeValue: string | null | undefined;
  isChange: boolean;
}

interface SummaryGridProps {
  summaries: SummaryGridItemProps[];
}

const SummaryGrid: React.FC<SummaryGridProps> = ({ summaries }) => {
  return (
    <Grid
      templateColumns="repeat(2,1fr)"
      templateRows="auto"
      fontWeight={1000}
      bg="ui.dim"
      gap={4}
      borderColor={"ui.secondary"}
    >
      {summaries.map((summary, index) => (
        <SummaryGridItem
          key={index}
          title={summary.title}
          itemTitle={summary.itemTitle}
          value={summary.value}
          changeValue={summary.changeValue}
          priValue={summary.priValue}
          priChangeValue={summary.priChangeValue}
          isChange={summary.isChange}
        />
      ))}
    </Grid>
  );
};

export default SummaryGrid;

const SummaryGridItem: React.FC<SummaryGridItemProps> = ({
  title,
  itemTitle,
  value,
  changeValue,
  priValue,
  priChangeValue,
  isChange,
}) => {
  const isValue = () => {
    if (value === "" && isChange === true) {
      return false;
    }
    return true;
  };

  const isChangeUp = () => {
    if (changeValue && changeValue.includes("△")) {
      return false;
    }
    return true;
  };

  const isGridItemView = () => {
    if (value === "") {
      if (isChange === false) {
        return false;
      }
    }
    return true;
  };

  return (
    <GridItem
      borderColor={
        isValue()
          ? isChange
            ? isChangeUp()
              ? "#f2b5b5"
              : "#a4b4e9"
            : "ui.main"
          : "ui.main"
      }
      bg="ui.light"
      color="ui.main"
      borderStyle="solid"
      borderWidth="0.5px"
      w="45vw"
      p={1}
      mx="auto"
      display={isGridItemView() ? "block" : "none"}
    >
      <Heading as="h3" size="md" textAlign="center" p={2}>
        {title}
      </Heading>
      <Grid
        templateColumns="repeat(4,1fr)"
        templateRows="repeat(4,1fr)"
        fontSize={20}
        gap={2}
      >
        <GridItem
          alignSelf="center"
          colSpan={4}
          fontSize={12}
          borderWidth="1px"
          borderStyle="solid"
          bg={
            isValue()
              ? isChange
                ? isChangeUp()
                  ? "ui.secondary"
                  : "blue.400"
                : "ui.main"
              : "ui.main"
          }
          color="ui.light"
        >
          <Text textAlign="center">{itemTitle}</Text>
        </GridItem>
        <GridItem
          colSpan={isChange ? 2 : 4}
          display={isValue() ? "block" : "none"}
        >
          <Center>
            <Text>{value ? value : "-"}</Text>
          </Center>
        </GridItem>
        <GridItem
          colSpan={isValue() ? 2 : 4}
          display={isChange ? "block" : "none"}
        >
          <Center>
            <Text>{changeValue ? `${changeValue}%` : "-"}</Text>
          </Center>
        </GridItem>
        <GridItem
          alignSelf="center"
          colSpan={4}
          fontSize={12}
          borderWidth="1px"
          borderStyle="solid"
          bg={
            isValue()
              ? isChange
                ? isChangeUp()
                  ? "ui.secondary"
                  : "blue.400"
                : "ui.main"
              : "ui.main"
          }
          color="ui.light"
        >
          <Text textAlign="center">前年期中間期</Text>
        </GridItem>
        <GridItem
          colSpan={isChange ? 2 : 4}
          fontWeight={600}
          display={isValue() ? "block" : "none"}
        >
          <Center>
            <Text>{priValue ? priValue : "-"}</Text>
          </Center>
        </GridItem>
        <GridItem
          colSpan={isValue() ? 2 : 4}
          display={isChange == false ? "none" : "block"}
          fontWeight={600}
        >
          <Center>
            <Text>{priChangeValue ? `${priChangeValue}%` : "-"}</Text>
          </Center>
        </GridItem>
      </Grid>
    </GridItem>
  );
};
