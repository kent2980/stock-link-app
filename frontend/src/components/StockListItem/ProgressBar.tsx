import { Box, HStack, Progress } from "@chakra-ui/react";
import React from "react";

interface ProgressBarProps {
  value: number;
}
const ProgressBar: React.FC<ProgressBarProps> = ({ value }) => {
  return (
    <Box width="100%">
      <Progress.Root
        defaultValue={40}
        maxW="sm"
        animated
        striped
        colorPalette={"red"}
      >
        <HStack gap="5">
          <Progress.Label>進捗率</Progress.Label>
          <Progress.Track flex="1" borderRadius={"md"}>
            <Progress.Range />
          </Progress.Track>
          <Progress.ValueText>{value}%</Progress.ValueText>
        </HStack>
      </Progress.Root>
    </Box>
  );
};
export default ProgressBar;
