import {
  Box,
  Heading,
  Image,
  Skeleton,
  Spacer,
  Stack,
  StackProps,
  Text,
} from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import React from "react";
import { XbrlQualitativeService } from "../../client";

interface SummaryQualitativeProps extends StackProps {
  head_item_key: string;
}

const SummaryQualitative: React.FC<SummaryQualitativeProps> = ({
  head_item_key,
  ...props
}) => {
  // フェードインアニメーション
  const fadeInSpin = `keyframes fadeInSpin {
  0% { opacity: 0; transform: rotate(0deg); }
  100% { opacity: 1; transform: rotate(360deg); }
  }`;

  // qualitative data
  const { data: items, status } = useQuery({
    queryKey: ["qualitative", head_item_key],
    queryFn: async () =>
      XbrlQualitativeService.readIxQualitativeItem({
        headItemKey: head_item_key,
      }),
    staleTime: 1000 * 60 * 60 * 24 * 7,
    gcTime: 1000 * 60 * 60 * 24 * 30,
  });

  if (status === "error") {
    return (
      <Box>
        <Text>この銘柄の定性的情報はありません。</Text>
      </Box>
    );
  }

  if (status === "pending") {
    return (
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        height="100vh"
        width="100%"
        flexDirection="column"
      >
        {[...Array(20)].map((_, i) => (
          <Skeleton key={i} height="20px" my={2} width="80%" />
        ))}
      </Box>
    );
  }

  const opeInfo = items?.qualitative_info;
  const fullText = opeInfo?.operating_result_info || "";
  const fullTextLines = fullText.split("\n").length;
  const sectorKey = opeInfo?.segment_info_key || [];
  const sectorInfo: { [key: string]: React.ReactNode } =
    (opeInfo?.segment_info as { [key: string]: React.ReactNode }) || {};
  const sectorPhoto: { [key: string]: string } =
    (opeInfo?.segment_photo_url as { [key: string]: string }) || {};

  return (
    <Stack
      direction={{ base: "column", md: "row" }}
      spacing={4}
      p={1}
      {...props}
      alignItems={{ md: "flex-start" }}
    >
      <Box
        width={{ base: "100%", md: "50%" }}
        bg="gray.100"
        p={2}
        boxShadow="md"
        animation={`${fadeInSpin} 10s linear`}
        display={fullText.length === 0 ? "none" : "block"}
      >
        <Heading as="h2" size="xs" m={2}>
          市場の動向と経営成績
        </Heading>
        <Box bg="white" p={2} boxShadow="md">
          {fullText.split("\n").map((line, index) => (
            <Text
              key={index}
              mb={4}
              fontSize="sm"
              lineHeight="32px"
              color="gray.600"
              display={
                line.match(/^セグメント.*/)
                  ? index > fullTextLines - 3
                    ? "none"
                    : "block"
                  : "block"
              }
            >
              {line}
            </Text>
          ))}
        </Box>
      </Box>
      <Box
        width={{ base: "100%", md: "50%" }}
        bg="gray.100"
        p={2}
        boxShadow="md"
        animation={`${fadeInSpin} 10s linear`}
        display={sectorKey.length === 0 ? "none" : "block"}
      >
        <Heading as="h2" size="xs" m={2}>
          セクター・トピックス
        </Heading>
        <Box bg="white" p={2} boxShadow="md">
          {sectorKey.map((sector, index) => (
            <Box key={index}>
              <Stack direction="row" align="center" m={4} spacing={4}>
                <Image
                  src={sectorPhoto[sector]}
                  alt={sector}
                  w="50px"
                  h="50px"
                  borderRadius="100%"
                />
                <Heading as="h4" size="xs" color="gray.800">
                  {sector}
                </Heading>
              </Stack>
              {typeof sectorInfo[sector] === "string"
                ? (sectorInfo[sector] as string)
                    ?.split("\n")
                    .map((line: string, index: number) => (
                      <Text
                        key={index}
                        fontSize="sm"
                        color="gray.600"
                        lineHeight="25px"
                        m={4}
                      >
                        {line}
                      </Text>
                    ))
                : null}
              <Spacer border="0.5px solid" borderColor="gray.300" />
            </Box>
          ))}
        </Box>
      </Box>
    </Stack>
  );
};

export default SummaryQualitative;
