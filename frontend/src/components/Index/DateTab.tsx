import {
  Box,
  Center,
  GridItem,
  GridItemProps,
  HStack,
  Modal,
  ModalContent,
  ModalOverlay,
  useDisclosure,
  VStack,
} from "@chakra-ui/react";
import dayjs from "dayjs";
import React, { useEffect, useState } from "react";
import CustomDatePicker from "./CustomDatePicker";

const DateTab: React.FC<GridItemProps> = (props) => {
  const [time, setTime] = useState(dayjs().format("HH:mm:ss"));
  useEffect(() => {
    const timer = setInterval(() => {
      setTime(dayjs().format("HH:mm:ss"));
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  //   モーダルウインドウの設定
  const { isOpen, onOpen, onClose } = useDisclosure();

  return (
    <GridItem {...props}>
      <Center onClick={onOpen}>
        <VStack spacing={0}>
          <Box fontSize="20px" fontWeight={800} alignSelf="flex-start">
            {dayjs().format("YYYY")}
          </Box>
          <HStack>
            <Box fontSize="60px" fontWeight={800}>
              {dayjs().format("MM.DD")}
            </Box>
            <Box
              fontSize="28px"
              fontWeight={800}
              border="1px solid white"
              borderRadius="5px"
              w="40px"
              h="40px"
              textAlign="center"
              display="flex"
              alignItems="center"
              justifyContent="center"
            >
              {dayjs().format("dd")}
            </Box>
          </HStack>
          <Box fontSize="20px" fontWeight={800} alignSelf="flex-end">
            {time}
          </Box>
        </VStack>
      </Center>
      <CustomModal isOpen={isOpen} onClose={onClose} />
    </GridItem>
  );
};

export default DateTab;

interface CustomModalProps {
  isOpen: boolean;
  onClose: () => void;
}

const CustomModal: React.FC<CustomModalProps> = ({ isOpen, onClose }) => {
  return (
    <>
      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <CustomDatePicker />
        </ModalContent>
      </Modal>
    </>
  );
};
