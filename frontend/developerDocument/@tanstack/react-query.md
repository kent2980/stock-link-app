# @tanstic/react-Query

## 使い方

```
function dataInfo() {
    const { data } = useSuspenseQuery({
     queryKey: [constant, uniqueKey],    // 定数と変数の組み合わせ
     queryFn: () =>
 ...クエリの取得メソッド,
     staleTime: 10, //データが古いとみなされるまでの時間 (ミリ秒単位)
     gcTime: 10, //未使用または非アクティブなキャッシュ データがメモリ内に残る時間 (ミリ秒)
    }
}
```

useSuspenseQueryの場合、エラー発生時やデータ未取得時に表示する内容をDOM内に記述できる。

useQueryに比べて、可読性の高いコードを記述できる。

```
<Suspense
    fallback={
 <Box>
 ...エラー時、データ未取得時に表示する内容
 </Box>
>
    <Box>
      ...データの取得処理を行うコンポーネントをSuspenseの子要素にする
 <dataInfo />
    </BOX>
}
```
