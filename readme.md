# 日本語テキストのベクトル化サービス

このリポジトリは、LUKE-based SBERT モデルを使用して日本語テキストをベクトル埋め込みに変換する Flask ベースの API サービスです。Docker コンテナ化されており、簡単にデプロイできます。

## 特徴

- テキストのベクトル化のための RESTful API エンドポイント
- `sbert-jsnli-luke-japanese-base-lite`モデルを使用
- Docker 対応で簡単デプロイ
- パフォーマンスモニタリング機能付き
- JSON 形式の入出力をサポート

## 前提条件

- Docker
- Git LFS（モデルのダウンロードに必要）
- Python 3.12 以降（ローカルで実行する場合）

## モデルのセットアップ

まず、Hugging Face から必要なモデルをダウンロードします：

```bash
git lfs install
git clone https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite
```

## ビルドと実行方法

1. Docker イメージのビルド：

```bash
docker build -t japanese-text-vectorizer:latest .
```

2. コンテナの実行：

```bash
docker run -p 9000:8080 japanese-text-vectorizer:latest
```

## API 仕様

サービスは 2 つのエンドポイントを提供します：

### 1. ヘルスチェック

- **エンドポイント**: GET `/`
- **レスポンス**: サービスが稼働中であることを示す簡単なテキスト

### 2. テキストのベクトル化

- **エンドポイント**: POST `/vectorize`
- **入力形式**:

```json
{
  "text": "ベクトル化したい日本語テキストをここに入力"
}
```

- **レスポンス**: ベクトル埋め込みの配列

## リクエスト例

PowerShell を使用する場合：

```powershell
Invoke-RestMethod -Method Post -Uri "http://localhost:9000/2015-03-31/functions/function/invocations" -Body (Get-Content -Raw -Path .\event.json) -ContentType "application/json"
```

## プロジェクト構成

```
├── .gitignore              # Gitの除外設定ファイル
├── Dockerfile              # Dockerの設定ファイル
├── app.py                  # メインアプリケーションコード
├── event.json             # サンプルリクエストのペイロード
├── readme.md              # 本ドキュメント
└── requirements.txt       # Pythonの依存パッケージ一覧
```

## 依存パッケージ

requirements.txt を参照

## 注意事項

- サービスはコンテナ内でポート 8080 を使用
- デフォルトの設定ではホスト側のポート 9000 にマッピング
- 各リクエストのパフォーマンスメトリクスがログに記録されます

## トラブルシューティング

エラーが発生した場合は、以下を確認してください：

- モデルが正しくダウンロードされているか
- Docker が正常に起動しているか
- ポートの競合がないか
- リクエストの JSON フォーマットが正しいか
