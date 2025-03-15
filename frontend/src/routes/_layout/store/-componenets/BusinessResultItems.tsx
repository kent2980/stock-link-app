import { DataList } from "@chakra-ui/react";

interface BusinessResultItemsProps {
  label: string;
  curChange: string;
  preChange: string;
  key: number;
}

const BusinessResultItems: React.FC<BusinessResultItemsProps> = ({
  label,
  curChange,
  preChange,
  key,
}: BusinessResultItemsProps) => {
  return (
    <>
      <DataList.Item key={key} pt="4">
        <DataList.ItemLabel w="30%">{label}</DataList.ItemLabel>
        <DataList.ItemValue>{curChange}</DataList.ItemValue>
        <DataList.ItemValue>({preChange})</DataList.ItemValue>
      </DataList.Item>
    </>
  );
};

export default BusinessResultItems;
