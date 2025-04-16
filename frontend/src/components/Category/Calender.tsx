import { XbrlIxHeadService } from "@/client";
import { Box } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { useNavigate } from "@tanstack/react-router";

const Calender = () => {
  const { data } = useSuspenseQuery({
    queryKey: ["Calendar"],
    queryFn: async () => {
      return await XbrlIxHeadService.getCalendar();
    },
  });

  const navigate = useNavigate();
  const handleClick = (dateStr: string) => {
    navigate({
      to: "/index/date/$dateStr",
      params: {
        dateStr: dateStr,
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
      bg="gray.50"
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
          onClick={() => handleClick(item.reporting_date)}
        >
          <Box fontWeight="bold" fontSize="md" color={"gray.600"}>
            {item.reporting_date}
          </Box>
          <Box color="gray.600" fontSize="md">
            {item.count}件
          </Box>
        </Box>
      ))}
    </Box>
  );
};

export default Calender;
