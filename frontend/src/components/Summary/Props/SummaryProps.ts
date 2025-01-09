export interface SummaryProps {
  title: string;
  value?: {
    cur: string | number;
    pri?: string | number;
  };
  changeValue?: {
    cur: number;
    pri?: number;
  };
  valueScale?: string;
}

export interface SummaryPropsList {
  summaries: SummaryProps[];
}
