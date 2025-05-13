import { DocumentListPublic, JpxService } from "@/client";
import { Box, Heading, Image, Text, TextProps } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { Suspense } from "react";
import { CiClock2 } from "react-icons/ci";
import logo_list from "../../logo/logo_list.json";

interface HeaderProps {
  item: DocumentListPublic;
}

const LogoDisplay: React.FC<{ logoUrl: string }> = ({ logoUrl }) => {
  return (
    <Box
      display="flex"
      justifyContent="flex-start"
      w={{ base: 16, md: 20 }}
      h={{ base: 16, md: 20 }}
      p={1}
      borderWidth={1}
      borderColor="gray.200"
      bg="#ffffffe3"
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
    document_name = "第一四半期報告書",
    insert_date = "2025-04-17T14:00:43.854091",
  },
}) => {
  const logo_name =
    logo_list.find((item) => item.code === securities_code)?.file_name || ""; // デフォルトロゴURLを設定
  const logo_url = `/assets/images/stock_logo/${logo_name}`; // 画像のURLを生成

  const dateStr = new Date(insert_date).toLocaleDateString("ja-JP", {
    //insertDateを日本語の形式で表示
    timeZone: "Asia/Tokyo",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
  return (
    <>
      <Box display="flex" flexDirection="column" gap={{ base: 1, md: 2 }}>
        <Box
          display="flex"
          justifyContent="flex-end"
          alignItems="center"
          gap={1}
        >
          <CiClock2 />
          <Text fontSize="12px" color="gray.500">
            {dateStr}
          </Text>
        </Box>
        <Box display="flex" alignItems="center" gap={2}>
          <LogoDisplay logoUrl={logo_url} />
          <Text fontSize="13px" color="gray.500">
            {securities_code}
          </Text>
          <Heading as="h2" fontSize="15px" fontWeight="bold">
            {company_name}
          </Heading>
        </Box>
        <Box
          display="flex"
          flexDirection="column"
          justifyContent="flex-start"
          alignItems="flex-start"
        >
          <Suspense fallback={<Text>Loading...</Text>}>
            <JpxDataDisplay code={securities_code} fontSize="11.5px" />
          </Suspense>
          <Text fontSize="11.5px" color="ui.main" mt={1} fontWeight="semibold">
            {document_name}
          </Text>
        </Box>
      </Box>
    </>
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
    gcTime: 30 * 24 * 60 * 60 * 1000, // 30 days
    staleTime: 30 * 24 * 60 * 60 * 1000, // 30 days
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
