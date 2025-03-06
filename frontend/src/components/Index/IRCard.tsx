import { IxService } from "@/client";
import { Badge, Box, Card, Skeleton, Text } from "@chakra-ui/react";
import { useSuspenseQueries } from "@tanstack/react-query";
import { useNavigate } from "@tanstack/react-router";
import { Suspense } from "react";
import CustomCard from "./CustomCard";
interface IRCardProps {
  select_date: null | undefined | string;
}

function IRCard({ select_date }: IRCardProps) {
  const navigate = useNavigate({
    from: "/",
  });

  const handleCardClick = () => {
    navigate({ to: "/store" });
  };
  return (
    <CustomCard onClick={handleCardClick} cursor="pointer">
      <Card.Header>
        <Card.Title fontSize="md">IR Store</Card.Title>
        <Card.Description fontSize="sm">新規報告書のお知らせ</Card.Description>
      </Card.Header>
      <Suspense
        fallback={
          <Card.Body>
            <Skeleton height="20px" />
            <Box>
              <Badge colorPalette="purple" mt={2}>
                新着アイテム
              </Badge>
              <Skeleton height="20px" />
            </Box>
          </Card.Body>
        }
      >
        <CustomCardBody select_date={select_date} />
      </Suspense>
    </CustomCard>
  );
}

export default IRCard;

interface CustomCardBodyProps extends Card.BodyProps {
  select_date: null | undefined | string;
}

function CustomCardBody({ select_date, ...props }: CustomCardBodyProps) {
  const [firstQuery, secondQuery] = useSuspenseQueries({
    queries: [
      {
        queryKey: ["DocumentCount", select_date],
        queryFn: async () => {
          return IxService.getDocumentCount({
            dateStr: select_date,
          });
        },
      },
      {
        queryKey: ["latest Document", select_date],
        queryFn: async () => {
          return IxService.getLatestDocumentTitle();
        },
      },
    ],
  });
  return (
    <Card.Body {...props} gap={2}>
      <Text>本日の報告件数は、{firstQuery.data}件です。</Text>
      {/* <Separator my={2} /> */}
      <Box>
        <Badge colorPalette="purple" mt={2}>
          新着アイテム
        </Badge>
        <Text fontSize={11} mt={2}>
          {secondQuery.data}
        </Text>
      </Box>
    </Card.Body>
  );
}
