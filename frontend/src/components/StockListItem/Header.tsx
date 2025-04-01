import { JpxService, WikiService } from "@/client";
import { Box, Heading, Image, Link, Text, TextProps } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { Info } from "lucide-react";
import React, { Suspense } from "react";
import logo_list from "../../json/logo_list.json";
import { Tooltip } from "../ui/tooltip";

interface HeaderProps {
  company_name?: string;
  securities_code?: string;
}

const Header: React.FC<HeaderProps> = ({
  company_name = "GLOE株式会社",
  securities_code = "9565",
}) => {
  const logo_name =
    logo_list.find((item) => item.code === securities_code)?.file_name || ""; // デフォルトロゴURLを設定
  const logo_url = `/assets/images/stock_logo/${logo_name}`; // 画像のURLを生成

  return (
    <Box mb={2} pb={3}>
      <Box display="flex" justifyContent="left" mb={4} p={2} borderRadius="md">
        <Image src={logo_url} alt="企業ロゴ" h={5} borderRadius="lg" />
      </Box>
      <Box>
        <Box display="flex" alignItems="center" mb={1}>
          <Heading as="h2" fontSize="xl" fontWeight="bold" mr={2}>
            {company_name}
          </Heading>
          <Text fontSize="sm" color="gray.500">
            {securities_code}
          </Text>
        </Box>
        <Box mb={2}>
          <Suspense fallback={<Text>Loading...</Text>}>
            <JpxDataDisplay code={securities_code} />
          </Suspense>
        </Box>
        <Box display="flex" alignItems="center">
          <Tooltip content="企業詳細情報">
            <Box as="span" display="inline-flex" alignItems="center" mr={1}>
              <Info size="16" color="#3b8af8" />
            </Box>
          </Tooltip>
          <Text fontSize="xs" color="gray.500">
            <Suspense fallback={<Text>Loading...</Text>}>
              <WikiText code={securities_code} />
            </Suspense>
          </Text>
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
    <Text fontSize="xs" color="gray.500" {...props}>
      {data.market_or_type.replace("(内国株式)", "市場")} /{" "}
      {data.industry_33_name} [{data.industry_17_name}]
    </Text>
  );
};

const WikiText: React.FC<SelectCodeProps> = ({ code, ...props }) => {
  if (!code) {
    return <Text {...props}>企業情報がありません</Text>;
  }

  const { data: wiki } = useSuspenseQuery({
    queryKey: ["wiki", { code: code }],
    queryFn: async () => {
      try {
        return await WikiService.getStockWikiItem({
          code: code,
        });
      } catch (error) {
        console.error(error);
        return {
          description: null,
          url: null,
        };
      }
    },
  });

  if (wiki.description === null || wiki.description === undefined) {
    return <Text {...props}>企業情報がありません</Text>;
  }
  return (
    <>
      <Text {...props}>{wiki.description}</Text>
      <Text>
        (<Link href={wiki.url ?? ""}>引用:Wikipediaより</Link>)
      </Text>
    </>
  );
};

export default Header;
