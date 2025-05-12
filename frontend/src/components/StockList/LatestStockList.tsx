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
  });

  const { data } = useSuspenseQuery({
    queryKey: ["StockList", dateStr],
    queryFn: () => {
      return InformationService.getDocumentList({
        reportTypes: ["edjp", "edif", "edus"],
        dateStr: dateStr.reporting_date,
      });
    },
  });

  // データを新しい順にソート
  const sortData = data.data.slice().sort((a, b) => {
    return b.insert_date.localeCompare(a.insert_date);
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
