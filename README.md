# sample-cloud-functions-uploader
Cloud Functionsで外部APIからデータを取得し、Cloud Storageに保存するサンプルスクリプト

## gcloudコマンドの初期設定

- ログイン
```
gcloud auth login
```

- プロジェクトの選択
```
gcloud config set project <Yout Project>
```

## デプロイ

- デプロイ

```
cd functions
gcloud functions deploy <function_name> --entry-point <function> --runtime python37 --timeout=300 --trigger-http --allow-unauthenticated
```

