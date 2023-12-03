# LINE Notifier

讓訂單可以透過通知打到 LINE 上面

## 安裝與執行

首先，請確保你的環境已經安裝 Python 3.7 或以上的版本。

Clone 這個專案到你的本地環境：
```
git clone git@github.com:gcp-serverless-workshop/notifier-line.git
cd notifier-line/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

環境變數請參考 `.env.sample`，其中 LOTIFY_ACCESS_TOKEN 可透過 [flask-line-notify](https://github.com/louis70109/flask-line-notify) 來佈署取得

如果你需要本地端測試 pub/sub 的話需要透過代理才可以

```
ngrok http 8080
```

## Google Cloud Platform 佈署

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

Clone 此專案

```
git clone git@github.com:gcp-serverless-workshop/notifier-line.git
cd notifier-line/
```

### gcloud 基礎設定

- `gcloud init`：初始化 gcloud CLI，該指令會提示登錄 Google 帳戶，並選擇您要使用的 GCP 項目。
- `gcloud config set project PROJECT_ID`：設定 GCP Project ID，以便 gcloud CLI 與該項目交互使用。
- `gcloud auth login`：登錄 Google 帳戶。

透過 [gcloud](https://cloud.google.com/sdk/docs/install?hl=zh-cn) 指令佈署

```
gcloud run deploy notifier-line-1 --source .
```

> 佈署參考: [【GCP】將 FastAPI 佈署上 Cloud Run](https://nijialin.com/2023/03/19/gcp-why-need-cloudrun-as-serverless/#5-%E4%BD%88%E7%BD%B2%E5%88%B0-Google-Cloud-Run)

## 問題

### Cloud Shell 中遇到 unauthorized: You don't have the needed permissions to perform this operation, and you may have invalid credentials.

參考 [stack overflow 解答](https://stackoverflow.com/questions/55446787/permission-issues-while-docker-push)，請先使用以下指令協助開啟權限

```
gcloud auth configure-docker # Y
```

透過 `rm` 刪除資料夾之後，再重新跑一次以下指令佈署

```
cloudshell_open --repo_url "https://github.com/gcp-serverless-workshop/notifier-line.git" --page "shell" --force_new_clone
```

## 參與貢獻

如果你有任何問題或建議，歡迎開 issue 或 pull request。

## LICENSE

請見 LICENSE 文件。
