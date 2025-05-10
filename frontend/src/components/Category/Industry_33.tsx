import { JpxService } from "@/client";
import { Badge, Center, Text, Wrap, WrapItem } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useNavigate } from "@tanstack/react-router";

const Industry13 = () => {
  const navigate = useNavigate();
  const { data } = useSuspenseQuery({
    queryKey: ["industry33"],
    queryFn: async () => {
      return await JpxService.readIndustryCount({
        type: 33,
      });
    },
  });
  const handleClick = (industry_33_code: number) => {
    navigate({
      to: "/stock/industry_33/$industry_33",
      params: {
        industry_33: String(industry_33_code),
      },
    });
  };
  return (
    <Wrap width="100%" maxWidth="1200px" gap={2} p={2}>
      {data.data.map((item, index) => (
        <WrapItem key={index}>
          <Center
            display="flex"
            justifyContent="space-between"
            alignItems="center"
            w="46vw"
            h="100px"
            p={6}
            bg="white"
            borderBottom="1px solid"
            borderColor="gray.200"
            borderRadius={"lg"}
            boxShadow="sm"
            onClick={() => handleClick(item.code)}
            gap={2}
          >
            <Text fontWeight="bold" fontSize="16px" color={"gray.600"}>
              {item.name}
            </Text>
            <Badge
              w="50px"
              justifyContent="center"
              alignItems="center"
              colorPalette="red"
            >
              {item.count}
            </Badge>
          </Center>
        </WrapItem>
      ))}
    </Wrap>
  );
};

export default Industry13;
