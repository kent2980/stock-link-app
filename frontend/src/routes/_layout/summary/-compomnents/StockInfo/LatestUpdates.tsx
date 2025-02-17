import {
  Heading,
  Table,
  TableContainer,
  Tbody,
  Td,
  Th,
  Tr,
} from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React from "react";
import { SummaryService } from "../../../../../client";

interface LatestUpdatesProps {
  code: string;
}

const LatestUpdates: React.FC<LatestUpdatesProps> = ({ code }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["latestUpdates", code],
    queryFn: async () => {
      return SummaryService.getOperatingResultsByCode({ code });
    },
  });
  return (
    <>
      <Heading as="h2" size="md">
        経営成績
      </Heading>
      <TableContainer>
        <Table>
          <thead>
            <Tr>
              {data.metrics.map((item, key) => (
                <Th key={key} colSpan={2}>
                  {item.label}
                </Th>
              ))}
            </Tr>
          </thead>
          <Tbody>
            <Tr>
              {data.metrics.map((item) => (
                <>
                  <Td>{item.value?.value}</Td>
                  <Td>{item.change?.value}%</Td>
                </>
              ))}
            </Tr>
          </Tbody>
        </Table>
      </TableContainer>
    </>
  );
};

export default LatestUpdates;
