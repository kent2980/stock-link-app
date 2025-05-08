import { FinancialSummaryService } from "@/client";
import CustomSpinner from "@/components/Spinner/CustomSpinner";
import {
  Box,
  Button,
  CloseButton,
  Dialog,
  Portal,
  Text,
  Wrap,
} from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";
import FinStructWrapItem from "./FinStructTable";
import FinStructUpperAndLowerWrapItem from "./FinStructUpperAndLowerTable";

interface ForecastTableProps {
  HeadItemKey: string;
}

const ForecastTable: React.FC<ForecastTableProps> = ({ HeadItemKey }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["forecastData", HeadItemKey],
    queryFn: async () => {
      return await FinancialSummaryService.getForecasts({
        headItemKey: HeadItemKey,
      });
    },
  });
  return (
    <Box>
      <IsChangeForecast HeadItemKey={HeadItemKey} />
      <Wrap>
        {data?.data?.map((item, index) => (
          <>
            {item.forecast?.isActive == true && (
              <FinStructWrapItem
                key={index}
                label={item.label}
                value={item.forecast?.curValue?.value}
                valueScale={item.forecast?.curValue?.display_scale}
                changeValue={item.forecast?.curChange}
              />
            )}
            {item.lower?.isActive == true && item.upper?.isActive == true && (
              <FinStructUpperAndLowerWrapItem
                key={index}
                label={item.label}
                downValue={item.lower?.curValue?.value}
                downValueScale={item.lower?.curValue?.display_scale}
                downChangeValue={item.lower?.curChange}
                upValue={item.upper?.curValue?.value}
                upValueScale={item.upper?.curValue?.display_scale}
                upChangeValue={item.upper?.curChange}
              />
            )}
          </>
        ))}
      </Wrap>
    </Box>
  );
};
export default ForecastTable;

interface IsChangeForecastProps {
  HeadItemKey: string;
}

const IsChangeForecast: React.FC<IsChangeForecastProps> = ({ HeadItemKey }) => {
  // 業績予想の修正を取得する
  const { data } = useSuspenseQuery({
    queryKey: ["isChangeForecast", HeadItemKey],
    queryFn: async () => {
      return await FinancialSummaryService.getForecastChange({
        headItemKey: HeadItemKey,
      });
    },
  });
  return (
    <Box display="flex" flexDir="row" fontSize={"xs"} m={2} p={1}>
      {data !== null ? (
        data ? (
          <>
            <Text alignSelf="center">業績予想の修正：有り</Text>
            <CustomDialog
              buttonLabel="→ 修正前はこちら"
              dialogTitle="修正前業績予想"
            >
              <ErrorBoundary fallback={<Box>表示するデータがありません。</Box>}>
                <Suspense fallback={<CustomSpinner />}>
                  <PriorForecastTable HeadItemKey={HeadItemKey} />
                </Suspense>
              </ErrorBoundary>
            </CustomDialog>
          </>
        ) : (
          <Text>業績予想の修正：無し</Text>
        )
      ) : (
        <Text>新しい業績予想が発表されました</Text>
      )}
    </Box>
  );
};

const PriorForecastTable: React.FC<ForecastTableProps> = ({ HeadItemKey }) => {
  const { data } = useSuspenseQuery({
    queryKey: ["priorForecastData", HeadItemKey],
    queryFn: async () => {
      return await FinancialSummaryService.getForecasts({
        headItemKey: HeadItemKey,
        offset: 1,
        reportTypes: ["edjp", "edif", "edus"],
      });
    },
    retry: false,
  });
  return (
    <Box>
      <Wrap>
        {data?.data?.map((item, index) => {
          return (
            <>
              {item.forecast?.isActive == true && (
                <FinStructWrapItem
                  key={index}
                  label={item.label}
                  value={item.forecast?.curValue?.value}
                  valueScale={item.forecast?.curValue?.display_scale}
                  changeValue={item.forecast?.curChange}
                />
              )}
              {item.lower?.isActive == true && item.upper?.isActive == true && (
                <FinStructUpperAndLowerWrapItem
                  key={index}
                  label={item.label}
                  downValue={item.lower?.curValue?.value}
                  downValueScale={item.lower?.curValue?.display_scale}
                  downChangeValue={item.lower?.curChange}
                  upValue={item.upper?.curValue?.value}
                  upValueScale={item.upper?.curValue?.display_scale}
                  upChangeValue={item.upper?.curChange}
                />
              )}
            </>
          );
        })}
      </Wrap>
    </Box>
  );
};

interface CustomDialogProps {
  buttonLabel: string;
  dialogTitle: string;
  children: React.ReactNode;
}

const CustomDialog: React.FC<CustomDialogProps> = ({
  buttonLabel,
  dialogTitle,
  children,
}) => {
  return (
    <Dialog.Root
      placement="top"
      motionPreset="slide-in-left"
      preventScroll={false}
    >
      <Dialog.Trigger asChild>
        <Button
          variant="plain"
          size="sm"
          fontSize={"xs"}
          textDecoration="underline"
        >
          {buttonLabel}
        </Button>
      </Dialog.Trigger>
      <Portal>
        <Dialog.Backdrop />
        <Dialog.Positioner>
          <Dialog.Content>
            <Dialog.Header>
              <Dialog.Title>{dialogTitle}</Dialog.Title>
              <Dialog.CloseTrigger asChild>
                <CloseButton size="sm" />
              </Dialog.CloseTrigger>
            </Dialog.Header>
            <Dialog.Body>{children}</Dialog.Body>
          </Dialog.Content>
        </Dialog.Positioner>
      </Portal>
    </Dialog.Root>
  );
};
