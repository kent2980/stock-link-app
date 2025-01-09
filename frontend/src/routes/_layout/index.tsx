import { Flex, Popover, PopoverTrigger, Stack, VStack } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { useEffect, useRef, useState } from "react";
import CustomButton from "../../components/Index/CustomButton";
import CustomPopoverContent from "../../components/Index/CustomPopoverContent";
import ReportList from "../../components/Index/ReportList";
import ScreenInput from "../../components/Index/ScreenInput";

export const Route = createFileRoute("/_layout/")({
  component: Dashboard,
});

function Dashboard() {
  const vStackRef = useRef<HTMLDivElement>(null);
  const headerRef = useRef<HTMLDivElement>(null);
  const [headerHeight, setHeaderHeight] = useState<number>(0);
  const today = new Date().toISOString().split("T")[0];
  const [inputValue, setInputValue] = useState<string>(today);

  useEffect(() => {
    if (headerRef.current) {
      const headerPoint = headerRef.current.getBoundingClientRect().height;
      setHeaderHeight(headerPoint);
    }
  }, []);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    console.log(event.target.value);
    setInputValue(event.target.value);
  };

  return (
    <VStack ref={vStackRef} spacing={6} mt={headerHeight} pt={6}>
      <Stack gap={4} direction={{ base: "column", md: "row" }}>
        <ScreenInput
          inputType="date"
          defaultValue={today}
          max={today}
          w={{ base: "60vw", md: "20vw" }}
          onChangeEvent={handleInputChange}
        >
          日付
        </ScreenInput>
        <Flex gap={4} fontSize={10}>
          <Popover placement="bottom" closeOnBlur={false}>
            <PopoverTrigger>
              <CustomButton colorScheme="gray">抽出条件</CustomButton>
            </PopoverTrigger>
            <CustomPopoverContent />
          </Popover>
          <CustomButton colorScheme="gray">並べ替え</CustomButton>
          <CustomButton
            colorScheme="blue"
            onClick={() => console.log(inputValue)}
          >
            実行
          </CustomButton>
        </Flex>
      </Stack>
      <ReportList w="full" selectDate={inputValue} px={{ base: 0, md: 10 }} />
    </VStack>
  );
}
