import { DocumentListPublic } from "@/client";
import { Box, Flex, Heading, Image, Link, Text } from "@chakra-ui/react";
import logo_json from "../../../public/assets/images/stock_logo/logo_list.json";

interface HeaderProps {
  item: DocumentListPublic;
}

const get_url = (url: string | null) => {
  if (url === null) {
    return undefined;
  }
  return url;
};

const Header: React.FC<HeaderProps> = ({ item }: HeaderProps) => {
  const get_logo_path = (code: string) => {
    const logo_dir = "/assets/images/stock_logo/";
    // jsonファイルを読み込む
    console.log(logo_json);
    // jsonファイルの中から一致するコードを探す

    const ext = logo_json.find(
      (logo) => logo.file_name === code + "_logo"
    )?.file_ext;

    const logo_path = `${logo_dir}${code}_logo.${ext}`;
    // ファイルが存在するかを確認するロジックを追加する場合はここに記述

    return logo_path; // 最初に一致したパスを返す
  };

  const get_logo = (code: string) => {
    const logo_path = get_logo_path(code);
    return logo_path ? (
      <Image src={logo_path} alt={`${code} logo`} w={200} />
    ) : null;
  };

  const logo = get_logo(item.securities_code);

  return (
    <Flex
      direction="column"
      gap={2}
      w="100%"
      alignItems="center"
      justifyContent="center"
    >
      <Flex
        dir="row"
        gap={2}
        w="100%"
        p={2}
        alignItems="center"
        justifyContent="center"
      >
        <Box className="logo">{logo && logo}</Box>
        <Heading as="h1" size={{ base: "md", md: "lg" }}>
          {item.securities_code}
        </Heading>
        <Heading as="h1" size={{ base: "md", md: "lg" }}>
          {item.company_name}
        </Heading>
      </Flex>
      {item.url ? (
        <Box>
          <Text fontSize={{ base: 14, md: 16 }}>
            公式サイト：
            <Link
              href={get_url(item.url)}
              color="ui.link"
              _hover={{ color: "ui.link_hover" }}
            >
              <Text>{item.url}</Text>
            </Link>
          </Text>
        </Box>
      ) : null}
    </Flex>
  );
};

export default Header;
