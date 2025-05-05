import { FinancialSummaryService, FinValueBase } from "@/client";
import CustomSpinner from "@/components/Spinner/CustomSpinner";
import {
  Badge,
  Box,
  Button,
  CloseButton,
  Dialog,
  FormatNumber,
  Portal,
  Stat,
  StatRootProps,
  Text,
  VStack,
  Wrap,
} from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import React, { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

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
        {data?.forecast?.data?.map((item, index) => (
          <ForecastItem
            key={index}
            label={item.label}
            value={item.curValue?.value}
            valueScale={item.curValue?.display_scale}
            changeValue={item.curChange}
          />
        ))}
      </Wrap>
    </Box>
  );
};
export default ForecastTable;

interface ForecastItemProps extends StatRootProps {
  label: string;
  value?: number | null | undefined;
  valueScale?: string | null | undefined;
  changeValue?: FinValueBase | null | undefined;
}
const ForecastItem: React.FC<ForecastItemProps> = ({
  label,
  value,
  valueScale,
  changeValue,
  ...props
}) => {
  return (
    <Stat.Root borderWidth="1px" borderRadius="lg" p={4} bg="white" {...props}>
      <Stat.Label>{label}</Stat.Label>
      <VStack>
        <Stat.ValueText>
          {value && valueScale && (
            <>
              <FormatNumber value={value} style="currency" currency="JPY" />
              <Text fontSize="12px">{valueScale}</Text>
            </>
          )}
        </Stat.ValueText>
        {changeValue !== null &&
          changeValue !== undefined &&
          (changeValue.value !== null ? (
            <>
              <Badge
                colorPalette={changeValue.value > 0 ? "green" : "red"}
                gap="0"
              >
                {changeValue.value > 0 ? (
                  <Stat.UpIndicator />
                ) : (
                  <Stat.DownIndicator />
                )}
                <FormatNumber
                  value={changeValue.value / 100}
                  style="percent"
                  maximumFractionDigits={2}
                  minimumFractionDigits={1}
                />
              </Badge>
            </>
          ) : (
            <Badge
              colorPalette="gray"
              gap="0"
              minW="50px"
              justifyContent="center"
            >
              <Text fontSize="12px">-</Text>
            </Badge>
          ))}
      </VStack>
    </Stat.Root>
  );
};

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
        {data?.forecast?.data?.map((item, index) => (
          <ForecastItem
            key={index}
            label={item.label}
            value={item.curValue?.value}
            valueScale={item.curValue?.display_scale}
            changeValue={item.curChange}
          />
        ))}
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
