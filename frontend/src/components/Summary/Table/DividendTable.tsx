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
  /**
   * ラベル
   */
  label: string;
  /**
   * 今期実績
   */
  resultValue: string;
  /**
   * 昨年実績
   */
  priResultValue: string;
  /**
   * 今期予想
   */
  forValue: string;
}

interface DividendTableProps {
  dividends: DividendPerShare[];
}

const DividendTable: React.FC<DividendTableProps> = ({ dividends }) => {
  return (
    <TableContainer border="1px solid #e2e8f0" padding="16px" bg="ui.light">
      <Table size="sm" variant="dividend" p={2}>
        <TableCaption>配当の状況</TableCaption>
        <Thead>
          <Tr>
            <Th>会計期間</Th>
            <Th>今期実績</Th>
            <Th>今期予想</Th>
            <Th>昨年実績</Th>
          </Tr>
        </Thead>
        <Tbody>
          {dividends.map((dividend) => (
            <Tr key={dividend.label}>
              <Th>{dividend.label}</Th>
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
