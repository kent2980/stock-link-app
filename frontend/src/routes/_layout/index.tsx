import { Flex, Popover, PopoverTrigger, Stack, VStack } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import { useStore } from "@tanstack/react-store";
import { useEffect, useRef, useState } from "react";
import CustomButton from "../../components/Index/CustomButton";
import CustomPopoverContent from "../../components/Index/CustomPopoverContent";
import ReportList from "../../components/Index/ReportList";
import ScreenInput from "../../components/Index/ScreenInput";
import { HeaderStore } from "../../Store/HeaderStore";
import { IndexStore } from "../../Store/IndexStore";

export const Route = createFileRoute("/_layout/")({
  component: Dashboard,
});

function Dashboard() {
  const selectDate = useStore(IndexStore, (state) => state.selectDate);
  const vStackRef = useRef<HTMLDivElement>(null);
  const headerRef = useRef<HTMLDivElement>(null);
  const [headerHeight, setHeaderHeight] = useState<number>(0);
  const today = new Date().toISOString().split("T")[0];
  const [inputValue, setInputValue] = useState<string>(selectDate);

  useEffect(() => {
    // ヘッダーの高さを取得
    if (headerRef.current) {
      const headerPoint = headerRef.current.getBoundingClientRect().height;
      setHeaderHeight(headerPoint);
    }
    // ストアを更新
    HeaderStore.setState((state) => {
      return {
        ...state,
        title: "IRライブラリ",
      };
    });
    // ローカルストレージから取得
    const localDate = localStorage.getItem("selectDate");
    if (localDate) {
      setInputValue(localDate);
    }
  }, []);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    console.log(event.target.value);
    setInputValue(event.target.value);
    IndexStore.setState((state) => {
      return {
        ...state,
        selectDate: event.target.value,
      };
    });
    // ローカルストレージに保存
    localStorage.setItem("selectDate", event.target.value);
  };

  return (
    <VStack ref={vStackRef} spacing={6} mt={headerHeight} pt={6}>
      <Stack gap={4} direction={{ base: "column", md: "row" }}>
        <ScreenInput
          inputType="date"
          defaultValue={inputValue}
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
