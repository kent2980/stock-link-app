import { DataList } from "@chakra-ui/react";

interface BusinessResultItemsProps {
  label: string;
  curChange: JSX.Element;
  preChange?: JSX.Element | null;
}

const BusinessResultItems: React.FC<BusinessResultItemsProps> = ({
  label,
  curChange,
  preChange = null,
}: BusinessResultItemsProps) => {
  return (
    <DataList.Item pt="4" gap={1} fontSize={{ base: "sm", md: "md" }}>
      <DataList.ItemLabel w={preChange ? { base: "20%", md: "40%" } : "55%"}>
        {label}
      </DataList.ItemLabel>
      <DataList.ItemValue w={preChange ? { base: "40%", md: "30%" } : "45%"}>
        {curChange}
      </DataList.ItemValue>
      {preChange && (
        <DataList.ItemValue w={{ base: "40%", md: "30%" }}>
          {preChange}
        </DataList.ItemValue>
      )}
    </DataList.Item>
  );
};

export default BusinessResultItems;
