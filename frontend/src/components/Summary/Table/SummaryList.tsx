import {
  Flex,
  Grid,
  GridItem,
  Icon,
  List,
  ListItem,
  Text,
} from "@chakra-ui/react";
import React from "react";
import { FaCaretDown, FaCaretUp } from "react-icons/fa";
import { SummaryProps, SummaryPropsList } from "../Props/SummaryProps";

const SummaryList: React.FC<SummaryPropsList> = ({ summaries }) => {
  const selectSummaries = summaries.filter((summary) => {
    return summary.value?.cur || summary.changeValue?.cur;
  });

  function getGridItem(summary: SummaryProps) {
    if (
      summary.value?.cur === undefined &&
      summary.changeValue?.cur != undefined
    ) {
      return <NonValueSummaryGrid {...summary} />;
    } else if (
      summary.changeValue?.cur === undefined &&
      summary.value?.cur != undefined &&
      summary.value.pri != undefined
    ) {
      return <NonChangeValueSummaryGrid {...summary} />;
    } else if (
      summary.value?.pri === undefined &&
      summary.changeValue?.pri === undefined &&
      summary.changeValue?.cur !== undefined
    ) {
      return <NonPriValueSummaryGrid {...summary} />;
    } else if (
      summary.value?.cur !== undefined &&
      summary.value.pri === undefined
    ) {
      return <ValueOnlySummaryGrid {...summary} />;
    } else {
      return <DefaultSummaryGrid {...summary} />;
    }
  }

  return (
    <List spacing={3} border="1px solid #e2e8f0" padding="16px" bg="ui.light">
      {selectSummaries.map((summary, index) => (
        <ListItem
          key={index}
          display="flex"
          alignItems="center"
          padding="8px 0"
          borderBottom={
            index < selectSummaries.length - 1 ? "1px solid #e2e8f0" : "none"
          }
        >
          <Grid
            gap={2}
            templateColumns="repeat(10, 1fr)"
            templateRows="repeat(3, auto)"
            w={"100%"}
          >
            {getGridItem(summary)}
          </Grid>
        </ListItem>
      ))}
    </List>
  );
};

export default SummaryList;

const DefaultSummaryGrid: React.FC<SummaryProps> = (summary) => {
  return (
    <>
      <GridItem colSpan={10}>
        <Text fontSize={10} fontWeight={800} color="gray.600">
          {summary.title}
        </Text>
      </GridItem>
      <GridItem textAlign="left" colSpan={6} fontSize={12} alignSelf="center">
        今年度実績
      </GridItem>
      <GridItem textAlign="left" colSpan={4} fontSize={10} alignSelf="center">
        昨年度実績
      </GridItem>
      <GridItem
        textAlign="center"
        fontWeight="bold"
        colSpan={3}
        alignSelf="center"
        fontSize={20}
      >
        <Flex justifyContent="center" gap={1}>
          <Text alignSelf="center">{summary.value?.cur}</Text>
          <Text alignSelf="center" fontSize={12}>
            {summary.valueScale}
          </Text>
        </Flex>
      </GridItem>
      <GridItem
        textAlign="left"
        colSpan={3}
        alignSelf="center"
        fontSize={20}
        fontWeight={800}
      >
        <Text>
          {summary.changeValue?.cur && summary.changeValue.cur > 0 ? (
            <Icon as={FaCaretUp} color="#ec7158" />
          ) : (
            <Icon as={FaCaretDown} color="#23b87c" />
          )}
          {summary.changeValue?.cur?.toString().replace("-", "")}%
        </Text>
      </GridItem>
      <GridItem
        textAlign="center"
        fontWeight="bold"
        colSpan={2}
        alignSelf="center"
        fontSize={12}
      >
        <Flex justifyContent="center" gap={1}>
          <Text alignSelf="center">{summary.value?.pri}</Text>
          <Text fontSize={8} alignSelf="center">
            {summary.valueScale}
          </Text>
        </Flex>
      </GridItem>
      <GridItem textAlign="left" colSpan={2} alignSelf="center" fontSize={14}>
        <Text justifyContent="flex-end">
          {summary.changeValue?.pri && summary.changeValue.pri > 0 ? (
            <Icon as={FaCaretUp} color="#ec7158" />
          ) : (
            <Icon as={FaCaretDown} color="#23b87c" />
          )}
          {summary.changeValue?.pri?.toString().replace("-", "")}%
        </Text>
      </GridItem>
    </>
  );
};

const NonChangeValueSummaryGrid: React.FC<SummaryProps> = (summary) => {
  return (
    <>
      <GridItem colSpan={10}>
        <Text fontSize={10} fontWeight={800} color="gray.600">
          {summary.title}
        </Text>
      </GridItem>
      <GridItem textAlign="left" colSpan={6} fontSize={12} alignSelf="center">
        今年度実績
      </GridItem>
      <GridItem textAlign="left" colSpan={4} fontSize={10} alignSelf="center">
        昨年度実績
      </GridItem>
      <GridItem
        textAlign="center"
        fontWeight="bold"
        colSpan={6}
        alignSelf="center"
        fontSize={20}
      >
        <Flex justifyContent="center" gap={1}>
          <Text alignSelf="center">{summary.value?.cur}</Text>
          <Text fontSize={12} alignSelf="center">
            {summary.valueScale}
          </Text>
        </Flex>
      </GridItem>
      <GridItem
        textAlign="center"
        fontWeight="bold"
        colSpan={4}
        alignSelf="center"
        fontSize={12}
      >
        <Flex justifyContent="center" gap={1}>
          <Text alignSelf="center">{summary.value?.pri}</Text>
          <Text fontSize={10} alignSelf="center">
            {summary.valueScale}
          </Text>
        </Flex>
      </GridItem>
    </>
  );
};

const NonValueSummaryGrid: React.FC<SummaryProps> = (summary) => {
  return (
    <>
      <GridItem colSpan={10}>
        <Text fontSize={10} fontWeight={800} color="gray.600">
          {summary.title}
        </Text>
      </GridItem>
      <GridItem textAlign="left" colSpan={6} fontSize={12} alignSelf="center">
        今年度実績
      </GridItem>
      <GridItem textAlign="left" colSpan={4} fontSize={10} alignSelf="center">
        昨年度実績
      </GridItem>
      <GridItem fontWeight="bold" colSpan={6} alignSelf="center" fontSize={20}>
        <Flex justifyContent="center" gap={1}>
          <Text alignSelf="center">{summary.changeValue?.cur}</Text>
          <Text alignSelf="center">{summary.valueScale}</Text>
        </Flex>
      </GridItem>
      <GridItem
        textAlign="center"
        fontWeight="bold"
        colSpan={4}
        alignSelf="center"
        fontSize={12}
      >
        <Flex justifyContent="center" gap={1}>
          <Text alignSelf="center">{summary.changeValue?.pri}</Text>
          <Text fontSize={10} alignSelf="center">
            {summary.valueScale}
          </Text>
        </Flex>
      </GridItem>
    </>
  );
};

const NonPriValueSummaryGrid: React.FC<SummaryProps> = (summary) => {
  return (
    <>
      <GridItem colSpan={10}>
        <Text fontSize={10} fontWeight={800} color="gray.600">
          {summary.title}
        </Text>
      </GridItem>
      <GridItem
        textAlign="center"
        fontWeight="bold"
        colSpan={10}
        alignSelf="center"
        fontSize={20}
      >
        <Flex justifyContent="center" gap={8}>
          <Flex gap={1}>
            <Text alignSelf="center">{summary.value?.cur}</Text>
            <Text fontSize={12} alignSelf="center">
              {summary.valueScale}
            </Text>
          </Flex>
          <Text>
            {summary.changeValue?.cur && summary.changeValue?.cur > 0 ? (
              <Icon as={FaCaretUp} color="#ec7158" />
            ) : (
              <Icon as={FaCaretDown} color="#23b87c" />
            )}
            {summary.changeValue?.cur.toString().replace("-", "")}%
          </Text>
        </Flex>
      </GridItem>
    </>
  );
};

const ValueOnlySummaryGrid: React.FC<SummaryProps> = (summary) => {
  return (
    <>
      <GridItem colSpan={10}>
        <Text fontSize={10} fontWeight={800} color="gray.600">
          {summary.title}
        </Text>
      </GridItem>
      <GridItem
        textAlign="center"
        fontWeight="bold"
        colSpan={10}
        alignSelf="center"
        fontSize={20}
      >
        <Flex justifyContent="center" gap={1}>
          <Text alignSelf="center">{summary.value?.cur}</Text>
          <Text fontSize={12} alignSelf="center">
            {summary.valueScale}
          </Text>
        </Flex>
      </GridItem>
    </>
  );
};
