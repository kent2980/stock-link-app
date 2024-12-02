import {
  Box,
  Center,
  CenterProps,
  Grid,
  HStack,
  Text,
  VStack,
  keyframes,
} from "@chakra-ui/react";
import dayjs from "dayjs";
import React, { useEffect } from "react";
import { FaCloudDownloadAlt } from "react-icons/fa";
import { IoSettingsSharp } from "react-icons/io5";

const Header: React.FC = () => {
  return (
    <Grid
      as="header"
      templateColumns="repeat(2, 1fr)"
      templateRows="repeat(2, 1fr)"
      bg="#0f4d99"
      color="white"
      w={{ base: "100%", md: "720px" }}
      h="400px"
    >
      <GridChiles />
    </Grid>
  );
};

export default Header;

const GridChiles: React.FC = () => {
  return (
    <>
      <DateTab borderRight="2px solid white" borderBottom="2px solid white" />
      <Chiles_third
        borderLeft="2px solid white"
        borderBottom="2px solid white"
      />
      <NewRelease borderRight="2px solid white" borderTop="2px solid white" />

      <SettingTab borderLeft="2px solid white" borderTop="2px solid white" />
    </>
  );
};

const DateTab: React.FC<CenterProps> = (props) => {
  const [time, setTime] = React.useState(dayjs().format("HH:mm:ss"));
  useEffect(() => {
    const timer = setInterval(() => {
      setTime(dayjs().format("HH:mm:ss"));
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <Center {...props}>
      <VStack spacing={0}>
        <Box
          fontSize={["12px", "16px", "20px"]}
          fontWeight={800}
          alignSelf="flex-start"
        >
          {dayjs().format("YYYY")}
        </Box>
        <HStack>
          <Box fontSize={["24px", "32px", "48px"]} fontWeight={800}>
            {dayjs().format("MM.DD")}
          </Box>
          <Box
            fontSize="16px"
            fontWeight={800}
            border="1px solid white"
            borderRadius="5px"
            w="30px"
            h="30px"
            textAlign="center"
            display="flex"
            alignItems="center"
            justifyContent="center"
          >
            {dayjs().format("dd")}
          </Box>
        </HStack>
        <Box
          fontSize={["12px", "14px", "16px"]}
          fontWeight={800}
          alignSelf="flex-end"
        >
          {time}
        </Box>
      </VStack>
    </Center>
  );
};

const SettingTab: React.FC<CenterProps> = (props) => {
  const spin = keyframes`
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
    `;
  return (
    <Center {...props}>
      <VStack>
        <Box animation={`${spin} 20s linear infinite`}>
          <IoSettingsSharp size="50px" />
        </Box>
        <Text fontSize="16px" fontWeight={600}>
          Settings
        </Text>
      </VStack>
    </Center>
  );
};

const Chiles_third: React.FC<CenterProps> = (props) => {
  return <Center {...props}></Center>;
};

const NewRelease: React.FC<CenterProps> = (props) => {
  return (
    <Center {...props}>
      <VStack>
        <FaCloudDownloadAlt size="50px" />
        <Text fontSize="16px" fontWeight={600}>
          New Release
        </Text>
      </VStack>
    </Center>
  );
};
