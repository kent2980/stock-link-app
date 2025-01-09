import {
  Table,
  TableContainer,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
} from "@chakra-ui/react";
import React from "react";
import { SummaryProps, SummaryPropsList } from "../Props/SummaryProps";

const SummaryTable: React.FC<SummaryPropsList> = ({ summaries }) => {
  const isChangeValue = (changeValue: number | undefined): boolean => {
    return changeValue !== undefined;
  };
  const getThColSpan = (sms: SummaryProps[]) => {
    let count;
    sms.map((sm) => {
      if (isChangeValue(sm.changeValue?.cur)) {
        count = 2;
      } else {
        count = 1;
      }
    });
    return count;
  };

  return (
    <TableContainer
      borderStyle="solid"
      borderWidth="0.5px"
      borderColor="black"
      m={2}
      bg="ui.light"
    >
      <Table variant="dividend">
        <Thead>
          <Tr>
            <Th>科目</Th>
            <Th colSpan={getThColSpan(summaries)}>昨年度実績</Th>
            <Th colSpan={getThColSpan(summaries)}>今年度実績</Th>
          </Tr>
        </Thead>
        <Tbody>
          {summaries.map((sm, index) => (
            <Tr key={index}>
              <Th>{sm.title}</Th>
              <Td isNumeric>
                {sm.value?.pri
                  ? sm.valueScale
                    ? sm.value.pri + sm.valueScale
                    : sm.value.pri
                  : ""}
              </Td>
              {isChangeValue(sm.changeValue?.pri) && (
                <Td isNumeric>{`${sm.changeValue?.pri}%`}</Td>
              )}
              <Td isNumeric>
                {sm.value?.cur
                  ? sm.valueScale
                    ? sm.value.cur + sm.valueScale
                    : sm.value.cur
                  : ""}
              </Td>
              {isChangeValue(sm.changeValue?.cur) && (
                <Td isNumeric>{`${sm.changeValue}%`}</Td>
              )}
            </Tr>
          ))}
        </Tbody>
      </Table>
    </TableContainer>
  );
};

export default SummaryTable;
