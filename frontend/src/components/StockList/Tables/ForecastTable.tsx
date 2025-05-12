import { FinancialSummaryService, FinValueFinance } from "@/client";
import CustomSpinner from "@/components/Spinner/CustomSpinner";
import {
  Box,
  Button,
  CloseButton,
  Dialog,
  FormatNumber,
  Portal,
  Stack,
  Table,
  Text,
  VStack,
} from "@chakra-ui/react";
import { useSuspenseQuery } from "@tanstack/react-query";
import { StackDirection } from "node_modules/@chakra-ui/react/dist/types/components/stack/get-separator-style";
import React, { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

const getDisplayValue = (item: FinValueFinance, direction: StackDirection) => {
  if (item.forecast?.isActive == true) {
    return (
      <VStack>
        <Stack direction={direction} alignItems="center" gap={0}>
          <FormatNumber value={item.forecast.curValue?.value ?? 0} />
          <Text fontSize={"8px"}>
            {item.forecast.curValue?.display_scale ?? ""}
          </Text>
        </Stack>
        <Text>
          {item.forecast.curChange?.value
            ? item.forecast.curChange.value + "%"
            : "-"}
        </Text>
      </VStack>
    );
  } else if (item.upper?.isActive == true && item.lower?.isActive == true) {
    return (
      <Stack direction={direction} alignItems="center" gap={0}>
        <FormatNumber value={item.lower?.curValue?.value ?? 0} />
        <Text fontSize={"8px"}>
          {item.lower?.curValue?.display_scale ?? ""}
        </Text>
        <Text fontSize={"8px"}>~</Text>
        <FormatNumber value={item.upper?.curValue?.value ?? 0} />
        <Text fontSize={"8px"}>
          {item.upper?.curValue?.display_scale ?? ""}
        </Text>
      </Stack>
    );
  } else {
    return <Text>-</Text>;
  }
};

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
      <Table.Root size={{ base: "sm", md: "md" }}>
        <Table.ColumnGroup>
          <Table.Column htmlWidth="5%" />
          {Array(0, 4).map((index) => {
            return <Table.Column key={index} htmlWidth="20%" />;
          })}
        </Table.ColumnGroup>
        <Table.Header>
          <Table.Row>
            <Table.ColumnHeader textAlign="center">期間</Table.ColumnHeader>
            {data.data?.map((item, key) => {
              if (key > 4) return null;
              return (
                <Table.ColumnHeader key={key} textAlign="center">
                  {item.label}
                </Table.ColumnHeader>
              );
            })}
          </Table.Row>
        </Table.Header>
        <Table.Body>
          <Table.Row>
            <Table.ColumnHeader>通期</Table.ColumnHeader>
            {data.data?.map((item, key) => {
              if (key > 4) return null;
              return (
                <Table.Cell key={key} textAlign="center">
                  {getDisplayValue(item, "column")}
                </Table.Cell>
              );
            })}
          </Table.Row>
        </Table.Body>
      </Table.Root>
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
      <Table.Root size={{ base: "sm", md: "md" }}>
        <Table.ColumnGroup>
          <Table.Column htmlWidth="5%" />
          {Array(0, 4).map((index) => {
            return <Table.Column key={index} htmlWidth="20%" />;
          })}
        </Table.ColumnGroup>
        <Table.Header>
          <Table.Row>
            <Table.ColumnHeader textAlign="center">期間</Table.ColumnHeader>
            {data.data?.map((item, key) => {
              if (key > 4) return null;
              return (
                <Table.ColumnHeader key={key} textAlign="center">
                  {item.label}
                </Table.ColumnHeader>
              );
            })}
          </Table.Row>
        </Table.Header>
        <Table.Body>
          <Table.Row>
            <Table.ColumnHeader>通期</Table.ColumnHeader>
            {data.data?.map((item, key) => {
              if (key > 4) return null;
              return (
                <Table.Cell key={key} textAlign="center">
                  {getDisplayValue(item, "column")}
                </Table.Cell>
              );
            })}
          </Table.Row>
        </Table.Body>
      </Table.Root>
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
