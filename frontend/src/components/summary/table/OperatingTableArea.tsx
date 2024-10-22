import {
  Box,
  BoxProps,
  Heading,
  Stack,
  Table,
  Tbody,
  Td,
  Text,
  Th,
  Thead,
  Tr,
} from "@chakra-ui/react";
import React from "react";
import { FaArrowCircleDown, FaArrowCircleUp } from "react-icons/fa";
import { abstract } from "../../../client";

interface OperatingTableAreaProps extends BoxProps {
  label: string;
  netSales: abstract | null | undefined;
  operatingIncome: abstract | null | undefined;
  ordinaryIncome: abstract | null | undefined;
  profit: abstract | null | undefined;
}

const OperatingTableArea: React.FC<OperatingTableAreaProps> = ({
  label,
  netSales,
  operatingIncome,
  ordinaryIncome,
  profit,
  ...props
}) => {
  return (
    <Box borderWidth="1px" {...props}>
      <Heading as="h2" size="xs" p={2} bg="gray.100">
        {label}
      </Heading>
      <Table variant="simple" size={"sm"}>
        <Thead>
          <Tr>
            <Th textAlign="center">売上高</Th>
            <Th textAlign="center">営業利益</Th>
            <Th textAlign="center">経常利益</Th>
            <Th textAlign="center">純利益</Th>
          </Tr>
        </Thead>
        <Tbody>
          <Tr>
            <OperatingTd item={netSales} />
            <OperatingTd item={operatingIncome} />
            <OperatingTd item={ordinaryIncome} />
            <OperatingTd item={profit} />
          </Tr>
        </Tbody>
      </Table>
    </Box>
  );
};

export default OperatingTableArea;

interface OperatingTdProps {
  item: abstract | undefined | null;
}

const OperatingTd: React.FC<OperatingTdProps> = ({ item }) => {
  return (
    <>
      <Td textAlign="center">
        <Stack direction={"column"} spacing={2}>
          <Text>{item?.Values?.value}</Text>
          <Box>
            <Stack
              direction={"row"}
              alignItems="center"
              spacing={1}
              display="flex"
              justifyContent="center"
              alignContent="center"
            >
              <Box textAlign="center" display="flex" alignItems="center">
                {item?.ChangeIn?.numeric !== undefined &&
                item.ChangeIn.numeric !== null &&
                item?.ChangeIn?.numeric > 0 ? (
                  <FaArrowCircleUp color="rgba(235, 44, 15, 0.702)" />
                ) : item?.ChangeIn?.numeric !== undefined &&
                  item.ChangeIn.numeric !== null &&
                  item?.ChangeIn?.numeric < 0 ? (
                  <FaArrowCircleDown color="rgba(18, 112, 195, 0.682)" />
                ) : (
                  <Text color="gray" textAlign="center" width="100%">
                    -
                  </Text>
                )}
                <Text>{item?.ChangeIn?.numeric}%</Text>
              </Box>
            </Stack>
          </Box>
        </Stack>
      </Td>
    </>
  );
};
