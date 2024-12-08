import {
  Table,
  TableCaption,
  TableContainer,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
} from "@chakra-ui/react";
import React from "react";

export interface DividendPerShare {
  label: string;
  resultValue: string;
  priResultValue: string;
  forValue: string;
}

interface DividendTableProps {
  dividends: DividendPerShare[];
}

const DividendTable: React.FC<DividendTableProps> = ({ dividends }) => {
  return (
    <TableContainer
      bg="ui.light"
      borderRadius="md"
      m={1}
      p={2}
      border="0.5px solid black"
    >
      <Table size="sm" variant="simple">
        <TableCaption>配当の状況</TableCaption>
        <Thead>
          <Tr>
            <Th>会計期間</Th>
            <Th isNumeric>今期実績</Th>
            <Th isNumeric>今期予想</Th>
            <Th isNumeric>昨年実績</Th>
          </Tr>
        </Thead>
        <Tbody>
          {dividends.map((dividend) => (
            <Tr key={dividend.label}>
              <Td>{dividend.label}</Td>
              <Td isNumeric>{dividend.resultValue}</Td>
              <Td isNumeric>{dividend.forValue}</Td>
              <Td isNumeric>{dividend.priResultValue}</Td>
            </Tr>
          ))}
        </Tbody>
      </Table>
    </TableContainer>
  );
};

export default DividendTable;
