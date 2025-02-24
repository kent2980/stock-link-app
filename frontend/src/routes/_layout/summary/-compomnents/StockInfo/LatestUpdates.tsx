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
      return SummaryService.getOperatingResults({ code });
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
              {data.labels.map((item, key) => (
                <Th key={key} colSpan={2}>
                  {item.label}
                </Th>
              ))}
            </Tr>
          </thead>
          <Tbody>
            {data.data.map(
              (item, key) =>
                item.metrics.is_active && (
                  <Tr key={key}>
                    {item.metrics.data?.map((metric) => (
                      <>
                        <Td>{metric.value?.value}</Td>
                        <Td>{metric.change?.value}%</Td>
                      </>
                    ))}
                  </Tr>
                )
            )}
          </Tbody>
        </Table>
      </TableContainer>
    </>
  );
};

export default LatestUpdates;
