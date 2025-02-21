import React from "react";
interface WikiInfoErrorBoundState {
  hasError: boolean;
}

interface WikiInfoErrorBoundProps {
  children: React.ReactNode;
}

class WikiInfoErrorBound extends React.Component<
  WikiInfoErrorBoundProps,
  WikiInfoErrorBoundState
> {
  constructor(props: any) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: any) {
    // エラーが発生した場合に状態を更新
    return { hasError: true };
  }

  componentDidCatch(error: any, errorInfo: any) {
    // エラーログを外部サービスに送信するなどの処理
    console.error("Error caught in WikiInfoErrorBound:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // エラーが発生した場合に表示するUI
      return <h1>表示するデータがありません。</h1>;
    }

    return this.props.children;
  }
}

export default WikiInfoErrorBound;
