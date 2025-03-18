import { DataList } from "@chakra-ui/react";

interface BusinessResultHeaderProps {
  columns: string[];
  widths: string[];
}

const BusinessResultHeader: React.FC<BusinessResultHeaderProps> = ({
  columns,
}: BusinessResultHeaderProps) => {
  return (
    <DataList.Item
      pt="4"
      gap={1}
      fontSize={{ base: "sm", md: "md" }}
      color={"gray.600"}
    >
      <DataList.ItemLabel w={{ base: "20%", md: "40%" }} />
      {columns.map((column, index) => (
        <DataList.ItemValue key={index} w={{ base: "40%", md: "30%" }}>
          {column}
        </DataList.ItemValue>
      ))}
    </DataList.Item>
  );
};

export default BusinessResultHeader;
