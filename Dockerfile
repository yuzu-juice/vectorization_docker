# ビルドステージ
FROM python:3.12-slim AS build-stage

# 作業ディレクトリを設定
WORKDIR /app

# requirements.txtをコピーして依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target /app

# モデルをコピー
COPY sbert-jsnli-luke-japanese-base-lite /app/model

# ランタイムステージ
FROM public.ecr.aws/lambda/python:3.12

# 作業ディレクトリを設定
WORKDIR ${LAMBDA_TASK_ROOT}

# ビルドステージから依存関係をコピー
COPY --from=build-stage /app /var/task

# app.pyをコピー
COPY app.py ${LAMBDA_TASK_ROOT}

# デフォルトコマンドを設定
CMD [ "app.handler" ]
