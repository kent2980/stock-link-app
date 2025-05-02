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
    queryKey: ["industryName", industry_17_code],
    queryFn: () => {
      return JpxService.readIndustryName({
        type: 17,
        code: industry_17_code,
      });
    },
  });

  const { data } = useSuspenseQuery({
    queryKey: ["stockList", industry_17_code],
    queryFn: () => {
      return InformationService.getDocumentList({
        reportTypes: ["edjp", "edif", "edus"],
        industry17Code: industry_17_code,
      });
    },
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
      <StockList data={data} />
    </>
  );
};

export default Industry17StockList;
