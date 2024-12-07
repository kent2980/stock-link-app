import {
  Box,
  Center,
  Grid,
  GridItem,
  GridItemProps,
  GridProps,
  Text,
  VStack,
  keyframes,
} from "@chakra-ui/react";
import React, { forwardRef } from "react";
import { BsBookmarkCheckFill } from "react-icons/bs";
import { FaCloudDownloadAlt } from "react-icons/fa";
import { IoSettingsSharp } from "react-icons/io5";
import DateTab from "./DateTab";

const Header = forwardRef<HTMLDivElement, GridProps>((props, ref) => {
  return (
    <Grid
      {...props}
      ref={ref}
      as="header"
      templateColumns="repeat(3, 1fr)"
      templateRows="repeat(2, auto)"
      gap={4}
      bg="ui.main"
      color="white"
      w={{ base: "100%", md: "720px" }}
      py={4}
    >
      <GridChiles />
    </Grid>
  );
});

export default Header;

const GridChiles: React.FC = () => {
  return (
    <>
      <DateTab colSpan={3} />
      <Chiles_third />
      <NewRelease />
      <SettingTab />
    </>
  );
};

const iconSize = "28px";

const SettingTab: React.FC<GridItemProps> = (props) => {
  const spin = keyframes`
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
    `;
  return (
    <GridItem {...props}>
      <Center>
        <VStack>
          <Box>
            <IoSettingsSharp size={iconSize} />
          </Box>
          <Text fontSize="16px" fontWeight={600}>
            Settings
          </Text>
        </VStack>
      </Center>
    </GridItem>
  );
};

const Chiles_third: React.FC<GridItemProps> = (props) => {
  return (
    <GridItem {...props}>
      <Center>
        <VStack>
          <BsBookmarkCheckFill size={iconSize} />
          <Text fontSize="16px" fontWeight={600}>
            BookMark
          </Text>
        </VStack>
      </Center>
    </GridItem>
  );
};

const NewRelease: React.FC<GridItemProps> = (props) => {
  return (
    <GridItem {...props}>
      <Center>
        <VStack>
          <FaCloudDownloadAlt size={iconSize} />
          <Text fontSize="16px" fontWeight={600}>
            New Release
          </Text>
        </VStack>
      </Center>
    </GridItem>
  );
};
