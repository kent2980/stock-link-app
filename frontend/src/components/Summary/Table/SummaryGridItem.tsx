import { Center, Grid, GridItem, Heading, Text } from "@chakra-ui/react";
import React from "react";

interface SummaryGridItemProps {
  title: string;
  itemTitle: string;
  value: string;
  changeValue: string;
  priValue: string;
  priChangeValue: string;
}

const SummaryGridItem: React.FC<SummaryGridItemProps> = ({
  title,
  itemTitle,
  value,
  changeValue,
  priValue,
  priChangeValue,
}) => {
  return (
    <GridItem bg="white" w="45vw" p={1} mx="auto">
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
          bg="ui.secondary"
          color="ui.light"
          borderRadius="3px"
        >
          <Text textAlign="center">{itemTitle}</Text>
        </GridItem>
        <GridItem colSpan={2}>
          <Center>
            <Text>{value ? value : "-"}</Text>
          </Center>
        </GridItem>
        <GridItem colSpan={2}>
          <Center>
            <Text>{changeValue ? `${changeValue}%` : "-"}</Text>
          </Center>
        </GridItem>
        <GridItem
          alignSelf="center"
          colSpan={4}
          fontSize={12}
          bg="ui.secondary"
          color="ui.light"
          borderRadius="3px"
        >
          <Text textAlign="center">前年期中間期</Text>
        </GridItem>
        <GridItem colSpan={2}>
          <Center>
            <Text>{priValue ? priValue : "-"}</Text>
          </Center>
        </GridItem>
        <GridItem colSpan={2}>
          <Center>
            <Text>{priChangeValue ? `${priChangeValue}%` : "-"}</Text>
          </Center>
        </GridItem>
      </Grid>
    </GridItem>
  );
};

export default SummaryGridItem;
