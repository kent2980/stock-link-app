import { Box, Checkbox, Skeleton, Wrap, WrapItem } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useStore } from "@tanstack/react-store";
import { Suspense, useEffect, useState } from "react";
import { JpxService } from "../../client";
import { IndustriesStore } from "../../Store/IndustriesStore";

function CustomCheckboxArea() {
  return (
    <Box p={4}>
      <Wrap spacing={2}>
        <Suspense
          fallback={Array(10).map((_, index) => (
            <WrapItem key={index}>
              <Skeleton h="20px" w="100px" />
            </WrapItem>
          ))}
        >
          <CustomWrapItem />
        </Suspense>
      </Wrap>
    </Box>
  );
}

export default CustomCheckboxArea;

const CustomWrapItem: React.FC = () => {
  const { industry17Code: code } = useStore(IndustriesStore, (state) => state);
  const { data: industry } = useSuspenseQuery({
    queryKey: ["Industries_17", code],
    queryFn: async () => {
      return await JpxService.readSelectIndustries({
        industry17Code: code ?? 0,
      });
    },
    staleTime: 1000 * 60 * 60 * 24 * 30, // 30 days
    gcTime: 1000 * 60 * 60 * 24 * 30, // 30 days
  });

  const [checkedItems, setCheckedItems] = useState<number[]>([]); // Keep track of checked items

  useEffect(() => {
    if (industry?.data) {
      const initialCheckedItems = industry.data.map((item) => item.code);
      setCheckedItems(initialCheckedItems);
    }
  }, [industry]);

  const handleCheckedItems = (code: number) => {
    setCheckedItems((prevCheckedItems) =>
      prevCheckedItems.includes(code)
        ? prevCheckedItems.filter((item) => item !== code)
        : [...prevCheckedItems, code]
    );
  };

  useEffect(() => {
    IndustriesStore.setState((state) => ({
      ...state,
      industry33Code: checkedItems,
    }));
  }, [checkedItems]);

  return (
    <>
      {industry?.data.map((item) => (
        <WrapItem key={item.code}>
          <Checkbox
            key={item.code}
            value={item.code}
            bg="gray.100"
            p={2}
            borderRadius="md"
            boxShadow="md"
            isChecked={checkedItems.includes(item.code)}
            onChange={() => handleCheckedItems(item.code)}
          >
            {item.name}
          </Checkbox>
        </WrapItem>
      ))}
    </>
  );
};
