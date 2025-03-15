import { DataList } from "@chakra-ui/react";

interface BusinessResultRootProps {
  children: React.ReactNode;
}

const BusinessResultRoot: React.FC<BusinessResultRootProps> = ({
  children,
}) => {
  return (
    <DataList.Root orientation="horizontal" divideY="1px" maxW="md">
      {children}
    </DataList.Root>
  );
};

export default BusinessResultRoot;
