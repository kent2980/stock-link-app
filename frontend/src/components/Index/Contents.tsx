import {
  Box,
  Flex,
  HStack,
  List,
  ListItem,
  Text,
  VStack,
} from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import { Link as RouterLink } from "@tanstack/react-router";
import dayjs from "dayjs";
import React from "react";
import { IxHeadTitlePublic, XbrlIxHeadService } from "../../client";
import EdifContents from "./Contents/EdifContents";
import EditContents from "./Contents/EditContents";
import EdjpContents from "./Contents/EdjpContents";
import EdusContents from "./Contents/EdusContents";
import EfjpContents from "./Contents/EfjpContents";
import RejpContents from "./Contents/RejpContents";
import RrdfContents from "./Contents/RrdfContents";
import RrfcContents from "./Contents/RrfcContents";
import RvdfContents from "./Contents/RvdfContents";
import RvfcContents from "./Contents/RvfcContents";

const Contents: React.FC = () => {
  const date_str = dayjs().format("YYYY-MM-DD");
  const { data, isPending, isError } = useQuery({
    queryKey: ["xbrlIxHead"],
    queryFn: () =>
      XbrlIxHeadService.selectIxHeadTitleItems({
        dateStr: "2024-10-30",
      }),
    staleTime: 1000 * 60 * 60 * 24,
    gcTime: 1000 * 60 * 60 * 24,
  });

  if (isError) {
    return <div>Error</div>;
  }

  if (isPending) {
    return <div>Loading...</div>;
  }

  if (data === undefined) {
    return <div>data is undefined</div>;
  }

  function isConsolidated(data: IxHeadTitlePublic): string {
    if (data.is_consolidated) {
      return "consolidated";
    } else {
      return "non_consolidated";
    }
  }

  function isSpecific(data: IxHeadTitlePublic): string {
    if (data.specific_business) {
      return "specific";
    } else {
      return "general";
    }
  }

  return (
    <Box color={"black"}>
      <List>
        {data.data.map((item: IxHeadTitlePublic) => (
          <RouterLink
            to={`/summary/$head_item_key/${item.report_type}`}
            params={{ head_item_key: item.item_key }}
            key={item.item_key}
          >
            <ListItem>
              <CustomListItem item={item} />
            </ListItem>
          </RouterLink>
        ))}
      </List>
    </Box>
  );
};

export default Contents;

interface CustomListItemProps {
  item: IxHeadTitlePublic;
}

const CustomListItem: React.FC<CustomListItemProps> = ({ item }) => {
  const update_date = dayjs(item.update_date).format("YYYY-MM-DD HH:mm:ss");
  return (
    <VStack borderBottom="0.2px solid #686868" pt={4} pb={2} mx={5} spacing={4}>
      <Flex alignSelf="flex-start" gap={4}>
        <Text
          border="1px solid #a7a7a7"
          borderRadius="md"
          h="30px"
          w="50px"
          justifyContent="center"
          display="flex"
          alignItems="center"
          fontSize="16px"
        >
          {item.securities_code}
        </Text>
        <Text>{item.company_name}</Text>
      </Flex>
      <Flex alignSelf="flex-start" gap={4}>
        <Text fontSize="12px">主要セクター :</Text>
      </Flex>
      <Flex alignSelf="flex-start" gap={4}>
        <Text fontSize="12px">{item.document_name}</Text>
      </Flex>
      <Flex>
        <ReportTypeContents item={item} />
      </Flex>
      <HStack alignSelf="flex-end">
        <Text fontSize="12px" color="#3e3d3d" fontWeight={500}>
          更新日 : {update_date}
        </Text>
      </HStack>
    </VStack>
  );
};

interface ReportTypeContentsProps {
  item: IxHeadTitlePublic;
}

const ReportTypeContents: React.FC<ReportTypeContentsProps> = ({ item }) => {
  if (item.report_type === "edjp") {
    return <EdjpContents />;
  } else if (item.report_type === "edus") {
    return <EdusContents />;
  } else if (item.report_type === "edif") {
    return <EdifContents />;
  } else if (item.report_type === "edit") {
    return <EditContents />;
  } else if (item.report_type === "rvdf") {
    return <RvdfContents />;
  } else if (item.report_type === "rvfc") {
    return <RvfcContents />;
  } else if (item.report_type === "rejp") {
    return <RejpContents />;
  } else if (item.report_type === "rrdf") {
    return <RrdfContents />;
  } else if (item.report_type === "rrfc") {
    return <RrfcContents />;
  } else if (item.report_type === "efjp") {
    return <EfjpContents />;
  }
};
