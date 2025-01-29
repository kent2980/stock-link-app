import { Flex, FlexProps, useColorModeValue } from "@chakra-ui/react";
import { useStore } from "@tanstack/react-store";
import { forwardRef } from "react";
import { HeaderStore } from "../../Store/HeaderStore";

const Header = forwardRef<HTMLDivElement, FlexProps>((props, ref) => {
  const bgColor = useColorModeValue("ui.light", "ui.dark");
  const textColor = useColorModeValue("ui.dark", "ui.light");
  const boxShadow = useColorModeValue(
    "1px 1px 4px #c0bcbc",
    "1px 1px 4px #000000"
  );
  const title = useStore(HeaderStore, (state) => state.title);

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
      {title}
    </Flex>
  );
});

export default Header;
