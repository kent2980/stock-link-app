import { HeaderStore } from "@/Store/Store";
import { InformationService } from "@/client";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { useEffect } from "react";
import StockList from "./StockList";

interface DateStockListProps {
  dateStr: string | null;
}

const DateStockList: React.FC<DateStockListProps> = ({ dateStr }) => {
  const cashTime = () => {
    if (dateStr === new Date().toISOString().slice(0, 10)) {
      return 0;
    } else {
      return 30 * 60 * 1000 * 24 * 60 * 60; // 30 days
    }
  };

  const { data } = useSuspenseQuery({
    queryKey: ["StockList", dateStr],
    queryFn: () => {
      return InformationService.getDocumentList({
        reportTypes: ["edjp", "edif", "edus"],
        dateStr: dateStr,
      });
    },
    gcTime: cashTime(),
    staleTime: cashTime(),
  });

  const sortData = data.data.slice().sort((a, b) => {
    return a.securities_code.localeCompare(b.securities_code);
  });

  // ストアを更新
  useEffect(() => {
    HeaderStore.setState((state) => ({
      ...state,
      SelectDateStr: dateStr,
      CurrentCategory: null,
    }));
  }, [dateStr]);
  return (
    <>
      <StockList data={sortData} count={sortData.length} />
    </>
  );
};

export default DateStockList;
