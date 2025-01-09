import {
  Box,
  Button,
  ButtonGroup,
  PopoverArrow,
  PopoverBody,
  PopoverCloseButton,
  PopoverContent,
  PopoverContentProps,
  PopoverFooter,
  PopoverHeader,
} from "@chakra-ui/react";
import React from "react";

const CustomPopoverContent: React.FC<PopoverContentProps> = (props) => {
  return (
    <PopoverContent {...props}>
      <PopoverHeader pt={4} fontWeight="bold" border="0">
        Manage Your Channels
      </PopoverHeader>
      <PopoverArrow bg="blue.800" />
      <PopoverCloseButton />
      <PopoverBody>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore.
      </PopoverBody>
      <PopoverFooter
        border="0"
        display="flex"
        alignItems="center"
        justifyContent="space-between"
        pb={4}
      >
        <Box fontSize="sm">Step 2 of 4</Box>
        <ButtonGroup size="sm">
          <Button colorScheme="green">Setup Email</Button>
          <Button colorScheme="blue">Next</Button>
        </ButtonGroup>
      </PopoverFooter>
    </PopoverContent>
  );
};

export default CustomPopoverContent;
