import { Box, Button, Heading, Stack, Text, keyframes } from "@chakra-ui/react";
import { Link } from "@tanstack/react-router";
import React from "react";
import { FcGoogle } from "react-icons/fc";
import useAuth from "../../hooks/useAuth";

interface HomeProps {}

const Home: React.FC<HomeProps> = () => {
  const { logout } = useAuth();
  const handleLogout = async () => {
    logout();
  };
  const spin = keyframes`
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
    `;
  return (
    <>
      <Stack
        direction="column"
        spacing={10}
        p={4}
        h="full"
        justifyContent="center"
        alignContent="center"
      >
        <Heading color="red.400" fontSize="3xl" textAlign="center">
          Tdnet Link Navigation
        </Heading>
        <Box fontSize="14px" textAlign="center">
          <Text>Tdnetから配信されている、</Text>
          <Text>上場企業のIR(XBRL)から情報を引用しています。</Text>
          <Text>この情報は、株式投資においての</Text>
          <Text>参考情報としてのみ利用してください。</Text>
        </Box>
        <Stack
          direction="column"
          spacing={6}
          height="20vh"
          display="flex"
          justifyContent="center"
          alignItems="center"
        >
          <Button
            colorScheme="blue"
            size="lg"
            variant="outline"
            as={Link}
            to="/navigate/"
          >
            利用を開始する
          </Button>
          <Button
            colorScheme="red"
            size="lg"
            variant="outline"
            onClick={handleLogout}
          >
            ログアウト
          </Button>
        </Stack>
        <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          animation={`${spin} infinite 3s linear`}
        >
          <FcGoogle size="100px" />
        </Box>
      </Stack>
    </>
  );
};

export default Home;
