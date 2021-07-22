import requests
import json

from google.cloud import storage
from datetime import datetime, timedelta, timezone

API_ENDPOINT = "https://jsonplaceholder.typicode.com/posts"
BUCKET_NAME = "test-api-data"

def data_uploader(request):
    """fetch data and upload to GCS
    """
    JST = timezone(timedelta(hours=+9), 'JST')

    data = fetcher(API_ENDPOINT)

    file_name = getFileName(datetime.now(JST))

    repository(BUCKET_NAME, file_name, data)

    # TODO: 適切なreturnを調査する
    return "OK"

def getFileName(time: datetime) -> str:
    return f'data_{time}.json'

def fetcher(url: str) -> str:
    """fetch api data and return json string
    """
    print(f"Access: {url}")
    response = requests.get(url)

    # Raise error if status code is not 200
    response.raise_for_status()

    data = response.json()
    return json.dumps(data)

def repository(bucket_name: str, file_name: str, data: str):
    """upload json file to GCS
    """
    # Select Bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    print(f'Bucket: {bucket.name}')

    # Upload Data
    blob = bucket.blob(file_name)
    # TODO: jsonの場合のcontent_typeを調査する
    blob.upload_from_string(data, content_type='application/json')
    print(f"Uploaded: {file_name}")

if __name__ == "__main__":
    pass
