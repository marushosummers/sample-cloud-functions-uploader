import requests
from google.cloud import storage
from datetime import date, timedelta, timezone

API_ENDPOINT = "https://jsonplaceholder.typicode.com/posts"
BUCKET_NAME = ""

def data_collector(request):
    """fetch data and save to GCS
    """
    JST = timezone(timedelta(hours=+9), 'JST')

    data = fetcher(API_ENDPOINT)

    file_name = getFileName(date.today(JST))

    repository(BUCKET_NAME, file_name, data)

    return "OK"

def getFileName(_date: date) -> str:
    return f'data{_date}.json'

def fetcher(url: str):
    # fetch
    print(f"Access: {API_ENDPOINT}")
    r = requests.get(API_ENDPOINT)

    # save
    print(r.status_code)
    if r.status_code != requests.codes.ok:
        print("HTTP Error: Skip this file")
    else:
        stream = r.content

    return stream

def repository(bucket_name: str, save_path: str, data: str):
    # Select Bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    print(f'Bucket: {bucket.name}')

    # Save Data
    blob = bucket.blob(save_path)
    
    # TODO: jsonの場合のcontent_typeを調査する
    blob.upload_from_string(data)
    print(f"Saved: {save_path}")



if __name__ == "__main__":
    pass
