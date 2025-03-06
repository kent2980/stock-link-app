import { Box, Grid, GridItem, Skeleton, Text } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { Suspense } from "react";
import { JpxService } from "../../../../client";

interface SummaryHeaderProps {
  code: string;
}

const SummaryHeader: React.FC<SummaryHeaderProps> = ({ code }) => {
  return (
    <Box mt={4}>
      <Suspense fallback={<Skeleton height="20px" w="full" />}>
        <HeaderContents code={code} />
      </Suspense>
    </Box>
  );
};

export default SummaryHeader;

const HeaderContents: React.FC<SummaryHeaderProps> = ({ code }) => {
  const { data } = useSuspenseQuery({
    // 銘柄情報を取得
    queryKey: ["SummaryHeader", code],
    queryFn: async () => {
      return await JpxService.readJpxStockInfoItem({
        code: code,
      });
    },
  });

  const market_match: { [key: string]: string } = {
    "グロース(内国株式)": "東京証券取引所 グロース市場",
    "スタンダード(内国株式)": "東京証券取引所 スタンダード市場",
    "プライム(内国株式)": "東京証券取引所 プライム市場",
  };
  return (
    <Box fontWeight={500}>
      <Grid
        templateColumns={{
          base: "repeat(5, auto)",
          md: "auto auto auto auto auto",
        }}
        gap={{ base: 2, md: 10 }}
        justifyContent={{ base: "-moz-initial", md: "start" }}
      >
        <GridItem colSpan={1}>
          <Box
            as="span"
            px={2}
            py={0.4}
            border={"1px solid"}
            borderColor="ui.dark"
            borderRadius="md"
            boxShadow={"0 0 1px 1px #ffffffdd"}
          >
            {data?.code}
          </Box>
        </GridItem>
        <GridItem colSpan={{ base: 4, md: 1 }}>
          <Text fontSize="16px">{data?.name}</Text>
        </GridItem>
        <GridItem colSpan={1}>
          <Text>{data.industry_33_name}</Text>
        </GridItem>
        <GridItem colSpan={1}>
          <Text>{data.industry_17_name}</Text>
        </GridItem>
        <GridItem colSpan={1}>
          <Text>{market_match[data.market_or_type as string]}</Text>
        </GridItem>
      </Grid>
    </Box>
  );
};
