import { Heading, Table } from "@chakra-ui/react";
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
      <Table.Root>
        <Table.Header>
          <Table.Row>
            {data.labels.map((item, key) => (
              <Table.ColumnHeader key={key} colSpan={2}>
                {item.label}
              </Table.ColumnHeader>
            ))}
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {data.data.map(
            (item, key) =>
              item.result.is_active && (
                <Table.Row key={key}>
                  {item.result.data?.map((metric) => (
                    <>
                      <Table.Cell>{metric.value?.value}</Table.Cell>
                      <Table.Cell>{metric.change?.value}%</Table.Cell>
                    </>
                  ))}
                </Table.Row>
              )
          )}
        </Table.Body>
      </Table.Root>
    </>
  );
};

export default LatestUpdates;
