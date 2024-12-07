import { Center, Grid, GridProps, HStack, Text } from "@chakra-ui/react";
import dayjs from "dayjs";
import React from "react";

const ShortHeader: React.FC<GridProps> = (props) => {
  return (
    <Grid
      {...props}
      bg="ui.main"
      h="50px"
      opacity={{ base: 1, md: 0 }}
      w={{ base: "full", md: "720px" }}
      templateColumns="repeat(4, 1fr)"
      color="white"
      fontWeight={800}
    >
      <ShortHeaderChildren />
    </Grid>
  );
};

export default ShortHeader;

const ShortHeaderChildren: React.FC = () => {
  return (
    <>
      <Center fontSize="14px">
        <HStack spacing={1}>
          <Text>{dayjs().format("YYYY.MM.DD")}</Text>
          <Text
            border="1px solid white"
            w="22px"
            h="22px"
            borderRadius="2px"
            textAlign="center"
            display="flex"
            alignItems="center"
            justifyContent="center"
          >
            {dayjs().format("dd")}
          </Text>
        </HStack>
      </Center>
      <Center>BookMark</Center>
      <Center>NewRelease</Center>
      <Center>Settings</Center>
    </>
  );
};
