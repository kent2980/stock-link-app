import {
  Stat,
  StatGroup,
  StatHelpText,
  StatLabel,
  StatNumber,
} from "@chakra-ui/react";
import React from "react";

interface SummaryStatProps {
  label: string;
  value: string | number;
  helpText?: string;
  priLabel: string;
  priValue: string | number;
  priHelpText?: string;
}

interface SummaryStatPropsList {
  summaries: SummaryStatProps[];
}

const SummaryStat: React.FC<SummaryStatPropsList> = ({ summaries }) => {
  return (
    <>
      {summaries.map((summary, index) => (
        <StatGroup key={index}>
          <Stat>
            <StatLabel>{summary.label}</StatLabel>
            <StatNumber>{summary.value}</StatNumber>
            {summary.helpText && (
              <StatHelpText>{summary.helpText}</StatHelpText>
            )}
          </Stat>
          <Stat>
            <StatLabel>{summary.priLabel}</StatLabel>
            <StatNumber>{summary.priValue}</StatNumber>
            {summary.priHelpText && (
              <StatHelpText>{summary.priHelpText}</StatHelpText>
            )}
          </Stat>
        </StatGroup>
      ))}
    </>
  );
};

export default SummaryStat;
