import { IxHeadTitlePublic } from "@/client";
import { Box, Heading, Image, Text } from "@chakra-ui/react";
import { Info } from "lucide-react";
import React from "react";
import logo_list from "../../json/logo_list.json";
import { Tooltip } from "../ui/tooltip";

interface HeaderProps {
  headItem?: IxHeadTitlePublic;
}

const Header: React.FC<HeaderProps> = ({
  headItem = {
    company_name: "日本オラクル株式会社",
    securities_code: "4716",
  },
}) => {
  const { company_name, securities_code } = headItem;
  const logo_name =
    logo_list.find((item) => item.code === securities_code)?.file_name || ""; // デフォルトロゴURLを設定
  const logo_url = `../../../public/assets/images/stock_logo/${logo_name}`; // 画像のURLを生成
  return (
    <Box mb={2} pb={3}>
      <Box display="flex" justifyContent="left" mb={4}>
        <Image src={logo_url} alt="企業ロゴ" h={4} borderRadius="lg" />
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
        <Box display="flex" alignItems="center">
          <Tooltip content="企業詳細情報">
            <Box as="span" display="inline-flex" alignItems="center" mr={1}>
              <Info size="16" color="#3b8af8" />
            </Box>
          </Tooltip>
          <Text fontSize="xs" color="gray.500">
            先端テクノロジーと持続可能なソリューションを提供するグローバルIT企業
          </Text>
        </Box>
      </Box>
    </Box>
  );
};

export default Header;
