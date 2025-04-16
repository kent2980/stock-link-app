import { DocumentListPublic, JpxService } from "@/client";
import { Box, Heading, Image, Text, TextProps } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { Suspense } from "react";
import logo_list from "../../json/logo_list.json";

interface HeaderProps {
  item: DocumentListPublic;
}

const LogoDisplay: React.FC<{ logoUrl: string }> = ({ logoUrl }) => {
  return (
    <Box
      display="flex"
      justifyContent="flex-start"
      borderRadius="100%"
      w={12}
      h={12}
      borderWidth={1}
      borderColor="gray.200"
      bg="#ded16315"
      boxShadow="md"
    >
      <Image
        src={logoUrl}
        alt="企業ロゴ"
        objectFit="contain"
        w="100%"
        h="100%"
      />
    </Box>
  );
};

const Header: React.FC<HeaderProps> = ({
  item: {
    company_name = "ファーマライズホールディングス株式会社",
    securities_code = "2796",
  },
}) => {
  const logo_name =
    logo_list.find((item) => item.code === securities_code)?.file_name || ""; // デフォルトロゴURLを設定
  const logo_url = `/assets/images/stock_logo/${logo_name}`; // 画像のURLを生成

  return (
    <Box w="100%">
      <Box>
        <Box display="flex" alignItems="center" mb={1} gap={4}>
          <LogoDisplay logoUrl={logo_url} />
          <Text fontSize="13px" color="gray.500">
            {securities_code}
          </Text>
          <Heading as="h2" fontSize="15px" fontWeight="bold">
            {company_name}
          </Heading>
        </Box>
        <Box display="flex" justifyContent="flex-start" my={1}>
          <Suspense fallback={<Text>Loading...</Text>}>
            <JpxDataDisplay code={securities_code} fontSize="11.5px" />
          </Suspense>
        </Box>
      </Box>
    </Box>
  );
};

interface SelectCodeProps extends TextProps {
  code: string | null;
}

const JpxDataDisplay: React.FC<SelectCodeProps> = ({ code, ...props }) => {
  if (!code) {
    return <Text {...props}>企業情報がありません</Text>;
  }
  const { data } = useSuspenseQuery({
    queryKey: ["jpxData", { code: code }],
    queryFn: async () => {
      try {
        return await JpxService.readJpxStockInfoItem({
          code: code,
        });
      } catch (error) {
        console.error(error);
        return {
          market_or_type: null,
          industry_33_name: null,
          industry_17_name: null,
        };
      }
    },
  });

  if (
    data.market_or_type === null ||
    data.industry_33_name === null ||
    data.industry_17_name === null
  ) {
    return <Text {...props}>企業情報がありません</Text>;
  }

  return (
    <Text color="gray.500" {...props}>
      {data.market_or_type.replace("(内国株式)", "市場")} /{" "}
      {data.industry_33_name} [{data.industry_17_name}]
    </Text>
  );
};

export default Header;
