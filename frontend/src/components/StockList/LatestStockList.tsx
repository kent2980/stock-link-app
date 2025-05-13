import { HeaderStore } from "@/Store/Store";
import { InformationService } from "@/client";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { useEffect } from "react";
import StockList from "./StockList";

const LatestStockList: React.FC = () => {
  const { data: dateStr } = useSuspenseQuery({
    queryKey: ["LatestDate"],
    queryFn: () => {
      return InformationService.getLatestReportingDate();
    },
    gcTime: 0,
    staleTime: 0,
  });

  const { data } = useSuspenseQuery({
    queryKey: ["StockList", dateStr],
    queryFn: () => {
      return InformationService.getDocumentList({
        reportTypes: ["edjp", "edif", "edus"],
        dateStr: dateStr.reporting_date,
      });
    },
    gcTime: 0,
    staleTime: 0,
  });

  // データを新しい順にソート
  const sortData = data.data.slice().sort((a, b) => {
    const aDate = new Date(a.insert_date);
    const bDate = new Date(b.insert_date);
    if (aDate.getTime() === bDate.getTime()) {
      return a.securities_code.localeCompare(b.securities_code);
    }
    // 日付が同じ場合は証券コードでソート
    return bDate.getTime() - aDate.getTime();
  });

  // ストアを更新
  useEffect(() => {
    HeaderStore.setState((state) => ({
      ...state,
      SelectDateStr: dateStr.reporting_date,
      CurrentCategory: null,
    }));
  }, [dateStr]);
  return (
    <>
      <StockList data={sortData} count={sortData.length} />
    </>
  );
};

export default LatestStockList;
