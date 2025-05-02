import { JpxService } from "@/client";
import { Badge, Box, Text } from "@chakra-ui/react";
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
      to: "/index/industry33/$industry_33",
      params: {
        industry_33: String(industry_33_code),
      },
    });
  };
  return (
    <Box
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
      width="100%"
      maxWidth="1200px"
      margin="0 auto"
    >
      {data.data.map((item, index) => (
        <Box
          key={index}
          display="flex"
          justifyContent="space-between"
          alignItems="center"
          width="100%"
          px="40px"
          py="20px"
          bg="white"
          borderBottom="1px solid"
          borderColor="gray.200"
          onClick={() => handleClick(item.code)}
        >
          <Text fontWeight="bold" fontSize="md" color={"gray.600"}>
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
        </Box>
      ))}
    </Box>
  );
};

export default Industry13;
