import { DataList } from "@chakra-ui/react";

interface BusinessResultHeaderProps {
  preChange?: boolean | null;
}

const BusinessResultHeader: React.FC<BusinessResultHeaderProps> = ({
  preChange = null,
}: BusinessResultHeaderProps) => {
  return (
    <DataList.Item pt="4" gap={1} fontSize={{ base: "sm", md: "md" }}>
      <DataList.ItemLabel w={preChange ? { base: "20%", md: "40%" } : "55%"} />
      <DataList.ItemValue w={preChange ? { base: "40%", md: "30%" } : "45%"}>
        今期
      </DataList.ItemValue>
      {preChange && (
        <DataList.ItemValue w={{ base: "40%", md: "30%" }}>
          前年同期
        </DataList.ItemValue>
      )}
    </DataList.Item>
  );
};

export default BusinessResultHeader;
