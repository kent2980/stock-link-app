import {
  Box,
  BoxProps,
  Input,
  InputAddon,
  InputGroup,
  useColorModeValue,
} from "@chakra-ui/react";
import React from "react";

interface ScreenInputProps extends BoxProps {
  children: string;
  inputType: string;
  defaultValue?: string;
  max?: string;
  onChangeEvent?: (event: React.ChangeEvent<HTMLInputElement>) => void;
}

/**
 * スクリーンブロック
 * @param props BoxProps
 */
const ScreenInput: React.FC<ScreenInputProps> = (props) => {
  const { children, inputType, defaultValue, max, onChangeEvent } = props;
  const borderColor = useColorModeValue("#d1d9e0", "#ffffff29");
  return (
    <>
      <Box {...props}>
        <InputGroup size={"sm"}>
          <InputAddon>{children}</InputAddon>
          <Input
            type={inputType}
            border="1px solid"
            borderColor={borderColor}
            borderRadius={2}
            fontSize={13}
            textAlign="center"
            defaultValue={defaultValue ?? ""}
            max={max ?? ""}
            onChange={onChangeEvent}
          />
        </InputGroup>
      </Box>
    </>
  );
};

export default ScreenInput;
