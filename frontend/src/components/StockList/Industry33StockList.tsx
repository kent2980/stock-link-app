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
    queryKey: ["industry33Name", industry_33_code],
    queryFn: () => {
      return JpxService.readIndustryName({
        type: 33,
        code: industry_33_code,
      });
    },
  });

  const { data } = useSuspenseQuery({
    queryKey: ["Industry33StockList", industry_33_code],
    queryFn: () => {
      return InformationService.getDocumentList({
        reportTypes: ["edjp", "edif", "edus"],
        industry33Code: industry_33_code,
      });
    },
    gcTime: 0,
    staleTime: 0,
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

export default Industry33StockList;
