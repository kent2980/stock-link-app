import { Spinner, SpinnerProps, Text, VStack } from "@chakra-ui/react";
import React from "react";

const CustomSpinner: React.FC<SpinnerProps> = (props) => {
  return (
    <>
      <VStack colorPalette="teal" m={10}>
        <Spinner color="colorPalette.600" {...props} />
        <Text color="colorPalette.600">Loading...</Text>
      </VStack>
    </>
  );
};
export default CustomSpinner;
