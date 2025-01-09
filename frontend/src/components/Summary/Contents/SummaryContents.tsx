import { Heading, SimpleGrid } from "@chakra-ui/react";
import React from "react";
import { SummaryProps } from "../Props/SummaryProps";
import DividendTable, { DividendPerShare } from "../Table/DividendTable";
import IssuedSharesTable, {
  IssuedSharesTableProp,
} from "../Table/IssuedSharesTable";
import SummaryList from "../Table/SummaryList";

export interface SummaryContentsProps {
  opeInfos: SummaryProps[];
  finInfos: SummaryProps[];
  dividends: DividendPerShare[];
  forecasts: SummaryProps[];
  issuedShares: IssuedSharesTableProp;
}

export interface SummaryContentsItems {
  items: SummaryContentsProps;
}

const SummaryContents: React.FC<SummaryContentsItems> = ({ items }) => {
  let headingCount = 1;
  return (
    <SimpleGrid gap={3} px={2} py={4}>
      <Heading as="h2" size="sm" alignSelf="flex-start" p={2}>
        {headingCount++}. 連結経営成績
      </Heading>
      <SummaryList summaries={items.opeInfos} />
      <Heading as="h2" size="sm" alignSelf="flex-start" p={2}>
        {headingCount++}. 連結財政状態
      </Heading>
      <SummaryList summaries={items.finInfos} />
      {items.dividends.length > 0 && (
        <>
          <Heading as="h2" size="sm" alignSelf="flex-start" p={2}>
            {headingCount++}. 配当の状況
          </Heading>
          <DividendTable dividends={items.dividends} />
        </>
      )}
      {items.forecasts.length > 0 && (
        <>
          <Heading as="h2" size="sm" alignSelf="flex-start" p={2}>
            {headingCount++}. 通期の連結業績予測
          </Heading>
          <SummaryList summaries={items.forecasts} />
        </>
      )}
      <Heading as="h2" size="sm" alignSelf="flex-start" p={2}>
        {headingCount++}. 株式の状況
      </Heading>
      <IssuedSharesTable items={items.issuedShares} />
    </SimpleGrid>
  );
};

export default SummaryContents;
