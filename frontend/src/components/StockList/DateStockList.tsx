import { HeaderStore } from "@/Store/Store";
import { InformationService } from "@/client";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { useEffect } from "react";
import StockList from "./StockList";

interface DateStockListProps {
  dateStr: string | null;
}

const DateStockList: React.FC<DateStockListProps> = ({ dateStr }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["DateStockList", dateStr],
    queryFn: () => {
      return InformationService.getDocumentList({
        reportTypes: ["edjp", "edif", "edus"],
        dateStr: dateStr,
      });
    },
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
      <StockList data={data} />
    </>
  );
};

export default DateStockList;
