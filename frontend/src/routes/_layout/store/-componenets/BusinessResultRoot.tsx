import { Card, DataList, Flex, Heading } from "@chakra-ui/react";
interface BusinessResultRootProps {
  children: React.ReactNode;
  title: string;
}

const BusinessResultRoot: React.FC<BusinessResultRootProps> = ({
  children,
  title,
}) => {
  return (
    <Card.Root
      w={{ base: "100%", md: "70%" }}
      boxShadow={{ base: "sm", md: "md" }}
      bg="gray.100"
    >
      <Card.Body>
        <Flex direction="column" gap={1} alignItems="center">
          <Heading size="md">{title}</Heading>
          <DataList.Root orientation="horizontal" divideY="1px" minW="100%">
            {children}
          </DataList.Root>
        </Flex>
      </Card.Body>
    </Card.Root>
  );
};

export default BusinessResultRoot;
