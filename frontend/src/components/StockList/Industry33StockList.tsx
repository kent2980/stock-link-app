import { HeaderStore } from "@/Store/Store";
import { InformationService, JpxService } from "@/client";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { useEffect } from "react";
import StockList from "./StockList";

interface Industry33StockListProps {
  industry_33_code: number;
}

const Industry33StockList: React.FC<Industry33StockListProps> = ({
  industry_33_code,
}) => {
  const { data: IndustryName } = useSuspenseQuery({
    queryKey: ["industryName", industry_33_code],
    queryFn: () => {
      return JpxService.readIndustryName({
        type: 33,
        code: industry_33_code,
      });
    },
  });

  const { data } = useSuspenseQuery({
    queryKey: ["stockList", industry_33_code],
    queryFn: () => {
      return InformationService.getDocumentList({
        reportTypes: ["edjp", "edif", "edus"],
        industry33Code: industry_33_code,
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

export default Industry33StockList;
