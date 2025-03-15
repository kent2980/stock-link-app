import { DocumentListPublic } from "@/client";
import { Box, Flex, Heading, Link, Text } from "@chakra-ui/react";

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
        <Heading as="h1" size={{ base: "md", md: "lg" }}>
          {item.securities_code}
        </Heading>
        <Heading as="h1" size={{ base: "md", md: "lg" }}>
          {item.company_name}
        </Heading>
      </Flex>
      <Box>
        <Text>
          公式サイト：
          <Link
            href={get_url(item.url)}
            color="ui.link"
            _hover={{ color: "ui.link_hover" }}
          >
            {item.url}
          </Link>
        </Text>
      </Box>
    </Flex>
  );
};

export default Header;
