import { HeaderStore } from "@/Store/Store";
import { InformationService, JpxService } from "@/client";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { useEffect } from "react";
import StockList from "./StockList";

interface Industry17StockListProps {
  industry_17_code: number;
}

const Industry17StockList: React.FC<Industry17StockListProps> = ({
  industry_17_code,
}) => {
  const { data: IndustryName } = useSuspenseQuery({
    queryKey: ["industry17Name", industry_17_code],
    queryFn: () => {
      return JpxService.readIndustryName({
        type: 17,
        code: industry_17_code,
      });
    },
    gcTime: 0,
    staleTime: 0,
  });

  const { data } = useSuspenseQuery({
    queryKey: ["Industry17StockList", industry_17_code],
    queryFn: () => {
      return InformationService.getDocumentList({
        reportTypes: ["edjp", "edif", "edus"],
        industry17Code: industry_17_code,
      });
    },
  });

  const sortData = data.data.slice().sort((a, b) => {
    return a.securities_code.localeCompare(b.securities_code);
  });

  // ストアを更新
  useEffect(() => {
    HeaderStore.setState((state) => ({
      ...state,
      SelectDateStr: null,
      CurrentCategory: IndustryName,
    }));
  }, [IndustryName]);
  return (
    <>
      <StockList data={sortData} count={sortData.length} />
    </>
  );
};

export default Industry17StockList;
