import { Box, List, ListItem } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import dayjs from "dayjs";
import React from "react";
import { IxHeadTitlePublic, XbrlIxHeadService } from "../../client";

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
  return (
    <Box color={"black"}>
      <List>
        {data.data.map((item: IxHeadTitlePublic) => (
          <ListItem key={item.item_key} h="60px">
            {item.company_name}
          </ListItem>
        ))}
      </List>
    </Box>
  );
};

export default Contents;
