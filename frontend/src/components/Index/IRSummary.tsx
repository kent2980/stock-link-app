import { FinResultStruct, SummaryService } from "@/client";
import { Badge, Box, FormatNumber, HStack, Stat } from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { Suspense } from "react";

interface IXSummaryProps {
  head_item_key: string;
}

function IRSummary({ head_item_key }: IXSummaryProps) {
  return (
    <Box>
      <Suspense fallback={<div>Loading...</div>}>
        <OperatingResult head_item_key={head_item_key} />
      </Suspense>
    </Box>
  );
}

function OperatingResult({ head_item_key }: IXSummaryProps) {
  const { data } = useSuspenseQuery({
    queryKey: ["IRSummary", head_item_key],
    queryFn: async () => {
      return await SummaryService.getOperatingResults({
        headItemKey: head_item_key,
      });
    },
  });
  return (
    <Box>
      {data.data.map((item: FinResultStruct) => {
        return (
          <>
            {item?.result?.data?.map((result) => {
              return (
                <Box border="1px solid" borderColor="gray.400" p={2} m={2}>
                  <Stat.Root>
                    <Stat.Label>{result.label}</Stat.Label>
                    <HStack>
                      <Stat.ValueText>
                        <FormatNumber value={result.curValue?.value ?? 0} />
                      </Stat.ValueText>
                      <Stat.HelpText>
                        {result.curValue?.display_scale}
                      </Stat.HelpText>
                      {(result.curChange?.value ?? 0) > 0 ? (
                        <Badge colorPalette="green">
                          <Stat.UpIndicator />
                          <FormatNumber
                            value={(result.curChange?.value ?? 0) / 100}
                            style="percent"
                            maximumFractionDigits={1}
                            minimumFractionDigits={1}
                          />
                        </Badge>
                      ) : (
                        <Badge colorPalette="red">
                          <Stat.DownIndicator />
                          <FormatNumber
                            value={(result.curChange?.value ?? 0) / 100}
                            style="percent"
                            maximumFractionDigits={1}
                            minimumFractionDigits={1}
                          />
                        </Badge>
                      )}
                    </HStack>
                  </Stat.Root>
                </Box>
              );
            })}
          </>
        );
      })}
    </Box>
  );
}

export default IRSummary;
