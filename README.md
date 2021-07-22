# sample-cloud-functions-uploader
Cloud Functionsで外部APIからデータを取得し、Cloud Storageに保存するサンプルスクリプト

[【GCP】Cloud Functionsで外部APIからデータを定期取得しCloud Storageに保存する](https://blog.marusho.io/repository-with-cloud-functions)

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
gcloud functions deploy data-uploader --entry-point data_uploader --runtime python37 --trigger-http
gcloud scheduler jobs create http daily-data-uploader --schedule="every 24 hours" --uri=<ENDPOINT> --oidc-service-account-email=<serviceAccountEmail>
```

