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

export interface IssuedSharesTableProp {
  issuedSharesEnd: {
    cur: string;
    pri: string;
    scale?: string;
  };
  treasurySharesEnd: {
    cur: string;
    pri: string;
    scale?: string;
  };
  avgSharesEnd: {
    cur: string;
    pri: string;
    scale?: string;
  };
}

interface IssuedSharesTableProps {
  items: IssuedSharesTableProp;
}

const IssuedSharesTable: React.FC<IssuedSharesTableProps> = ({ items }) => {
  return (
    <TableContainer bg="ui.light" p={2} border="1px solid #e2e8f0">
      <Table size={"sm"}>
        <Thead>
          <Tr>
            <Th></Th>
            <Th>今年度</Th>
            <Th>昨年度</Th>
          </Tr>
        </Thead>
        <Tbody>
          <Tr>
            <Th>期末発行済株式数</Th>
            <Td>
              {items.issuedSharesEnd.cur + (items.issuedSharesEnd.scale ?? "")}
            </Td>
            <Td>
              {items.issuedSharesEnd.pri + (items.issuedSharesEnd.scale ?? "")}
            </Td>
          </Tr>
          <Tr>
            <Th>期末自己株式数</Th>
            <Td>
              {items.treasurySharesEnd.cur +
                (items.treasurySharesEnd.scale ?? "")}
            </Td>
            <Td>
              {items.treasurySharesEnd.pri +
                (items.treasurySharesEnd.scale ?? "")}
            </Td>
          </Tr>
          <Tr>
            <Th>期末平均株式数</Th>
            <Td>{items.avgSharesEnd.cur + (items.avgSharesEnd.scale ?? "")}</Td>
            <Td>{items.avgSharesEnd.pri + (items.avgSharesEnd.scale ?? "")}</Td>
          </Tr>
        </Tbody>
      </Table>
    </TableContainer>
  );
};

export default IssuedSharesTable;
