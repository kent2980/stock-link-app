import { Flex, FlexProps, useColorModeValue } from "@chakra-ui/react";
import dayjs from "dayjs";
import { forwardRef } from "react";

const Header = forwardRef<HTMLDivElement, FlexProps>((props, ref) => {
  const bgColor = useColorModeValue("ui.light", "ui.dark");
  const textColor = useColorModeValue("ui.dark", "ui.light");
  const boxShadow = useColorModeValue(
    "1px 1px 4px #c0bcbc",
    "1px 1px 4px #000000"
  );

  const today = dayjs().format("YYYY.MM.DD(dd)");
  return (
    <Flex
      ref={ref}
      {...props}
      bg={bgColor}
      color={textColor}
      position="fixed"
      top={0}
      right={0}
      zIndex={3000}
      w={"100%"}
      p={3}
      boxShadow={boxShadow}
      fontSize={13}
    >
      {today}
    </Flex>
  );
});

export default Header;
