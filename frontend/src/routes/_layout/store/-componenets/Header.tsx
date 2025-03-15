import { DocumentListPublic } from "@/client";
import { Flex, Text } from "@chakra-ui/react";

interface HeaderProps {
  item: DocumentListPublic;
}

const Header: React.FC<HeaderProps> = ({ item }: HeaderProps) => {
  return (
    <Flex dir="row" gap={2}>
      <Text>{item.securities_code}</Text>
      <Text>{item.company_name}</Text>
    </Flex>
  );
};

export default Header;
