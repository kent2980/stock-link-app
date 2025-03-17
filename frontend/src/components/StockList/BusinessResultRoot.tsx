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
    <Card.Root w={{ base: "100%", md: "70%" }} borderRadius={0}>
      <Card.Header p={3}>
        <Heading size="md">{title}</Heading>
      </Card.Header>
      <Card.Body p={3}>
        <Flex direction="column" gap={1} alignItems="center">
          <DataList.Root
            orientation="horizontal"
            divideY="1px"
            minW="100%"
            divideColor={"gray.400"}
            divideStyle={"solid"}
            gap={0}
          >
            {children}
          </DataList.Root>
        </Flex>
      </Card.Body>
    </Card.Root>
  );
};

export default BusinessResultRoot;
